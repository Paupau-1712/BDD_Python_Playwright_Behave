Feature: Shopping on Sauce Labs

  @Regression @Firsttry
  Scenario: User makes a purchase on the Sauce Labs website
    Given the user is on the Sauce Labs login page
    And the user logs in with valid credentials
    When the user adds the following items to the cart
      | Item Name               |
      | sauce-labs-backpack     |
      | sauce-labs-bike-light   |
    And the user proceeds to checkout and completes the purchase
    Then a thank you message appears on successful purchase