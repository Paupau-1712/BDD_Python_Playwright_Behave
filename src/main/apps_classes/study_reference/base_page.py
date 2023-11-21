from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):

        self.page = page

    async def navigate_to(self, url: str):
        await self.page.goto(url)