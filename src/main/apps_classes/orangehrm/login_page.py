from playwright.async_api import Page

from src.main.apps_classes.saucedemov2.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    async def enter_username(self, username: any):
        await self.username_input.fill(username)

    async def enter_password(self, password: any):
        await self.password_input.fill(password)

    async def click_login_button(self):
        await self.login_button.click()
        await self.navigate_to_login_page()

    async def login_into_saucelabs(self, username: str, password: str):
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login_button()


