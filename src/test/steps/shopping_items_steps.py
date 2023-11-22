from behave import given, when, then
from behave.api.async_step import async_run_until_complete

from src.main.apps_classes.study_reference.checkout_page import CheckoutPage
from src.main.apps_classes.study_reference.home_page import HomePage
from src.main.apps_classes.study_reference.login_page import LoginPage


@given(u'the user is on the Sauce Labs login page')
@async_run_until_complete
async def step_user_on_login_page(context):
    context.login_page = LoginPage(context.page)
    await context.login_page.navigate_to('https://www.saucedemo.com')


@given(u'the user logs in with valid credentials')
@async_run_until_complete
async def step_user_logs_in(context):
    await context.login_page.login_into_saucelabs('standard_user','secret_sauce')
    await context.page.wait_for_timeout(2000)


@when(u'the user adds the following items to the cart')
@async_run_until_complete
async def step_user_adds_items_to_cart(context):
    context.home_page = HomePage(context.page)

    assert await context.home_page.is_home_page_displayed() is True
    for row in context.table:
        item_name = row["Item Name"]
        await context.home_page.select_item(item_name)

    await context.page.wait_for_timeout(2000)

    await context.home_page.click_cart_button()


@when(u'the user proceeds to checkout and completes the purchase')
@async_run_until_complete
async def step_user_checkout_and_complete_purchase(context):
    context.checkout_page = CheckoutPage(context.page)
    await context.checkout_page.click_checkout_button()
    await context.page.wait_for_timeout(2000)
    await context.checkout_page.fill_checkout_information("Aman", "Sharma", "8888")
    await context.page.wait_for_timeout(2000)


@then(u'a thank you message appears on successful purchase')
@async_run_until_complete
async def step_thank_you_message_appears(context):
    assert await context.checkout_page.verify_thank_you_message() is True