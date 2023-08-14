from mongoengine import Document, StringField, DateTimeField, BooleanField

class OrdersModel(Document):
    
    order_id = StringField(primary_key=True)
    name = StringField(required=True)
    birthday = DateTimeField(required=True)
    email = StringField(required=True)
    state = StringField(required=True)
    zipcode = StringField(required=True)
    is_valid = BooleanField(default=False)
