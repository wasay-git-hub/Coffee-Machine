# ☕ Coffee Machine Project

This is a simple console-based coffee machine simulation written in Python. The program allows users to select from three types of coffee (Espresso, Latte, Cappuccino), checks available resources, processes payment, gives change, and keeps track of inventory and total earnings.

## 🚀 Features

- Three drink options: Espresso, Latte, and Cappuccino
- Ingredient/resource management
- Coin-based payment system
- Change calculation
- Inventory report command
- Shut down (`off`) command

## 🧾 Menu

| Drink      | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
|------------|------------|-----------|------------|----------|
| Espresso   | 50         | 0         | 18         | 1.5      |
| Latte      | 200        | 150       | 24         | 2.5      |
| Cappuccino | 250        | 100       | 24         | 3.0      |

## 🛠 How It Works

1. **Prompt:** The user is asked to choose a drink or enter a command (`report`, `off`).
2. **Resource Check:** The machine checks if enough ingredients are available.
3. **Coin Insert:** The user inputs how much money they're inserting.
4. **Payment Verification:** If enough money is inserted, the drink is made, and change is returned if needed.
5. **Inventory Update:** Ingredients are reduced based on the drink made, and money is tracked.
6. **Report Command:** Typing `report` prints the current resource levels and earnings.
7. **Shutdown:** Typing `off` stops the program.

## 💻 How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or download the code file.
