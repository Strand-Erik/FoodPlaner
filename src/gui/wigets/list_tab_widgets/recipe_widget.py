import customtkinter as ctk

class RecipeWidget(ctk.CTkFrame):
    def __init__(self, parent, recipe_name, quantity=1):
        super().__init__(parent)
        self.recipe_name = recipe_name
        self.quantity = quantity
        self.button_font = ctk.CTkFont(family="Roboto", size=25)

        self.columnconfigure(1, weight=3)  # Give the recipe name more space

        self.quantity_label = ctk.CTkLabel(self, text=f"Quantity: {self.quantity}", font=self.button_font)
        self.quantity_label.grid(row=0, column=0, sticky='ew', padx=(10, 0))

        self.name_label = ctk.CTkLabel(self, text=self.recipe_name, font=self.button_font)
        self.name_label.grid(row=0, column=1, sticky='ew')

        self.increase_button = ctk.CTkButton(self, text="+", font=self.button_font, width=40, height=40, command=self.increase_quantity)
        self.increase_button.grid(row=0, column=2, padx=(10, 5))  # Reduce padding on the right side

        self.decrease_button = ctk.CTkButton(self, text="-", font=self.button_font, width=40, height=40, command=self.decrease_quantity)
        self.decrease_button.grid(row=0, column=3, padx=(2, 50))  # Reduce padding on the left side

        self.remove_button = ctk.CTkButton(self, text="Remove", font=self.button_font, command=self.remove)
        self.remove_button.grid(row=0, column=4, sticky='ew', padx=(0, 10))

    def increase_quantity(self):
        self.quantity += 1
        self.update_quantity_label()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.update_quantity_label()
        else:
            self.remove()

    def remove(self):
        self.destroy()

    def update_quantity_label(self):
        """Updates the text of the quantity label with the current quantity."""
        self.quantity_label.configure(text=f"Quantity: {self.quantity}")
