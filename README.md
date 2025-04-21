# Vending Machine Application README 🥤🍔

## 🌟 Overview
This is a Python-based vending machine application built using the Tkinter library. It features an interactive graphical interface where users can select items, input the required amount ("$2"), and enjoy their virtual snacks! 🍟🥪

## ✨ Features
- **🎨 User-Friendly Interface**: Clean and intuitive design.
- **🖱️ Interactive Buttons**:
  - Choose from multiple items: **Burger**, **Cold Drink**, **Juice**, **Chips**, **Sandwich**, and **Croissant**.
- **✅ Input Validation**: Ensures the user enters the correct amount.
- **⏳ Animated Order Processing**: Adds a short delay for a realistic vending machine experience.
- **📱 Customizable Design**: Easy to tweak items, prices, and interface elements.

## 🛠️ How It Works
1. **Launch the App** 🖥️:
   - You'll see a welcome message, input field for the amount, and buttons for item selection.
2. **Enter Amount** 💲:
   - Type **"$2"** in the input field.
   - If the field is blank or contains an invalid input, the app will prompt you with appropriate messages.
3. **Choose an Item** 🍴:
   - Click on your desired item button.
4. **Processing Your Order** ⏳:
   - The app simulates the preparation of your order.
5. **Order Delivered** 🎉:
   - After a moment, you’ll see a message confirming your snack is ready!

## 🔧 Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Tkinter Library**: It’s usually included with Python. If not, you can install it using:
  ```bash
  sudo apt-get install python3-tk  # For Linux
  ```

## 🚀 How to Run
1. Save the code in a file named `vending_machine.py`.
2. Run the script in your Python environment:
   ```bash
   python vending_machine.py
   ```

## 🛠️ Customization Options
- **Items and Prices**: Modify the buttons’ `command` parameters to update items or change pricing logic.
- **Look and Feel**: Adjust colors, fonts, and layouts in the Tkinter widgets like `Label`, `Entry`, and `Button`.

## 🔎 Code Highlights
- **Key Functions**:
  - `deliver()`: Provides instructions to the user.
  - `new(item)`: Validates the input and handles the logic for order placement.
  - `give(item)`: Initiates the order preparation process.
  - `throw(item)`: Delivers the final confirmation and resets the input field.
- **Widgets**:
  - **Labels**: Display messages to guide users.
  - **Entry Field**: Accepts user input (amount).
  - **Buttons**: Let users select items.

## 👨‍💻 Developer
Developed by **Hiten** 💻 to showcase the power of Tkinter and Python!

---
