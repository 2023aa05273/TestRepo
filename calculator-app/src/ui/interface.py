class CalculatorUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.create_window()

    def create_window(self):
        self.result_var = StringVar()
        self.result_entry = Entry(self.master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        self.add_buttons()

    def add_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            btn = Button(self.master, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.on_button_click(b))
            btn.grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == '=':
            try:
                result = eval(self.result_var.get())
                self.display_result(result)
            except Exception as e:
                self.display_result("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button)

    def display_result(self, result):
        self.result_var.set(result)