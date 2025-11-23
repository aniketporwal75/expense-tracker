# Expense Tracker

A simple and user-friendly command-line Expense Tracker built using Python.  
This project allows users to record daily expenses, view summaries, and store all data persistently in a JSON file.

---

## Features

- **Add new expenses** with date, category, amount, and description  
- **View all recorded expenses** in a clean list  
- **Summary by category** (food, travel, shopping, etc.)  
- **Summary by date**  
- **Automatic data saving** to `expenses.json`  
- **Input validation** for dates and amounts  
- Fully **offline**, lightweight, and easy to use  

---

## Project Structure

~~~text
expense-tracker/
│
├── expenses.json        # Automatically created file to store expense records
├── expense_tracker.py   # Main Python program
└── README.md            # Documentation
~~~

---

## How It Works

### 1. **Load Expenses**
At startup, the program loads existing data from `expenses.json`.  
If the file doesn’t exist, it starts with an empty list.

### 2. **Main Menu Options**
~~~text
1. Add Expense
2. View All Expenses
3. View Summary by Category
4. View Summary by Date
5. Exit
~~~

### 3. **Adding an Expense**
Users enter:
- Date (auto-fills today's date if blank)
- Category
- Amount (validated)
- Optional description  

The entry is saved immediately.

### 4. **Viewing & Summaries**
- View all expenses with total amount  
- View total spending per **category**  
- View total spending per **date**

---

## Sample Expense Entry

~~~json
{
  "date": "2025-01-23",
  "category": "food",
  "amount": 150.0,
  "description": "Pizza"
}
~~~

---

## How to Run

### **Step 1: Clone the repository**
~~~bash
git clone https://github.com/your-username/expense-tracker.git
~~~

### **Step 2: Navigate to the project folder**
~~~bash
cd expense-tracker
~~~

### **Step 3: Run the program**
~~~bash
python expense_tracker.py
~~~

---

## Requirements

- Python 3.x  
- No external libraries required  

---

## 📄 License
This project is open-source and free to use under the MIT License.
