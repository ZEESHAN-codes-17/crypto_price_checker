import requests
import tkinter as tk




def crypto():
   crypto_name= crypto_search.get()

   url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto_name}"

   response = requests.get(url)

   data = response.json()

   if response.status_code == 200:
     
      price_label.config(text=f"Current Price: ${data[0]['current_price']:.2f}")
      market_cap_label.config(text=f"Market Cap: ${data[0]['market_cap']:,}")
     
   else:
    print(f"Error: Unable to retrieve data for {crypto_name.capitalize()}. Please check the cryptocurrency name and try again.")    


root = tk.Tk()
root.title("Cryptocurrency Price Checker")
root.geometry("400x200")

crypto_search = tk.Entry(root, width=30)
crypto_search.pack(pady=10)

search_button = tk.Button(root, text="Check Price", command=crypto)
search_button.pack(pady=10)

price_label = tk.Label(root, text="", font=("Arial", 14))
price_label.pack(pady=10)

market_cap_label = tk.Label(root, text="", font=("Arial", 14))
market_cap_label.pack(pady=10)







root.mainloop()




