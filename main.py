from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk


a = CurrencyConverter()

currencies = [
    "USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY", "CHF", 
    "NZD", "SEK", "SGD", "HKD", "KRW", "BRL", "ZAR", "RUB", "MXN"
]


window = tk.Tk()
window.geometry("500x400")
window.title("Currency Converter")

def clicked():
    try:
       
        amount = float(e1.get())
        cur1 = currency_from.get()
        cur2 = currency_to.get()
        
        data = a.convert(amount, cur1, cur2)
        
      
        result_label.config(text=f"Converted Amount: {data:.2f}", fg="black")
    except ValueError:
      
        result_label.config(text="Invalid input! Please enter a valid number.", fg="red")
    except Exception as e:
    
        result_label.config(text=f"Error: {e}", fg="red")


l1 = tk.Label(window, text="Currency Converter", font="times 25 bold")
l1.place(x=100, y=30)

l2 = tk.Label(window, text="Enter amount:", font="times 18 bold")
l2.place(x=50, y=80)
e1 = tk.Entry(window)
e1.place(x=250, y=85)

l3 = tk.Label(window, text="From currency:", font="times 18 bold")
l3.place(x=50, y=130)
currency_from = ttk.Combobox(window, values=currencies, state="readonly", font="times 14")
currency_from.place(x=250, y=135)
currency_from.set("USD")  

l4 = tk.Label(window, text="To currency:", font="times 18 bold")
l4.place(x=50, y=180)
currency_to = ttk.Combobox(window, values=currencies, state="readonly", font="times 14")
currency_to.place(x=250, y=185)
currency_to.set("INR")  


b1 = tk.Button(window, text="Convert", command=clicked, font="times 18 bold", bg="green", fg="black")
b1.place(x=200, y=230)


result_label = tk.Label(window, text="", font="times 16 bold")
result_label.place(x=50, y=300)


window.mainloop()
