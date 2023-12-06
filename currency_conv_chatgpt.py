import requests

def get_currency_conversion():
    from_currency, to_currency = input("Enter initial currency: ").upper(), input("Enter target currency: ").upper()

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0: raise ValueError("Invalid value! Amount must be greater than 0. Please try again.")
            break
        except ValueError as err: print(err)

    url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": "BYxSx5ORAl8MEw4UkyTyQPQoN0RT8Mx8"}
    response = requests.get(url, headers=headers)

    status_code, result = response.status_code, response.json()

    if status_code != 200 or not result.get("success", False):
        print("Sorry! Invalid operation. Please try again later.")
        if "error" in result: print(f"Error details: {result['error']}")
    else: print(f"{amount} {from_currency} = {result['result']} {to_currency}")

if __name__ == "__main__": get_currency_conversion()