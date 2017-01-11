# -*- coding: utf-8 -*-
from cross_api import CrossAPI
import simplejson as json

API_KEY = 'Your API Key'
SECRET_KEY = 'your Secret Key'

api = CrossAPI(api_key=API_KEY, secret_key=SECRET_KEY)

# Get your balance
print api.get_balance()

# Get your app's users
print api.get_users()

# Create your app's user
result = api.create_user(id_number='9012311234567',
                        name=u"홍길동",
                        phone_number='01012345678')
print result

# Get cross service rate for China
print api.rate_info(country='cny')

# Get required fields of Japan to know what parameter is required to transfer money
print api.required_fields(country='jpy')

# Get a list of banks from Philippines
print api.banks(country='php')

# Get a list of bank branches from Japan
print api.branches(country='jpy')

# Get transfer log of your users
print api.transfer_log_all()

# Get transfer log of a user
print api.transfer_log(user_id=1)

# Request of remittance to China
payload = {
    'user_id': 1,
    'recipient_name': u"張偉",
    'country': 'cny',
    'send_amount': 3000000,
    'bank_id': 1,
    'bank_account': '1234567890',
}
print api.transfer(payload)
