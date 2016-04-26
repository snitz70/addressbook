from addressbook import Addressbook

def before_all(context):
    context.addressbook = Addressbook()