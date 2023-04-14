import time

from ..utilities.config_parser import get_test_data


def test_cart_page(open_computers_page, open_login_page):
    login_page = open_login_page

    email, password = get_test_data()
    main_page = login_page.set_password(password).set_email(email).click_login_button()

    computer_page = main_page.open_page()
    product_page = computer_page.add_product_to_cart(product_index=2)

    description = computer_page.description
    price = computer_page.price

    title = product_page.get_product_title()
    product_price = product_page.get_current_price()

    assert title == description and price == product_price, 'Product is added properly'

    product_page.set_processor_radio('fast').set_ram_radio('8_gb').set_hdd_radio('400_gb')
    product_page.set_additional_options(['image_viewer', 'office_suite', 'other_office_suite'])
    product_page.set_qty('10')
    product_page.add_to_cart()

    cart_page = product_page.go_to_cart_page()
    cart_price = cart_page.get_price()
    qty = cart_page.get_qty()
    total_price = cart_page.get_total_price()

    assert cart_price == '2205.00' and qty == '10' and total_price == '22050.00', \
        'Product attributes are different'

    cart_page.set_country("Ukraine").set_zip('65123').set_agree_checkbox()
    cart_page.click_checkout_button().click_billing_button()
    cart_page.click_shipping_address_button()
    cart_page.set_shipping_method('next_day_air')
    cart_page.set_payment_method('check')
    cart_page.click_payment_information_button()
    order_status_page = cart_page.click_final_button()

    title = order_status_page.get_page_title()
    status = order_status_page.get_order_status()

    assert title == 'Thank you' and status == 'Your order has been successfully processed!', \
        'Order is not created'

    main_page = order_status_page.click_continue_button()

    assert main_page.get_signed_value() == email, 'Main page is not returned after order creation'



