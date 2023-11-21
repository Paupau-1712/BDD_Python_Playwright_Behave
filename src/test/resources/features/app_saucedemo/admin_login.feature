Feature: Sauce Demo Admin login
  @Firsttry
  Scenario Outline: Admin Login Successful, Unsuccessful (Required fields,Wrong credentials, Locked-out)
    Given user is on the login page
    When the user logs his <username> and <password>
    Then user clicked the login button
    Examples:
      |username|password|
      |standard_user|secret_sauce|
      |standard_user| wrongpassword |
      |wrongusername|secret_sauce|
      |      locked_out_user       |      secret_sauce      |
      |       " "       |secret_sauce|
      |standard_user|      " "      |
      | " "  |      " "      |
