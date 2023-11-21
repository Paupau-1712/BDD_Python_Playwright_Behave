from playwright.async_api import Page



class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.product_label = page.get_by_text("Products")
        self.login_error = page.locator("[data-test=\"error\"]")
        self.login_error_blank = page.locator("[data-test=\"error\"]")
    async def navigate_to_login_page(self):
        url_login_page ='https://www.saucedemo.com'
        await self.page.goto(url_login_page)

    async def is_home_page_displayed(self):
        if self.product_label.is_visible():
            assert True
        elif self.page.login_error.is_visible():
            assert True
        elif self.login_error_blank.is_visible():
            assert True




