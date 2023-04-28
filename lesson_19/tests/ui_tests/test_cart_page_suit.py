import allure
import pytest

from ...page_objects.computer_product_page import ComputerProductPage
from ...utilities.waiters import wait_until


@allure.title('Successful order of product')
@pytest.mark.regression
def test_cart_page(open_computers_page, open_login_page, config_data):
    login_page = open_login_page

    email = config_data.test_data['email']
    password = config_data.test_data['password']

    with allure.step('Make login'):
        main_page = login_page.set_password(password).set_email(email).click_login_button()

    with allure.step('Open computer page, add product to cart'):
        computer_page = main_page.open_computer_page()
        product_page = computer_page.add_product_to_cart(product_index=2)

    description = computer_page.description
    price = computer_page.price

    title = product_page.get_product_title()
    product_price = product_page.get_current_price()

    assert title == description and price == product_price, 'Product is added properly'

    with allure.step('Add product to cart'):
        product_page.set_processor_radio('fast').set_ram_radio('8_gb').set_hdd_radio('400_gb')
        product_page.set_additional_options(['image_viewer', 'office_suite', 'other_office_suite'])
        product_page.set_qty('10')

        processor_cost = float(product_page.set_processor_radio(value='fast', is_get_text=True))
        ram_cost = float(product_page.set_ram_radio(value='8_gb', is_get_text=True))
        hdd_cost = float(product_page.set_hdd_radio(value='400_gb', is_get_text=True))
        product_page.set_additional_options(['image_viewer', 'office_suite', 'other_office_suite'], is_get_text=True)
        additional_options = sum(ComputerProductPage.prices)

        product_page.add_to_cart()

    with allure.step('Go to Cart page'):
        cart_page = product_page.go_to_cart_page()

    price_with_all_options = float(price) + processor_cost + ram_cost + hdd_cost + additional_options
    cart_price = wait_until(cart_page.get_price)

    qty = cart_page.get_qty()
    total_price = cart_page.get_total_price()

    assert float(cart_price) == price_with_all_options, \
        'Price is incorrect'
    assert qty == '10', 'Qty is incorrect'
    assert float(total_price) == (float(price) + processor_cost + ram_cost + hdd_cost + additional_options) * 10, \
        'Total price is incorrect'

    with allure.step('Finish order'):
        cart_page.set_country("Ukraine").set_zip('65123').set_agree_checkbox()
        cart_page.click_checkout_button().click_billing_button()
        cart_page.click_shipping_address_button()
        cart_page.set_shipping_method('next_day_air')
        cart_page.set_payment_method('check')
        cart_page.click_payment_information_button()
        order_status_page = cart_page.click_final_button()

    title = order_status_page.get_page_title(title_selector=order_status_page._page_title)
    status = order_status_page.get_order_status()

    assert title == 'Thank you' and status == 'Your order has been successfully processed!', \
        'Order is not created'

    main_page = order_status_page.click_continue_button()

    assert main_page.get_signed_value() == email, 'Main page is not returned after order creation'
