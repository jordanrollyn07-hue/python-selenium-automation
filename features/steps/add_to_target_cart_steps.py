from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on add to cart button')
def click_add_to_cart(context):
    sleep(20)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="shippingButton"]').click()

@then('Confirm added to cart message from side navigation')
def side_nav_added_to_cart(context):
    sleep(5)
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h2[data-test="modal-drawer-heading"] span[class="h-text-lg"]').text
    assert expected_text == actual_text, f'Expected text {expected_text} not in {actual_text}'