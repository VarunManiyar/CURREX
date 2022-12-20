import tkinter as tk
from tkinter import *
import tkinter.messagebox
from forex_python.converter import CurrencyRates

def Conversion():
	c = CurrencyRates()

	from_currency = fr.get()
	to_currency = to.get()

	if (Entry1_field.get() == ""):
		tkinter.messagebox.showinfo("Invalid", "Enter Amount")

	elif (from_currency == "Select" or to_currency == "Select"):
		tkinter.messagebox.showinfo("Invalid","Select Type")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Entry1_field.get()))
		new_amount = float((new_amt))
		Entry2_field.insert(0, str(new_amount))

def clear_all():
	Entry1_field.delete(0, tk.END)
	Entry2_field.delete(0, tk.END)

win = tk.Tk()
win.title("Currency converter")

fr = tk.StringVar(win)
to = tk.StringVar(win)

fr.set("Select")
to.set("Select")

CurrenyCode_list = ["USD", "INR", "CAD", "CNY", "JPY","EUR","GBP","HKD","KRW","SGD"]

win.configure(background='#e6e5e5')
win.geometry("550x400")

bg =tk.PhotoImage(file = "C:\\Users\\Admin\\OneDrive\\Documents\\VSCode\\Python\\currency convertor\\background (1).png")

label_1 = Label( win, image = bg)
label_1.place(x = 0, y = 0,)

headlabel = tk.Label(win, font=('lato black', 19, 'bold'), text='Currency Convertor')
headlabel.place(x=150,y=20)

label1 = tk.Label(win, font=('arial', 15, 'bold'), text="Amount : ")
label1.place(x=100,y=60)

label2 = tk.Label(win, font=('arial', 15, 'bold'), text="From Currency : ")
label2.place(x=100,y=90)

label3 = tk.Label(win, font=('arial', 15, 'bold'), text="To Currency : ")
label3.place(x=100,y=120)

label4 = tk.Label(win, font=('arial', 15, 'bold'), text="Converted Amount : ")
label4.place(x=100,y=220)

Button1 = Button(win, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="lightgreen", fg="white",command=Conversion)
Button1.place(x=210,y=160)

Button2 = Button(win, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="orange", fg="white",
				command=clear_all)
Button2.place(x=210,y=270)

FromCurrency_option = tk.OptionMenu(win, fr, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(win, to, *CurrenyCode_list)

FromCurrency_option.place(x=280,y=90)
ToCurrency_option.place(x=280,y=120)

Entry1_field = tk.Entry(win,width=30)
Entry1_field.place(x=205,y=65,width=50)

Entry2_field = tk.Entry(win)
Entry2_field.place(x=310,y=225)

win.mainloop()