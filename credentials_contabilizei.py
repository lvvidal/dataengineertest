# Primeiramente vamos importar as bibliotecas para trabalhar com JSON e HTTP
import json
import requests

# Informação que será usada em cada request
api_url_base = 'https://api-sandbox.contabilizei.com/ds/customers'
# Headers HTTP - caso houvesse um token por exemplo.
headers = {'Content-Type': 'application/json'}

def get_data_json():

    response = requests.get(api_url_base, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None