import tkinter as tk

root = tk.Tk()

root.geometry("800x800")
root.title("StatComparisonWebsiteGUI")

label = tk.Label(root, text="Hello", font=('Georgia', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height = 3, font=('Georgia',18))
textbox.pack()

entry = tk.Entry(root)
entry.pack(padx = 10)

button= tk.Button(root, text="Click me", font=('Georgia', 15))
button.pack(padx=10, pady=10)


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text = "1", font=('Georgia', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text = "2", font=('Georgia', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text = "3", font=('Georgia', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text = "4", font=('Georgia', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text = "5", font=('Georgia', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text = "6", font=('Georgia', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')

# in case i want to place an object
# bt4 = tk.Button(root, text="TEXT")
# bt4.place(x=200,y=200,height=100, width=100)

root.mainloop()