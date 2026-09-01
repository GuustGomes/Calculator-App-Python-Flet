# Calculator App — Python and Flet

A desktop calculator application developed using Python and Flet, featuring a minimalist graphical interface and basic arithmetic operations.

## Preview

[Calculator App]
<img width="971" height="787" alt="Calculator App" src="https://github.com/user-attachments/assets/ecd93b13-9900-4460-b31e-1732e765929d" />

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Percentage calculation
- Positive/negative number conversion
- Decimal number support
- Clear function (`AC`)
- Error handling
- Fixed-size desktop window
- Always-on-top window mode

## Technologies

- Python
- Flet
- Decimal

## How It Works

The application uses a graphical interface built with Flet. User interactions with the calculator buttons are managed by event-driven functions, while the calculation logic processes the entered mathematical expressions.

The calculator also utilizes Python's `Decimal` module to control the number of decimal places displayed in the result.

## Installation

Clone the repository:

```bash
git clone https://github.com/GuustGomes/Calculator-App-Python-Flet.git
```
Navigate to the project directory:
```bash
cd Calculator-App-Python-Flet
```
Install the required dependency:
```bash
pip install flet
```
Project Structure
```text
Calculator-App-Python-Flet/

├── main.py
├── calculatorApp.png
├── calculatorApp.exe
└── README.md
```
Concepts Practiced

This project was developed as a practical exercise to reinforce fundamental concepts of Python and GUI (Graphical User Interface) programming, including:

Functions
Conditional structures
Lists and dictionaries
List comprehensions
Event handling
String manipulation
Exception handling
Decimal number formatting
GUI development
Limitations

This project was created as an introductory Python application and intentionally maintains a simple architecture.

The current implementation uses Python's `eval()` function to evaluate mathematical expressions. This approach is suitable for the current controlled interface but would require re-evaluation for a production-ready application.

Future Improvements
Possible improvements for future versions include:
- Replacing `eval()` with a safer expression evaluation approach
- Improving the calculator's internal architecture
- Adding automated tests
- Improving input validation
- Adding keyboard support
- Adding calculation history
- Improving error handling
