# tests/test_models.py
def test_read_product():
    product = Product.objects.create(name="Product1", category="Category1", availability=True)
    assert product.name == "Product1"

# tests/test_models.py
def test_update_product():
    product = Product.objects.create(name="Product1", category="Category1", availability=True)
    product.name = "Updated Product"
    product.save()
    updated_product = Product.objects.get(id=product.id)
    assert updated_product.name == "Updated Product"
# tests/test_models.py
def test_delete_product():
    product = Product.objects.create(name="Product1", category="Category1", availability=True)
    product_id = product.id
    product.delete()
    try:
        deleted_product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        deleted_product = None
    assert deleted_product is None
# tests/test_models.py
def test_list_all_products():
    Product.objects.create(name="Product1", category="Category1", availability=True)
    Product.objects.create(name="Product2", category="Category2", availability=False)
    products = Product.objects.all()
    assert len(products) == 2
# tests/test_models.py
def test_find_product_by_name():
    Product.objects.create(name="Product1", category="Category1", availability=True)
    product = Product.objects.filter(name="Product1").first()
    assert product is not None
    assert product.name == "Product1"
# tests/test_models.py
def test_find_product_by_category():
    Product.objects.create(name="Product1", category="Category1", availability=True)
    product = Product.objects.filter(category="Category1").first()
    assert product is not None
    assert product.category == "Category1"
# tests/test_models.py
def test_find_product_by_availability():
    Product.objects.create(name="Product1", category="Category1", availability=True)
    Product.objects.create(name="Product2", category="Category2", availability=False)
    available_products = Product.objects.filter(availability=True)
    assert len(available_products) == 1
    assert available_products[0].name == "Product1"
