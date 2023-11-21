from playwright.async_api import Page
from src.main.apps_classes.study_reference.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.login_error = page.locator("[data-test=\"error\"]")

    async def enter_username(self, username: str):
        await self.username_input.fill(username)

    async def enter_password(self, password: str):
        await self.password_input.fill(password)

    async def click_login_button(self):
        await self.login_button.click()

    async def login_into_saucelabs(self, username: str, password: str):
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login_button()

    async def is_home_page_displayed(self):
        return await self.page.get_by_text("Swag Labs").is_visible()

