import requests
import json

barcode = input()

response = requests.get(f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def is_recyclable(product_data):
    if 'product' in product_data and 'packaging' in product_data['product']:
        packaging_info = product_data['product']['ecoscore_data']['adjustments']['packaging']
        return packaging_info['packagings']
    #return False

product_data = response.json()
#jprint(response.json())
print(is_recyclable(product_data))
# if is_recyclable(product_data):
#     print("The product is recyclable.")
# else:
#     print("The product is not recyclable.")