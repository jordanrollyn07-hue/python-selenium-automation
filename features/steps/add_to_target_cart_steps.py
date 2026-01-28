from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium. webdriver.support import expected_conditions as EC

@when('Click on add to cart button')
def click_add_to_cart(context):
    sleep(20)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="shippingButton"]'))).click()


@then('Confirm added to cart message from side navigation')
def added_to_cart_message_from_side_navigation(context):

    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2[data-test="modal-drawer-heading"] span[class="h-text-lg"]')))

    expected_text = 'Added to cart'
    assert f'Expected text to be {expected_text}'
