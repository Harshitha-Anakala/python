import tkinter as tk
from tkinter import ttk
import requests
import re


class RealTimeCurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # Limit to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class CurrencyConverterUI(tk.Tk):
    def __init__(self, converter):
        super().__init__()
        self.converter = converter
        self.title('Currency Converter')
        self.geometry('500x200')
        self.configure(bg='white')
        self.resizable(width=False, height=False)

        # Fonts
        self.intro_label = tk.Label(
            self, text='Welcome to Real Time Currency Converter',
            fg='blue', relief=tk.RAISED, borderwidth=3
        )
        self.intro_label.config(font=('Arial', 15, 'bold'))
        self.intro_label.place(x=10, y=5)

        self.date_label = tk.Label(
            self,
            text=f"1 Indian Rupee equals = {self.converter.convert('INR', 'USD', 1)} USD\nDate: {self.converter.data['date']}",
            relief=tk.GROOVE, borderwidth=5
        )
        self.date_label.place(x=10, y=50)

        # Amount entry
        self.amount_field = tk.Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER)
        self.amount_field.place(x=30, y=120)

        # From currency dropdown
        self.from_currency_variable = tk.StringVar(self)
        self.from_currency_variable.set('INR')
        self.from_currency_dropdown = ttk.Combobox(
            self, textvariable=self.from_currency_variable, values=list(self.converter.currencies.keys()), state='readonly'
        )
        self.from_currency_dropdown.place(x=150, y=120)

        # To currency dropdown
        self.to_currency_variable = tk.StringVar(self)
        self.to_currency_variable.set('USD')
        self.to_currency_dropdown = ttk.Combobox(
            self, textvariable=self.to_currency_variable, values=list(self.converter.currencies.keys()), state='readonly'
        )
        self.to_currency_dropdown.place(x=300, y=120)

        # Convert button
        self.convert_button = tk.Button(
            self, text='Convert', fg='black', command=self.perform
        )
        self.convert_button.config(font=('Arial', 10, 'bold'))
        self.convert_button.place(x=225, y=150)

        # Result label
        self.converted_amount_label = tk.Label(self, text='', fg='green', relief=tk.FLAT)
        self.converted_amount_label.config(font=('Arial', 12, 'bold'))
        self.converted_amount_label.place(x=200, y=90)

        # Restrict input
        self.amount_field.bind('<KeyRelease>', self.restrictNumberOnly)

    def perform(self):
        try:
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()
            converted_amount = self.converter.convert(from_curr, to_curr, amount)
            self.converted_amount_label.config(
                text=f"{amount} {from_curr} = {converted_amount} {to_curr}"
            )
        except ValueError:
            self.converted_amount_label.config(text="Enter a valid number", fg='red')

    def restrictNumberOnly(self, event):
        value = self.amount_field.get()
        if re.search(r'[^0-9.]', value):
            self.amount_field.delete(len(value)-1, tk.END)


if __name__ == '__main__':
    URL = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(URL)
    CurrencyConverterUI(converter).mainloop()
