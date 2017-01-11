# -*- coding: utf-8 -*-
import simplejson as json
import time
import base64
import hashlib
import hmac
import httplib2

class CrossAPI(object):
    # Initialization
    def __init__(self, api_key, secret_key):
        self.url = 'https://apicross.coinone.co.kr'
        self.api_key = api_key
        self.secret_key = secret_key

    # Generate X-CROSS-PAYLOAD
    def get_encoded_payload(self, payload):
        # Add nonce
        payload[u'nonce'] = int(time.time() * 1000)
        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(dumped_json)
        return encoded_json

    # Generate X-CROSS-SIGNATURE
    def get_signature(self, encoded_payload):
        signature = hmac.new(str(self.secret_key).upper(), str(encoded_payload), hashlib.sha512)
        return signature.hexdigest()

    # HTTP Request
    def http_request(self, path, payload):
        encoded_payload = self.get_encoded_payload(payload)
        headers = {
            'Content-Type': 'application/json',
            'X-CROSS-PAYLOAD': encoded_payload,
            'X-CROSS-SIGNATURE': self.get_signature(encoded_payload)
        }
        http = httplib2.Http()
        response, content = http.request(self.url + path,
                                    'POST',
                                    headers=headers,
                                    body=encoded_payload)
        return content

    # Get balace
    def get_balance(self):
        path = '/account/v1/balance/'
        payload = {
            'api_key': self.api_key
        }
        content = self.http_request(path, payload)
        return content

    # Get a list of users using your App
    def get_users(self):
        path = '/account/v1/users/'
        payload = {
            'api_key': self.api_key
        }
        content = self.http_request(path, payload)
        return content

    # Create a user
    def create_user(self, id_number, name, phone_number):
        path = '/account/v1/users/create/'
        payload = {
            'api_key': self.api_key,
            'id_number': id_number,
            'name': name,
            'phone_number': phone_number
        }
        content = self.http_request(path, payload)
        return content

    # Get exchange rates provided by Cross
    def rate_info(self, country):
        path = '/remit/v1/rate_info/'
        payload = {
            'api_key': self.api_key,
            'country': country
        }
        content = self.http_request(path, payload)
        return content

    # Get required fields for remittance
    def required_fields(self, country):
        path = '/remit/v1/required_fields/'
        payload = {
            'api_key': self.api_key,
            'country': country
        }
        content = self.http_request(path, payload)
        return content

    # Get banks
    def banks(self, country):
        path = '/remit/v1/banks/'
        payload = {
            'api_key': self.api_key,
            'country': country
        }
        content = self.http_request(path, payload)
        return content

    # Get bank branches
    def branches(self, country):
        path = '/remit/v1/branches/'
        payload = {
            'api_key': self.api_key,
            'country': country
        }
        content = self.http_request(path, payload)
        return content

    # Get transfer log of all users
    def transfer_log_all(self):
        path = '/remit/v1/transfer_log/all/'
        payload = {
            'api_key': self.api_key,
        }
        content = self.http_request(path, payload)
        return content

    # Get transfer log of a specific user
    def transfer_log(self, user_id):
        path = '/remit/v1/transfer_log/'
        payload = {
            'api_key': self.api_key,
            'user_id': user_id
        }
        content = self.http_request(path, payload)
        return content

    # Request a remittance
    def transfer(self, payload):
        path = '/remit/v1/transfer/'
        payload['api_key'] = self.api_key
        content = self.http_request(path, payload)
        return content
