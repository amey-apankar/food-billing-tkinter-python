#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",            
    password="password",  
    database="food_world"
)
cursor = db.cursor()


items = {
    "Burger": 50,
    "Pizza": 100,
    "Pasta": 80,
    "Fries": 40,
    "Coke": 20
}

bg_color = "black"
fg_color = "white"
accent_color = "cyan"
secondary_color = "gray20"
highlight_color = "gray30"

font_title = ("Helvetica", 22, "bold")
font_label = ("Helvetica", 13)
font_button = ("Helvetica", 12, "bold")
font_bill = ("Courier", 11)

root = tk.Tk()
root.title("Food World Billing 🍔")
root.geometry("520x700")
root.configure(bg=bg_color)

tk.Label(root, text="Food World Billing", font=font_title, bg=bg_color, fg=accent_color).pack(pady=20)
vars = {}
for item in items:
    vars[item] = tk.IntVar()
    tk.Checkbutton(
        root,
        text=f"{item} — ₹{items[item]}",
        variable=vars[item],
        font=font_label,
        bg=bg_color,
        fg=fg_color,
        activebackground=bg_color,
        activeforeground=accent_color,
        selectcolor=highlight_color,
        pady=5
    ).pack(anchor='w', padx=35)

bill_text = tk.Text(
    root,
    height=17,
    width=52,
    font=font_bill,
    bg=secondary_color,
    fg="light green",
    insertbackground=fg_color,
    borderwidth=0,
    padx=10,
    pady=10
)
bill_text.pack(pady=20)

def generate_bill():
    bill_text.delete('1.0', tk.END)
    total = 0
    bill_text.insert(tk.END, "====== Food World Bill ======\n")
    bill_text.insert(tk.END, "{:<15}{:<10}{:<10}\n".format("Item", "Qty", "Amount"))
    for item, var in vars.items():
        qty = var.get()
        if qty > 0:
            amt = qty * items[item]
            bill_text.insert(tk.END, f"{item:<15}{qty:<10}{amt:<10}\n")
            total += amt
    bill_text.insert(tk.END, "=============================\n")
    bill_text.insert(tk.END, f"Total Bill: ₹{total}\n")
    bill_text.insert(tk.END, "=============================\n")

def save_bill():
    items_list = []
    total = 0

    for item, var in vars.items():
        qty = var.get()
        if qty > 0:
            amt = qty * items[item]
            items_list.append(f"{item} x{qty} = ₹{amt}")
            total += amt

    if not items_list:
        messagebox.showwarning("Empty", "No items selected.")
        return

    items_text = "\n".join(items_list)
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        cursor.execute(
            "INSERT INTO bills (date_time, items, total) VALUES (%s, %s, %s)",
            (date_now, items_text, total)
        )
        db.commit()
        messagebox.showinfo("Saved", "Bill saved to MySQL database.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save bill:\n{e}")


btn_style = {
    "font": font_button,
    "width": 20,
    "bd": 0,
    "pady": 8
}

tk.Button(
    root,
    text="Generate Bill",
    command=generate_bill,
    bg="green",
    fg="white",
    activebackground="light green",
    **btn_style
).pack(pady=5)

tk.Button(
    root,
    text="Save Bill",
    command=save_bill,
    bg="blue",
    fg="white",
    activebackground="sky blue",
    **btn_style
).pack(pady=5)
root.mainloop()

