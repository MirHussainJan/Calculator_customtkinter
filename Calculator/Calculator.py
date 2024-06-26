import customtkinter as ctk
import math

def append(text):
    current_text = Screen.cget("text")  # Get the current text from the Screen label
    if current_text == "0" and text != ".":
        new_text = text
    else:
        new_text = current_text + text

    Screen.configure(text=new_text)

def calculate():
    try:
        current_text = Screen.cget("text")
        
        # Check for square root symbol (√)
        if '√' in current_text:
            parts = current_text.split('√')
            if len(parts) == 2:
                num_expr = parts[1].strip()
                result = eval(num_expr)
                result = math.sqrt(result)

        else:
            result = eval(current_text)  # Evaluate the whole expression if no √ symbol
        
        if isinstance(result, int):
            formatted_str = str(result)  # Convert integer to string
        else:
            formatted_str = "{:.2f}".format(result)  # Format float to 2 decimal places
        
        Screen.configure(text=formatted_str)
        
    except ValueError:
        Screen.configure(text="Syntax Error!")
    except ZeroDivisionError:
        Screen.configure(text="Division by zero!")
    except Exception as e:
        Screen.configure(text=f"Error: {str(e)}")

def delete():
    current_text = Screen.cget("text")
    new_text = current_text[:-1]
    Screen.configure(text=new_text if new_text else "0")

def clear():
    Screen.configure(text="0")  # Reset the screen label text to "0"

root = ctk.CTk()
root.title("Calculator")
root.geometry("650x300")

# Display screen for calculator
Calculator = ctk.CTkFrame(root)
Screen = ctk.CTkLabel(root, text="0", font=("Arial", 30))
Screen.pack(pady=10)
Calculator.pack(pady=10)

# Define buttons with their labels and grid positions
buttons = [
    ("C", 0, 0),
    ("(", 0, 1),
    (")", 0, 2),
    ("/", 0, 3),
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("*", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("-", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("+", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("√", 4, 2),
    ("=", 4, 3),
]

# Create buttons and place them in the grid
for text, row, col in buttons:
    if text == '=':
        button = ctk.CTkButton(Calculator, text=text, font=("Arial", 20, "bold"), command=calculate)
    elif text == '√':
        button = ctk.CTkButton(Calculator, text=text, font=("Arial", 20, "bold"), command=lambda t=text: append(t))
    elif text == 'DEL':
        button = ctk.CTkButton(Calculator, text=text, font=("Arial", 20, "bold"), command=delete)
    elif text == 'C':
        button = ctk.CTkButton(Calculator, text=text, font=("Arial", 20, "bold"), command=clear)
    else:
        button = ctk.CTkButton(Calculator, text=text, font=("Arial", 20, "bold"), command=lambda t=text: append(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.configure(corner_radius=20)

def key(event):
    key_press = event.keysym
    print(key_press)
    if key_press.isdigit():
        append(event.char)
    elif key_press == 'period':
        append('.')
    elif key_press == 'minus':
        append('-')
    elif key_press == 'asterisk':
        append('*')
    elif key_press == 'slash':
        append('/')
    elif key_press == 'plus':
        append('+')
    elif key_press == 'parenleft':
        append('(')
    elif key_press == 'parenright':
        append(')')
    elif key_press == 'Return':
        calculate()
    elif key_press == 'BackSpace':
        delete()
    elif key_press == 'Delete':
        clear()

# Bind all keys to the key function
root.bind_all('<Key>', key)

root.mainloop()