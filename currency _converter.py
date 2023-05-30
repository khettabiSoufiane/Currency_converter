# The original version of the code:
#----------------------------------

import requests

# Prompt for the initial currency
initial_currency = input("Insert your initial currency: ")

# Prompt for the currency to target
target_currency = input("Insert your currency to target: ")

while True:
    try:
        # Prompt for the amount to convert
        amount = float(input("Insert your amount: "))
    except:
        print("The amount must be a numeric value!")
        continue

    if amount == 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

# Construct the URL for the API request
url = (
    "https://api.apilayer.com/fixer/convert?to="
    + target_currency
    + "&from="
    + initial_currency
    + "&amount="
    + str(amount)
)

payload = {}
headers = {
    "apikey": "3QNZuSJJdvvhZ0nY30o8tSuilxNnPzGm"
}

# Send a GET request to the API
response = requests.request("GET", url, headers=headers, data=payload)

# Get the status code of the API response
status_code = response.status_code

if status_code != 200:
    print("Sorry, there was a problem. Please try again later.")
    quit()

# Extract the JSON data from the API response
result = response.json()

# Retrieve the converted amount from the result
converted_amount = result["result"]

# Display the conversion result
print(f"{amount} {initial_currency} = {converted_amount} {target_currency}")
