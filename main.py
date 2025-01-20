# Calculator
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")

entry = tk.Entry(root, font=15)
entry.grid(row=0, column=0, columnspan=4)

# Number field -----------------------------------------------------------
num_pad_x = 2
num_pad_y = 10
num_font_def = 10

sym_pad_y = 10
# Row 1 Numbers ----------------------------------------------------------
bt_1 = tk.Button(root, font=num_font_def, text="1")
bt_1.grid(row=1, column=0, pady=num_pad_y, padx=num_pad_x)

bt_2 = tk.Button(root, font=num_font_def, text="2")
bt_2.grid(row=1, column=1, pady=num_pad_y, padx=num_pad_x)

bt_3 = tk.Button(root, font=num_font_def, text="3")
bt_3.grid(row=1, column=2, pady=num_pad_y, padx=num_pad_x)
# Row 2 Numbers ----------------------------------------------------------
bt_4 = tk.Button(root, font=num_font_def, text="4")
bt_4.grid(row=2, column=0, pady=num_pad_y, padx=num_pad_x)

bt_5 = tk.Button(root, font=num_font_def, text="5")
bt_5.grid(row=2, column=1, pady=num_pad_y, padx=num_pad_x)

bt_6 = tk.Button(root, font=num_font_def, text="6")
bt_6.grid(row=2, column=2, pady=num_pad_y, padx=num_pad_x)
# Row 3 Numbers ----------------------------------------------------------
bt_7 = tk.Button(root, font=num_font_def, text="7")
bt_7.grid(row=3, column=0, pady=num_pad_y, padx=num_pad_x)

bt_8 = tk.Button(root, font=num_font_def, text="8")
bt_8.grid(row=3, column=1, pady=num_pad_y, padx=num_pad_x)

bt_9 = tk.Button(root, font=num_font_def, text="9")
bt_9.grid(row=3, column=2, pady=num_pad_y, padx=num_pad_x)
# Row 4 Numbers ----------------------------------------------------------
bt_0 = tk.Button(root, font=num_font_def, text="0")
bt_0.grid(row=4, column=0, pady=num_pad_y, padx=num_pad_x)

bt_p = tk.Button(root, font=num_font_def, text=".")
bt_p.grid(row=4, column=1, pady=num_pad_y, padx=num_pad_x)


# Row 1 Symbols ----------------------------------------------------------
bt_plus = tk.Button(root, font=num_font_def, text="+")
bt_plus.grid(row=1, column=3, pady=num_pad_y, padx=num_pad_x)

# Row 2 Symbols ----------------------------------------------------------
bt_minus = tk.Button(root, font=num_font_def, text="-")
bt_minus.grid(row=2, column=3, pady=num_pad_y, padx=num_pad_x)

# Row 3 Symbols ----------------------------------------------------------
bt_mult = tk.Button(root, font=num_font_def, text="*")
bt_mult.grid(row=3, column=3, pady=num_pad_y, padx=num_pad_x)

# Row 4 Symbols ----------------------------------------------------------
bt_div = tk.Button(root, font=num_font_def, text="/")
bt_div.grid(row=4, column=3, pady=num_pad_y, padx=num_pad_x)

root.mainloop()
