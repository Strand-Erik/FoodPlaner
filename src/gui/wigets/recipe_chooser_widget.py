import customtkinter as ctk

class RecipeChooserWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent = parent
        self.title_font = ctk.CTkFont(family="Roboto", size=35)
        self.button_font = ctk.CTkFont(family="Roboto", size=25)
        
        # Title label for the Recipe Chooser
        self.title_label = ctk.CTkLabel(self, text="Used Recipes", font=self.title_font, anchor="w")
        self.title_label.pack(fill="x", padx=20, pady=5)

        # Scrollable frame for the recipes
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)

        # Button for generating a list of recipies
        self.generate_button = ctk.CTkButton(self, text="Generate", font=self.button_font, width=40, command=self.generate_action)
        self.generate_button.pack(pady=8)

        # Prototype data
        for i in range(10):
            recipe_label = ctk.CTkLabel(self.scrollable_frame, text=f"Recipe {i+1}")
            recipe_label.pack()

    def generate_action(self):
        print("Test generate")