from playwright.async_api import Page

from src.main.apps_classes.study_reference.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.first_name_input = page.locator("[data-test=\"firstName\"]")
        self.last_name_input = page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.thank_you_message = page.get_by_role("heading", name="Thank you for your order!")

    async def click_checkout_button(self):
        await self.checkout_button.click()

    async def enter_first_name(self, first_name: str):
        await self.first_name_input.fill(first_name)

    async def enter_last_name(self, last_name: str):
        await self.last_name_input.fill(last_name)

    async def enter_postal_code(self, postal_code: str):
        await self.postal_code_input.fill(postal_code)

    async def click_continue_button(self):
        await self.continue_button.click()

    async def click_finish_button(self):
        await self.finish_button.click()

    async def verify_thank_you_message(self):
        return await self.thank_you_message.is_visible()

    async def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        await self.enter_first_name(first_name)
        await self.enter_last_name(last_name)
        await self.enter_postal_code(postal_code)
        await self.click_continue_button()
        await self.click_finish_button()