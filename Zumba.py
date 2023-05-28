import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#### WISH LIST
# Put the address and pull a photo to the side of the form

TITLE = "Zumba Mortgage Calculator"
FRAME_FONT = ("Arial", 16)
TITLE_FONT = ("Arial", 26, "bold")

class MortgageCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title(TITLE)
        self.window.geometry("700x700")
        self.window.configure(bg="#ECECEC")

        # Title Label
        title_label = ttk.Label(self.window, text=TITLE, font=TITLE_FONT)
        title_label.grid(row=1, column=0, columnspan=2, padx=30, pady=10)

        #label for house price
        house_price_label = ttk.Label(self.window, text="House Price", font=FRAME_FONT)
        house_price_label.grid(row=3, column=0, padx=30, pady=5)

        self.house_price_entry = ttk.Entry(self.window, font=FRAME_FONT)
        self.house_price_entry.grid(row=3, column=1, padx=30, pady=5)

        #downpayment stuff
        downpayment = ttk.Label(self.window, text="Downpayment", font=FRAME_FONT)
        downpayment.grid(row=4, column=0, padx=30, pady=5)

        self.downpayment_entry = ttk.Entry(self.window, font=FRAME_FONT)
        self.downpayment_entry.grid(row=4, column=1, padx=30, pady=5)

        #interest rate
        interest_rate = ttk.Label(self.window, text="Interest Rate %", font=FRAME_FONT)
        interest_rate.grid(row=5, column=0, padx=30, pady=5)

        self.interest_rate_entry = ttk.Entry(self.window, font=FRAME_FONT)
        self.interest_rate_entry.grid(row=5, column=1, padx=30, pady=5)

        #loan life terms
        loan_term = ttk.Label(self.window, text="Loan Term (Years)", font=FRAME_FONT)
        loan_term.grid(row=6, column=0, padx=30, pady=5)

        self.loan_term_entry = ttk.Entry(self.window, font=FRAME_FONT)
        self.loan_term_entry.grid(row=6, column=1, padx=30, pady=5)

        # separator
        separator = ttk.Separator(self.window, orient='horizontal')
        separator.grid(row=7, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

        separator1 = ttk.Separator(self.window, orient='horizontal')
        separator1.grid(row=10, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

        #property taxes
        property_taxes_label = ttk.Label(self.window, text="Property Tax", font=FRAME_FONT)
        property_taxes_label.grid(row=8, column=0, padx=10, pady=0)

        self.property_taxes_entry = ttk.Entry(self.window, font=FRAME_FONT)
        self.property_taxes_entry.grid(row=8, column=1, padx=10, pady=0)

        #house insurance
        house_insurance_label = ttk.Label(self.window, text="House Insurance", font=FRAME_FONT)
        house_insurance_label.grid(row=9, column=0, padx=10, pady=0)

        self.house_insurance_entry = ttk.Entry(self.window, font=FRAME_FONT)
        self.house_insurance_entry.grid(row=9, column=1, padx=10, pady=0)

        #calculate button
        calculate_button = ttk.Button(self.window, text='CALCULATE', command=self.calculate_payment)
        calculate_button.grid(row=15, columnspan=2, padx=10, pady=10)

        #result
        self.mortgage_label = ttk.Label(self.window, text="", font=FRAME_FONT)
        self.mortgage_label.grid(row=12, column=1, padx=30, pady=10)

        #other resuts
        self.taxes_label = ttk.Label(self.window, text="", font=FRAME_FONT)
        self.taxes_label.grid(row=13, column=1, padx=30, pady=10)

        self.total_label = ttk.Label(self.window, text="", font=FRAME_FONT)
        self.total_label.grid(row=14, column=1, padx=30, pady=10)

        # Configure grid to center the form
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(15, weight=1)

    def calculate_payment(self):
        house_price = float(self.house_price_entry.get())
        downpay = float(self.downpayment_entry.get())
        interest_rate = float(self.interest_rate_entry.get()) / 100
        loan_terms = int(self.loan_term_entry.get())
        property_taxes = float(self.property_taxes_entry.get()) / 12
        house_insurance = float(self.house_insurance_entry.get()) / 12

        total_loan = house_price - downpay
        monthly_interest_rate = interest_rate / 12

        loan_term_months = loan_terms * 12

        monthly_payment = (total_loan * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / ((1 + monthly_interest_rate) ** loan_term_months - 1)

        total_taxes = property_taxes + house_insurance

        total = monthly_payment + total_taxes

        self.mortgage_label.config(text=f"The mortgage payment is: $ {monthly_payment:.2f}")
        self.taxes_label.config(text=f"Taxes and insurance is: $ {total_taxes:.2f}")
        self.total_label.config(text=f"Your total estimate monthly payment is: $ {total:.2f}")

def main():
        window = tk.Tk()
        mortgage_calculator = MortgageCalculator(window)
        window.mainloop()

if __name__ == '__main__':
    main()

