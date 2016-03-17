from contacts import Contact

# todo:  new_address side effects
# todo:  populate Contact.address instead of empty list

def test_new_contact():
    contact = Contact('Brian Snyder')
    assert contact.name == 'Brian Snyder'

def test_add_addresses():
    contact = Contact('Brian Snyder')
    contact.new_address('512 2nd st se dyersville ia 52040')
    assert len(contact.address) == 1
