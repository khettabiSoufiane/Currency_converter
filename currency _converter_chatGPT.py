# the refactored version of the code:
#-----------------------------------

import requests

# Prompt for the initial currency
initial_currency = input("Insert your initial currency: ")

# Prompt for the currency to target
target_currency = input("Insert your currency to target: ")

while True:
    try:
        # Prompt for the amount to convert
        amount = float(input("Insert your amount: "))
        
        if amount <= 0:
            print("The amount must be greater than 0")
            continue
        else:
            break
    except ValueError:
        print("The amount must be a numeric value!")

# Construct the URL for the API request
url = f"https://api.exchangerate-api.com/v4/latest/{initial_currency}"

# Send a GET request to the API
response = requests.get(url)

# Check if the API request was successful
if response.status_code != 200:
    print("Sorry, there was a problem. Please try again later.")
    quit()

# Extract the JSON data from the API response
data = response.json()

# Get the conversion rate for the target currency
conversion_rate = data["rates"][target_currency]

# Calculate the converted amount
converted_amount = amount * conversion_rate

# Display the conversion result
print(f"{amount} {initial_currency} = {converted_amount} {target_currency}")
