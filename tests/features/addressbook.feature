# Created by Brian Snyder at 4/15/2016
Feature:  Open an Addressbook

  @wip
  Scenario: creating an addressbook that does not exist
    When user creates an addressbook called "testing"
    Then a new addressbook named "testing" should be created

  Scenario: creating an addressbook that already exists
    When user creates an addressbook called "testing"
    And that addressbok already exists in the database
    Then the program returns a warning
    And the addressbook is not created

  Scenario: selecting an aleady existing addressbook
    When the user selects an exiting addressbook
    Then the addressbook should be selected






