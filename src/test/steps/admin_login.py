from behave import *
from behave.api.async_step import async_run_until_complete
from src.main.apps_classes.saucedemov2.login_page import LoginPage



@given(u'user is on the login page')
@async_run_until_complete
async def step_user_on_login_page(context):
    context.login_page = LoginPage(context.page)
    await context.login_page.navigate_to_login_page()


@when(u'the user logs his {username} and {password}')
@async_run_until_complete
async def step_user_input_creds(context, username, password):
    await context.login_page.login_into_saucelabs(username,password)


@then(u'user clicked the login button')
@async_run_until_complete
async def step_open_page(context):
    await context.login_page.is_home_page_displayed()



