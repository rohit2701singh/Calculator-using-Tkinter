from tkinter import *

COLOR = "#7c9d96"
first_number = second_number = operator = None


def screen_clear():
    result_label.config(text="")
    status_show.config(text="")


def num_press(digit):
    current_value = result_label.cget("text")  # or use result_label["text"]
    new_value = current_value + str(digit)  # press digit 7 and again 7. result 77
    result_label.config(text=new_value)


def get_operator(op):
    global first_number, operator
    first_number = int(result_label['text'])
    status_show.config(text=str(first_number))
    operator = op
    status_show.config(text=str(first_number) + " " + operator)

    result_label.config(text="")


def final_result():
    global first_number, second_number, operator
    second_number = int(result_label["text"])
    status_show.config(text=str(first_number) + " " + operator + " " + str(second_number))

    if operator == "+":
        result_label.config(text=str(first_number + second_number))
    elif operator == "-":
        result_label.config(text=str(first_number - second_number))
    elif operator == "*":
        result_label.config(text=str(first_number * second_number))
    elif operator == "/":
        if second_number == 0:
            result_label.config(text="error")
        else:
            result_label.config(text=str(round(first_number / second_number, 6)))


# ----- creating UI ----------------

window = Tk()
window.title("calculator")
window.geometry('350x480')
window.config(padx=15, bg="#3b638c")
window.resizable(width=False, height=True)

status_show = Label(text="", bg="black", fg="white", width=19, anchor="w", font=("ariel", 20, 'bold'), wraplength=320)
status_show.grid(row=0, column=0, pady=(30, 5), columnspan=4, sticky="w")

result_label = Label(text="", bg="#3b638c", fg="white", font=("ariel", 30, 'bold'), wraplength=320)
result_label.grid(row=1, column=0, pady=(30, 10), columnspan=4, sticky="w")

btn7 = Button(text="7", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(7))
btn7.grid(row=2, column=0, padx=3)

btn8 = Button(text="8", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(8))
btn8.grid(row=2, column=1, padx=3)

btn9 = Button(text="9", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(9))
btn9.grid(row=2, column=2, padx=3)

add_button = Button(text="+", bg="#017a79", fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: get_operator("+"))
add_button.grid(row=2, column=3, padx=3, pady=(3, 3))

btn4 = Button(text="4", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(4))
btn4.grid(row=3, column=0, padx=3, )

btn5 = Button(text="5", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(5))
btn5.grid(row=3, column=1, padx=3)

btn6 = Button(text="6", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(6))
btn6.grid(row=3, column=2, padx=3)

subtract_btn = Button(text="-", bg="#017a79", fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: get_operator("-"))
subtract_btn.grid(row=3, column=3, padx=3, pady=(3, 3))

btn1 = Button(text="1", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(1))
btn1.grid(row=4, column=0, padx=3, )

btn2 = Button(text="2", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(2))
btn2.grid(row=4, column=1, padx=3)

btn3 = Button(text="3", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(3))
btn3.grid(row=4, column=2, padx=3)

multiply_btn = Button(text="*", bg="#017a79", fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: get_operator("*"))
multiply_btn.grid(row=4, column=3, padx=3, pady=(3, 3))

clr_btn = Button(text="clr", bg="#017a79", fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=screen_clear)
clr_btn.grid(row=5, column=0, padx=3, )

btn0 = Button(text="0", bg=COLOR, fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: num_press(0))
btn0.grid(row=5, column=1, padx=3)

equal_btn = Button(text="=", bg="#017a79", fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=final_result)
equal_btn.grid(row=5, column=2, padx=3)

divide_btn = Button(text="/", bg="#017a79", fg="white", width=5, height=2, font=("ariel", 16, "bold"), command=lambda: get_operator("/"))
divide_btn.grid(row=5, column=3, padx=3, pady=(3, 3))

window.mainloop()
