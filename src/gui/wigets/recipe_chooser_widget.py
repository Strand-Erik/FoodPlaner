import customtkinter as ctk
from src.gui.wigets.recipe_widget import RecipeWidget

class RecipeChooserWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.title_font = ctk.CTkFont(family="Roboto", size=35)
        self.button_font = ctk.CTkFont(family="Roboto", size=25)
        
        # Title label for the Recipe Chooser
        self.title_label = ctk.CTkLabel(self, text="Used Recipes", font=self.title_font, anchor="w")
        self.title_label.pack(fill="x", padx=20, pady=5)

        # Scrollable frame for the recipes
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)

        # Button for generating a list of recipes
        self.generate_button = ctk.CTkButton(self, text="Generate", font=self.button_font, width=40, command=self.generate_action)
        self.generate_button.pack(pady=8)

        # Prototype data
        for i in range(10):
            RecipeWidget(self.scrollable_frame, f"Recipe {i+1}").pack(pady=2, padx=10, fill="x")

        # Container frame for the last buttons
        self.buttons_frame = ctk.CTkFrame(self.scrollable_frame)
        self.buttons_frame.pack(fill="x", pady=10)
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

        # Add Random button
        self.add_random_button = ctk.CTkButton(self.buttons_frame, text="Add Random", font=self.button_font, command=self.add_random_recipe)
        self.add_random_button.grid(row=0, column=0, padx=5, pady=8)

        # Choose More button
        self.choose_more_button = ctk.CTkButton(self.buttons_frame, text="Choose More", font=self.button_font, command=self.choose_more_recipes)
        self.choose_more_button.grid(row=0, column=1, padx=5, pady=8)

    def generate_action(self):
        print("Test generate")

    def add_random_recipe(self):
        print("Add random recipe")

    def choose_more_recipes(self):
        print("Choose more recipes")
