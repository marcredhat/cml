#1) export $CDSW_DOMAIN

#2) create a file named "apikey" with my API v2 key

#3) 
import os
import cmlapi
import cmlapi.configuration
from cmlapi.utils import Cursor
import string
import random
import json

cluster = os.getenv("CDSW_DOMAIN")

config = cmlapi.Configuration()

config.host = "https://" + str(os.getenv('CDSW_DOMAIN'))

config.ssl_ca_cert = "/root/root_ca.crt"

config.verify_ssl = False

with open('apikey', 'r') as file:
    APIKEY = file.read().replace('\n', '')

client = cmlapi.ApiClient(config)

client.set_default_header("authorization", "Bearer "+APIKEY) # This is the new apikey so "Bearer ..."

api = cmlapi.CMLServiceApi(client)
print(api.list_projects())
