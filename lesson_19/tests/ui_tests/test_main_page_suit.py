import allure
import pytest


@allure.title('Check login from Main page')
@pytest.mark.regression
def test_check_login(open_main_page, config_data):
    main_page_driver = open_main_page

    email = config_data.test_data['email']
    password = config_data.test_data['password']

    with allure.step('Make login'):
        login_page = main_page_driver.click_login()
        main_page = login_page.set_email(email).set_password(password).click_login_button()
        signed_user = main_page.get_signed_value()

        assert signed_user == email, 'User successfully logged in'
        return main_page


@allure.title('Check logout from Main page')
@pytest.mark.regression
def test_check_log_out(make_login):
    login_to_account = make_login

    with allure.step('Make logout'):
        login_to_account.make_logout()
        name = login_to_account.get_unsigned_value()

        assert name == 'Register', 'User successfully logged out'


@allure.title('Check navigation links text')
@pytest.mark.regression
@pytest.mark.parametrize('urls,text',
                         [('books_url', 'BOOKS'), ('computers_url', 'COMPUTERS'), ('electronics_url', 'ELECTRONICS'),
                          ('apparel_shoes_url', 'APPAREL & SHOES'), ('digital_url', 'DIGITAL DOWNLOADS'),
                          ('jewerly_url', 'JEWELRY'), ('gift_cards', 'GIFT CARDS')])
def test_check_navigation_links_text(open_main_page, urls, text):
    main_page_driver = open_main_page

    with allure.step('Check navigation links text'):
        link = main_page_driver.get_navigation_link_text(url=urls)
        assert link == text, 'Text in link is wrong'


@allure.title('Check navigation links transitions')
@pytest.mark.regression
@pytest.mark.parametrize('urls,text',
                         [('books_url', 'Books'), ('computers_url', 'Computers'), ('electronics_url', 'Electronics'),
                          ('apparel_shoes_url', 'Apparel & Shoes'), ('digital_url', 'Digital downloads'),
                          ('jewerly_url', 'Jewelry'), ('gift_cards', 'Gift Cards')])
def test_check_navigation_links_transitions(open_main_page, urls, text):
    main_page_driver = open_main_page

    with allure.step('Check navigation links transitions'):
        page = main_page_driver.get_navigation_link(url=urls)
        page_title = page.get_page_title(title_selector=page._page_title)
        assert page_title == text, 'Transition is incorrect'


@allure.title('Check search transitions')
@pytest.mark.regression
def test_search_transition(open_main_page):
    main_page_driver = open_main_page

    with allure.step('Go to Search page'):
        main_page_driver.send_keys_search(keys='Computer')
        search_page = main_page_driver.click_search_button()

        title = search_page.get_page_title(title_selector=search_page._page_title)
        assert title == 'Search', 'Transition is incorrect'


@allure.title('Check search goods')
@pytest.mark.regression
def test_search_goods(open_main_page):
    main_page_driver = open_main_page

    with allure.step('Check goods on Computer page'):
        main_page_driver.send_keys_search(keys='Computer')
        search_page = main_page_driver.click_search_button()

        goods = search_page.get_all_product_cards()
        for good in goods:
            title, _ = good
            assert title.lower().__contains__('computer'), 'Goods didn`t find at the page'


@allure.title('Check prices for goods')
@pytest.mark.regression
def test_check_goods_prices(open_main_page):
    main_page_driver = open_main_page

    expected_prices = ['25.00', '1590.00', '800.00', '1200.00', '1800.00', '800.00']

    with allure.step('Check prices for Computer page'):
        goods = main_page_driver.get_all_product_cards()
        actual_prices = []
        for good in goods:
            _, price = good
            actual_prices.append(price)

        pairs = zip(expected_prices, actual_prices)
        for pair in pairs:
            assert float(pair[0]) == float(pair[1]), 'Price is wrong'
