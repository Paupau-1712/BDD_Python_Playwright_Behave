import os

from playwright.async_api import async_playwright
from behave.api.async_step import async_run_until_complete


# from src.test.utilities.file_processor import read_value_from_yaml_file


@async_run_until_complete
async def before_scenario(context, scenario):
    print("Inside before scenario")
    context.p = await async_playwright().start()

    if scenario.tags.__contains__("Firsttry"):
        browser = await context.p.firefox.launch(headless=True, channel="firefox")
        context.page = await browser.new_page()

@async_run_until_complete
async def after_scenario(context, scenario):
    await context.p.stop(scenario)

