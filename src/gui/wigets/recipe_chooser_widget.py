import customtkinter as ctk

class RecipeChooserWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Title label for the Recipe Chooser
        self.title_label = ctk.CTkLabel(self, text="Used Recipes", anchor="w")
        self.title_label.pack(fill="x")

        # Scrollable frame for the recipes
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)

        for i in range(10):
            recipe_label = ctk.CTkLabel(self.scrollable_frame, text=f"Recipe {i+1}")
            recipe_label.pack()