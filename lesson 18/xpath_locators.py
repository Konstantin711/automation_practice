"""
Find web page.
Write 30 XPATH locators for this page using XPath Axes and Wildcards. Some of them should have more than 3 steps.
For 10 XPATH locators write 10 CSS locators which find the same element
"""


url = 'https://refactoring.guru/'

locators_xpath = {
    1: '//button[@class="dropdown-toggle"]',
    2: '//img[@alt="Refactoring.Guru"]/..',
    3: 'html/body/div/div/a',
    4: '//h2[text() = "Refactoring"]',
    5: '//main//div[@class="page text"]/h1',
    6: '//li//a[@title="Contact us"]//i[@aria-hidden]',
    7: '//input[@id="email"]',
    8: '//input[@id="email"]/..//button',
    9: '//input[@id="email"]/..//button/../../../..//h3',
    10: '//div//div[@class="index-grid"]//form',
    11: '//footer//ul//li//a[text()="Home"]',
    12: '//footer//ul//li//a[contains(@href, refa)]',
    13: '//main//div[@class="page text"]//p[contains(text(), "This site shows you the big picture")]',
    14: '//*[contains(@href, "facebook") and contains(@title, "Refactor")]',
    15: '//a[@class="menu-brand"]//img[contains(@src, "logo-new")]',
    16: '//p//b[contains(text(), "Alex")]',
    17: '//*[contains(@id, "solution")]',
    18: '//div[@style="margin-top: 1rem"]',
    19: '//a[starts-with(@href, "/design")]',
    20: '//div[@class="main-menu-aux-controls"]//a[starts-with(@href, "https://refa") and contains(@title, "Log")]',
    21: '//button[@class="dropdown-toggle"]//following::div',
    22: '//img[@alt="Refactoring.Guru"]//ancestor::a',
    23: '//img[@alt="Refactoring.Guru"]//ancestor::a//following::img[contains(@alt, "Refact")]',
    24: '//ul[@class="footer-list"]//child::li',
    25: '//ul[@class="footer-list footer-list-horizontal"]//li//child::a',
    26: '//div[@class="container-fluid container-headline"]//a[@href="/design-patterns"]//preceding::p',
    27: '//ul[@class="footer-list footer-list-horizontal"]//li//following-sibling::li',
    28: '//*[@class="footer-list footer-list-horizontal"]//self::ul',
    29: '//a[starts-with(@class, "btn") and contains(@href, "buy")]',
    30: '//h1[@class="title text-center"]',
    31: '//h1[@class="title text-center"]/..//div//span[contains(text(), "New")]',
    32: '//main/div/article/div/text()',
    33: '//div[@class="screenshot-container"]/child::div',
    34: '//div[@class="screenshot-container"]/following::h2[contains(text(), "Why")]',
    35: '//div[@class="top-product-block product-block"]//div[@class="buy-widget-new"]'
        '//div[@class="buy-widget-new-new-price font-money"]/text()',
    36: '//div[@class="name" and contains(text(), "Peter")]',
    37: '//div[@class="name" and contains(text(), "Peter")]/../..//div//p',
    38: '//div[@class="top-product-block product-block"]//div[@class="image"]//a[@class="do-checkout"]'
        '//img[@src="/images/refactoring/course/course-cover-en.jpg"]',
    39: '//h2[contains(text(), "inside")]',
    40: '//h2[contains(text(), "inside")]/following::p[contains(text(), "course tea")]',
}

css_locators = {
    1: 'button.dropdown-toggle',
    2: 'a.menu-brand',
    3: 'a[href="/store"]',
    4: 'div h2',
    5: 'div.page h1',
    6: 'a.userecho-private i.fa',
    7: '#email',
    8: 'button[type="submit"]',
    9: 'div.index-grid div.email h3',
    10: 'div.index-grid div.email form'
}
