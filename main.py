# Calculator
import tkinter as tk
from tkinter import ttk


def input_calculator_1():
    pos = len(entry.get())
    entry.insert(pos, "1")

def input_calculator_2():
    pos = len(entry.get())
    entry.insert(pos, "2")

def input_calculator_3():
    pos = len(entry.get())
    entry.insert(pos, "3")

def input_calculator_4():
    pos = len(entry.get())
    entry.insert(pos, "4")

def input_calculator_5():
    pos = len(entry.get())
    entry.insert(pos, "5")

def input_calculator_6():
    pos = len(entry.get())
    entry.insert(pos, "6")

def input_calculator_7():
    pos = len(entry.get())
    entry.insert(pos, "7")

def input_calculator_8():
    pos = len(entry.get())
    entry.insert(pos, "8")

def input_calculator_9():
    pos = len(entry.get())
    entry.insert(pos, "9")

def input_calculator_0():
    pos = len(entry.get())
    entry.insert(pos, "0")

def input_calculator_p():
    pos = len(entry.get())
    entry.insert(pos, ".")

def input_calculator_plus():
    pos = len(entry.get())
    entry.insert(pos, "+")

def input_calculator_minus():
    pos = len(entry.get())
    entry.insert(pos, "-")

def input_calculator_mult():
    pos = len(entry.get())
    entry.insert(pos, "*")

def input_calculator_div():
    pos = len(entry.get())
    entry.insert(pos, "/")

def input_calculator_percent():
    pos = len(entry.get())
    entry.insert(pos, "%")

def input_calculator_par_open():
    pos = len(entry.get())
    entry.insert(pos, "(")

def input_calculator_par_close():
    pos = len(entry.get())
    entry.insert(pos, ")")

def clear():
    end = len(entry.get())
    entry.delete(0, end)

def calculate():
    calc = entry.get()
    calc_list = list(calc)
    calc_list_len = len(calc_list)

    for i in range(calc_list_len):
        if calc_list[i] == "%":
            calc_list[i] = "*1/100"
        # print(calc)
    calc = ''.join(calc_list)
    result = eval(calc)

    end = len(entry.get())
    entry.delete(0, end)
    entry.insert(0, result)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x300")
    root.resizable(False, False)

    entry = ttk.Entry(root, font=15)
    entry.grid(row=0, column=0, columnspan=4)

    # Number field -----------------------------------------------------------
    num_pad_x = 2
    num_pad_y = 5

    sym_pad_y = 10
    # Row 1 Numbers ----------------------------------------------------------
    bt_1 = ttk.Button(root, text="1", command=input_calculator_1)
    bt_1.grid(row=1, column=0, pady=num_pad_y, padx=num_pad_x)

    bt_2 = ttk.Button(root, text="2", command=input_calculator_2)
    bt_2.grid(row=1, column=1, pady=num_pad_y, padx=num_pad_x)

    bt_3 = ttk.Button(root, text="3", command=input_calculator_3)
    bt_3.grid(row=1, column=2, pady=num_pad_y, padx=num_pad_x)
    # Row 2 Numbers ----------------------------------------------------------
    bt_4 = ttk.Button(root, text="4", command=input_calculator_4)
    bt_4.grid(row=2, column=0, pady=num_pad_y, padx=num_pad_x)

    bt_5 = ttk.Button(root, text="5", command=input_calculator_5)
    bt_5.grid(row=2, column=1, pady=num_pad_y, padx=num_pad_x)

    bt_6 = ttk.Button(root, text="6", command=input_calculator_6)
    bt_6.grid(row=2, column=2, pady=num_pad_y, padx=num_pad_x)
    # Row 3 Numbers ----------------------------------------------------------
    bt_7 = ttk.Button(root, text="7", command=input_calculator_7)
    bt_7.grid(row=3, column=0, pady=num_pad_y, padx=num_pad_x)

    bt_8 = ttk.Button(root, text="8", command=input_calculator_8)
    bt_8.grid(row=3, column=1, pady=num_pad_y, padx=num_pad_x)

    bt_9 = ttk.Button(root, text="9", command=input_calculator_9)
    bt_9.grid(row=3, column=2, pady=num_pad_y, padx=num_pad_x)
    # Row 4 Numbers ----------------------------------------------------------
    bt_0 = ttk.Button(root, text="0", command=input_calculator_0)
    bt_0.grid(row=4, column=0, pady=num_pad_y, padx=num_pad_x)

    bt_p = ttk.Button(root, text=".", command=input_calculator_p)
    bt_p.grid(row=4, column=1, pady=num_pad_y, padx=num_pad_x)

    bt_e = ttk.Button(root, text="=", command=calculate)
    bt_e.grid(row=4, column=2, pady=num_pad_y, padx=num_pad_x)


    # Row 1 Symbols ----------------------------------------------------------
    bt_plus = ttk.Button(root, text="+", command=input_calculator_plus)
    bt_plus.grid(row=1, column=3, pady=num_pad_y, padx=num_pad_x)

    bt_percent = ttk.Button(root, text="%", command=input_calculator_percent)
    bt_percent.grid(row=1, column=4, pady=num_pad_y, padx=num_pad_x)

    # Row 2 Symbols ----------------------------------------------------------
    bt_minus = ttk.Button(root, text="-", command=input_calculator_minus)
    bt_minus.grid(row=2, column=3, pady=num_pad_y, padx=num_pad_x)

    bt_par_open = ttk.Button(root, text="(", command=input_calculator_par_open)
    bt_par_open.grid(row=2, column=4, pady=num_pad_y, padx=num_pad_x)

    # Row 3 Symbols ----------------------------------------------------------
    bt_mult = ttk.Button(root, text="*", command=input_calculator_mult)
    bt_mult.grid(row=3, column=3, pady=num_pad_y, padx=num_pad_x)

    bt_par_close = ttk.Button(root, text=")", command=input_calculator_par_close)
    bt_par_close.grid(row=3, column=4, pady=num_pad_y, padx=num_pad_x)

    # Row 4 Symbols ----------------------------------------------------------
    bt_div = ttk.Button(root, text="/", command=input_calculator_div)
    bt_div.grid(row=4, column=3, pady=num_pad_y, padx=num_pad_x)

    bt_clear = ttk.Button(root, text="C", command=clear)
    bt_clear.grid(row=4, column=4, pady=num_pad_y, padx=num_pad_x)

    root.mainloop()
