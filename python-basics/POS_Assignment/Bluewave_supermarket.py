# Name : Ronnie Muturi
# Date : 24/02/2026
# program to make a supermarket pos

import tkinter as tk
from tkinter import messagebox

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("BlueWave Supermarket POS")
root.geometry("480x620")
root.resizable(False, False)
root.configure(bg="#eaeaea")

items = []
item_details = []

# ---------------- FUNCTIONS ----------------
def add_item():
    name = item_name.get()
    price = item_price.get()

    if name == "" or price == "":
        messagebox.showerror("Error", "Enter item name and price")
        return

    try:
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Price must be a number")
        return

    items.append(price)
    item_details.append(f"{name} - Ksh {price:.2f}")
    listbox.insert(tk.END, f"{name} - Ksh {price:.2f}")

    item_name.set("")
    item_price.set("")
    update_total()

def update_total():
    total = sum(items)
    total_label.config(text=f"Total: Ksh {total:.2f}")

def calculate_balance():
    try:
        cash = float(cash_paid.get())
        total = sum(items)
        if cash < total:
            messagebox.showerror("Error", "Cash paid is less than total")
            return
        balance = cash - total
        balance_label.config(text=f"Balance: Ksh {balance:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid cash amount")

def clear_all():
    items.clear()
    item_details.clear()
    listbox.delete(0, tk.END)
    total_label.config(text="Total: Ksh 0.00")
    balance_label.config(text="Balance: Ksh 0.00")
    cash_paid.set("")

def show_receipt():
    if not items:
        messagebox.showwarning("No Items", "No items to print receipt")
        return

    receipt = tk.Toplevel(root)
    receipt.title("Receipt")
    receipt.geometry("320x450")
    receipt.configure(bg="white")

    tk.Label(receipt, text="BLUEWAVE SUPERMARKET",
             font=("Arial", 14, "bold"), bg="white").pack(pady=5)

    text = tk.Text(receipt, width=38, height=20, bd=0)
    text.pack()

    text.insert(tk.END, "Items Purchased:\n\n")
    for item in item_details:
        text.insert(tk.END, item + "\n")

    total = sum(items)
    cash = float(cash_paid.get()) if cash_paid.get() else 0
    balance = cash - total

    text.insert(tk.END, "\n-------------------------\n")
    text.insert(tk.END, f"Total:   Ksh {total:.2f}\n")
    text.insert(tk.END, f"Cash:    Ksh {cash:.2f}\n")
    text.insert(tk.END, f"Balance: Ksh {balance:.2f}\n")
    text.insert(tk.END, "\nThank you for shopping with us!\n")

    text.config(state="disabled")

# ---------------- VARIABLES ----------------
item_name = tk.StringVar()
item_price = tk.StringVar()
cash_paid = tk.StringVar()

# ---------------- HEADER ----------------
header = tk.Frame(root, bg="#1976D2", height=80)
header.pack(fill="x")

tk.Label(header, text="BLUEWAVE SUPERMARKET",
         font=("Arial", 20, "bold"), fg="white", bg="#1976D2").pack(pady=20)

# ---------------- BODY ----------------
body = tk.Frame(root, bg="#eaeaea")
body.pack(pady=10)

tk.Label(body, text="Item Name", bg="#eaeaea").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(body, textvariable=item_name).grid(row=0, column=1)

tk.Label(body, text="Price (Ksh)", bg="#eaeaea").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(body, textvariable=item_price).grid(row=1, column=1)

tk.Button(root, text="Add Item", width=25,
          bg="#4CAF50", fg="white",
          command=add_item).pack(pady=8)

listbox = tk.Listbox(root, width=42, height=8)
listbox.pack(pady=10)

total_label = tk.Label(root, text="Total: Ksh 0.00",
                       font=("Arial", 14, "bold"), bg="#eaeaea")
total_label.pack()

# ---------------- PAYMENT ----------------
payment = tk.Frame(root, bg="#eaeaea")
payment.pack(pady=10)

tk.Label(payment, text="Cash Paid (Ksh)", bg="#eaeaea").grid(row=0, column=0, padx=5)
tk.Entry(payment, textvariable=cash_paid).grid(row=0, column=1)

tk.Button(root, text="Calculate Balance", width=25,
          bg="#FF9800", fg="white",
          command=calculate_balance).pack(pady=8)

balance_label = tk.Label(root, text="Balance: Ksh 0.00",
                         font=("Arial", 14, "bold"), bg="#eaeaea")
balance_label.pack()

# ---------------- ACTION BUTTONS ----------------
tk.Button(root, text="Print Receipt", width=25,
          bg="#2196F3", fg="white",
          command=show_receipt).pack(pady=5)

tk.Button(root, text="Clear Sale", width=25,
          bg="#F44336", fg="white",
          command=clear_all).pack(pady=5)

root.mainloop()