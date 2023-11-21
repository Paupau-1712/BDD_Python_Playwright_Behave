from playwright.async_api import Page

from src.main.apps_classes.study_reference.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_button = page.locator("#shopping_cart_container a")

    async def select_item(self, item_name: str):
        await self.page.locator(f"[data-test=\"add-to-cart-{item_name}\"]").click()

    async def click_cart_button(self):
        await self.cart_button.click()

    async def is_home_page_displayed(self):
        return await self.page.get_by_text("Swag Labs").is_visible()