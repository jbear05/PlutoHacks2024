# import requests
# import json

# barcode = input("Enter the barcode: ")

# response = requests.get(f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json")

# data = response.json()

# # Extract the materials
# materials = []
# recycling_info = []

# for packaging in data['product']['ecoscore_data']['adjustments']['packaging']['packagings']:
#     score = packaging['ecoscore_material_score']
#     materials.append(f"Ecoscore material score: {score}. This score represents the environmental impact of the material used in the packaging, with a lower score indicating a more environmentally friendly material.")
    
#     recycling = packaging.get('recycling', 'No recycling information available')
#     recycling_info.append(f"Recycling information: {recycling}")

# # Print the materials
# for material in materials:
#     print(material)

# # Print the recycling information
# for recycling in recycling_info:
#     print(recycling)

# api.py
import requests

def fetch_product_data(barcode):
    response = requests.get(f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json")
    data = response.json()
    return data

def extract_and_print_data(data):
    # Extract the materials
    materials = []
    recycling_info = []

    
    for packaging in data['product']['ecoscore_data']['adjustments']['packaging']['packagings']:
        score = packaging['ecoscore_material_score']
        materials.append(f"Ecoscore material score: {score}. This score represents the environmental impact of the material used in the packaging, with a lower score indicating a more environmentally friendly material.")
        
        recycling = packaging.get('recycling', 'No recycling information available')
        recycling_info.append(f"Recycling information: {recycling}")

    return materials, recycling_info
    # # Print the materials
    # for material in materials:
    #     print(material)

    # # Print the recycling information
    # for info in recycling_info:
    #     print(info)