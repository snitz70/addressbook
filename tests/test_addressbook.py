import addressbook
import mock



def test_can_create_addressbook():
    addr = addressbook.Addressbook()
    addr.name = 'testing'
    assert addr.name == 'testing'






