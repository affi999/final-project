# features/steps/load_steps.py
@given('the product data is loaded')
def step_impl(context):
    context.product = create_fake_product()

