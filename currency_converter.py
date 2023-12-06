import requests

from_currency = input("enter the initial currency: ")#.upper
to_currency = input("enter the target currency: ")#.upper


while True:
    try:
      amount = float(input("enter the amount: "))
      if amount <= 0 :
        raise ValueError("invalid value!, amount must be > 0 please try again")
      else: break

    except ValueError as err:
       print(err)


url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "BYxSx5ORAl8MEw4UkyTyQPQoN0RT8Mx8"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
convert_result = result['result']
if status_code !=200:
   print("sorry! invalid operation please try again later")
   exit()
else: 
   print(f"{amount} {from_currency} = {convert_result} {to_currency}")


    
