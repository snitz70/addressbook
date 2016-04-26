from behave import given, when, then
#import addressbook
import mock

@when('user creates an addressbook called "{addressbook_name}"')
def create_addressbook(context, addressbook_name):
    context.addressbook.name = addressbook_name

@then('a new addressbook named "{addressbook_name}" should be created')
def check_if_new_addressbook_created(context, addressbook_name):
    assert context.addressbook.name == addressbook_name















