# cross-api-python
Cross Remittance API implemented by using python

Documentation at:

http://apicross.coinone.co.kr/doc/

### Example:

```python
from cross_api import CrossAPI
import simplejson as json

API_KEY = 'Your API Key'
SECRET_KEY = 'Your Secret Key'

api = CrossAPI(api_key=API_KEY, secret_key=SECRET_KEY)

# Get your balance
result = json.loads(api.get_balance())
```

https://github.com/cross-remittance/cross-api-python
