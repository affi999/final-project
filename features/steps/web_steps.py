# features/steps/web_steps.py
from behave import given, when, then
from selenium import webdriver

# Assuming you have Selenium WebDriver to interact with the browser
context.browser = webdriver.Chrome()

@given('the product data is loaded')
def step_impl(context):
    # This could be a setup step to load product data
    context.browser.get('http://yourapp.com/products')

@when('I read the product')
def step_impl(context):
    # Here, simulate reading a product (could be getting product details)
    context.product = context.browser.find_element_by_id('product_id')

@then('the product details are returned')
def step_impl(context):
    # Check if the product details are displayed correctly
    assert context.product.text == "Expected Product Data"

@when('I create a new product')
def step_impl(context):
    # Simulate filling in the form and submitting for product creation
    context.browser.find_element_by_name('name').send_keys("New Product")
    context.browser.find_element_by_name('category').send_keys("Category 1")
    context.browser.find_element_by_name('price').send_keys("100")
    context.browser.find_element_by_name('availability').click()  # Assuming it's a checkbox or button
    context.browser.find_element_by_name('submit').click()

@then('the product should be added to the system')
def step_impl(context):
    # Verify the product was added successfully, you can check product list or confirmation message
    success_message = context.browser.find_element_by_id('success_message')
    assert "Product created" in success_message.text

# Repeat the process for the other steps like updating, deleting, etc.

