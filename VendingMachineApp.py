import tkinter as tk


def deliver():
    label.config(text="Enter '$2' Below first, Then click the button!")

def new(item):
    money = entry.get()
    if money!='$2':
        if money=="":
            deliver()

        elif money=='2':
            give(item)

        else:
            label.config(text='Invalid Amount!')

    else:
        give(item)

def give(item):
    label.config(text="Your " + item + " is Coming out")
    screen.after(1500, lambda: throw(item))

def throw(item):
    label.config(text="Here's Your " + item + "!")
    label1.config(text=item)
    entry.delete(0, tk.END)

screen = tk.Tk()
screen.geometry('2000x1000')
screen.title("Hiten's Vending Machine")
screen.configure(bg='#ADD8E6')

label = tk.Label(screen, text='Welcome to our vending machine',bg='black',fg='white' ,width=70, height=3, font=('Arial','14', 'bold'))
label.pack(pady=30)

entry = tk.Entry(screen, font=("Arial", 12), relief='flat')
entry.pack(pady=5)

button = tk.Button(screen, text='Burger', command=lambda: new('Burger'), font=('Arial', '10', 'bold'), fg='white', bg='red', highlightthickness=2, relief='flat', width='10')
button.pack(pady=5)

button1 = tk.Button(screen, text='Cold Drink', command=lambda: new('Cold Drink'), font=('Arial', '10', 'bold'), fg='white', bg='red', highlightthickness=2, relief='flat', width='10')
button1.pack(pady=5)

button2 = tk.Button(screen, text='Juice', command=lambda: new('Juice'), font=('Arial', '10', 'bold'), fg='white', bg='red', highlightthickness=2, relief='flat', width='10')
button2.pack(pady=5)

button3 = tk.Button(screen, text='Chips', command=lambda: new('Chips'), font=('Arial', '10', 'bold'), fg='white', bg='red', highlightthickness=2, relief='flat', width='10')
button3.pack(pady=5)

button4 = tk.Button(screen, text='Sandwich', command=lambda: new('Sandwich'), font=('Arial', '10', 'bold'), fg='white', bg='red', highlightthickness=2, relief='flat', width='10')
button4.pack(pady=5)

button5 = tk.Button(screen, text='Croissant', command=lambda: new('Croissant'), font=('Arial', '10', 'bold'), fg='white', bg='red', highlightthickness=2, relief='flat', width='10')
button5.pack(pady=5)

label1 = tk.Label(screen, text='Your Order',bg='black',fg='white' ,width=20, height=2, font=('Arial','10', 'bold'))
label1.pack(pady=30)

label2 = tk.Label(screen, text='Developed by Hiten' ,fg='purple' ,bg='#ADD8E6')
label2.pack(pady=70)

screen.mainloop()