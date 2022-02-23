from tkinter import *
import operator

max_width, max_height = 500, 500
app_title = "Calculator"
number_buttons = []
type_operations = ["=", "+", "-", "x", "/", "C"]
operators = {"+": operator.add, "-": operator.sub, "x": operator.mul, "/": operator.div} # etc.
operation_buttons = []

# set-up window
window = Tk()
window.title(app_title)
window.geometry(f"{max_width}x{max_height}")
window.config(bg='black')

# set-up typing area
text_box = Text(window, width=100, height=2)
text_box.config(bg='black', fg="white", font=("Helvetica", 32))
text_box.pack()

# button was clicked
def buttonClicked(index : int or str):
    button_text = index
    if type(index) == int:
        numberButton = number_buttons[index]
        button_text = numberButton['text']
    if button_text == "C":
        return text_box.delete('1.0', END)
    if button_text == "=":
        text_box_contents = text_box.get("1.0",'end-1c')
        numbers = text_box_contents.split("+")
        calculated = operators["+"](int(numbers[0]), int(numbers[1]))
        text_box.delete('1.0', END)
        text_box.insert(INSERT, f"= {calculated}")
        return 
    text_box.insert(INSERT, button_text)

# create numbers 0-9
for number in range(0, 10):
    button = Button(window, text=number, width=4, height=2, command= lambda index = number: buttonClicked(index))
    button.config(bg="#3b3d40", fg="white", font=("Helvetica", 16))
    button.place(x=(number*50), y=max_height*(20/100))
    number_buttons.append(button)
    #button.pack()

# create operations
for number, value in enumerate(type_operations):
    text = type_operations[number]
    button = Button(window, text=text, width=4, height=2, command= lambda text = value: buttonClicked(text))
    button.config(bg="#c77a3c", fg="white", font=("Helvetica", 16))
    button.place(x=(number*50), y=max_height*(40/100))
    operation_buttons.append(button)

window.mainloop()