# Calculator using Tkinter 🧮

## 📌 About
A simple and functional **Desktop Calculator** built using Python's built-in **Tkinter** library.
This project performs basic arithmetic operations through an interactive GUI (Graphical User Interface) window — no browser or web server needed!

---

## ⚙️ Features
- Addition ➕
- Subtraction ➖
- Multiplication ✖️
- Division ➗
- Backspace button (`<-`) — delete last entered digit
- Clear Everything button (`CE`) — reset the display

---

## 🛠️ Libraries Used

| Library | Purpose |
|---------|---------|
| `tkinter` | Built-in Python library for creating the GUI window, buttons & entry box |

> No external libraries needed — `tkinter` comes pre-installed with Python! ✅

---

## 📂 Project Structure

```
Calculator-Using-Tkinter/
│
├── CALCULATOR USING TKINTER.ipynb       ← Main Python script
├── README.md                            ← Project documentation
└── Images/
    └── calculator_screenshot.png
```

---

## ▶️ How to Run

### Step 1 — Make sure Python is installed:
```bash
python --version
```

### Step 2 — Run the script:
```bash
python calculator.py
```

### Step 3 — Calculator window opens automatically! ✅

---

## 🔍 How It Works

```
Step 1 → User enters first number using number buttons (0-9)
Step 2 → User clicks an operator button (+, -, x, %)
         → First number is stored
         → Display is cleared for second number
Step 3 → User enters second number
Step 4 → User clicks = button
         → Calculation is performed
         → Result is displayed
```

---

## 🧠 Key Functions Explained

| Function | What it does |
|----------|-------------|
| `click(num)` | Appends clicked number to the display |
| `add()` | Stores first number & sets operation to addition |
| `sub()` | Stores first number & sets operation to subtraction |
| `mult()` | Stores first number & sets operation to multiplication |
| `div()` | Stores first number & sets operation to division |
| `equal()` | Reads second number, performs operation & shows result |
| `back()` | Deletes last digit from display |
| `clear()` | Clears entire display |

---

## 💡 Concepts Used

- `tkinter` — GUI window creation
- `Entry` widget — display box for numbers
- `Button` widget — number & operator buttons
- `global` variables — storing first number & operation type
- `lambda` functions — passing arguments to button commands
- `if / elif` logic — selecting correct math operation

---

## 🔗 References
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Python Official Website](https://www.python.org)
