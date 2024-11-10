# features/products.feature
Feature: Product management

  Scenario: Reading a product
    Given the product data is loaded
    When I read the product
    Then the product details are returned

  Scenario: Creating a product
    Given the product data is not yet in the system
    When I create a new product
    Then the product should be added to the system

  Scenario: Updating a product
    Given the product data exists in the system
    When I update the product
    Then the product data should be updated

  Scenario: Deleting a product
    Given the product data exists in the system
    When I delete the product
    Then the product should be removed from the system

  Scenario: Listing all products
    Given multiple products are available
    When I list all products
    Then a list of products should be returned

  Scenario: Finding a product by name
    Given products are available in the system
    When I search for a product by name
    Then the product matching the name should be returned

  Scenario: Finding a product by category
    Given products are available in the system
    When I search for products by category
    Then the products in the specified category should be returned

  Scenario: Finding products by availability
    Given products are available in the system
    When I search for products by availability
    Then the products matching the availability status should be returned
