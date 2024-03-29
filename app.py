#!/usr/bin/env python3

import customtkinter as ctk
from src.gui.wigets.grocery_list_wiget import GroceryListWiget
from src.gui.wigets.recipe_chooser_widget import RecipeChooserWidget

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("src/gui/themes/dark-blue.json")
        ctk.set_appearance_mode('system')

        self.title('Recipe to Grocery List App')
        self.geometry('1300x800')

        tabs = ctk.CTkTabview(self)
        tabs.pack(expand=True, fill="both")

        # Creating tabs
        self.list_tab = tabs.add("List")
        self.recipes_tab = tabs.add("Recipes")
        self.history_tab = tabs.add("History")

        # Initializing components in the List tab
        self.initialize_list_tab()
        
        self.mainloop()

    def initialize_list_tab(self):
        self.recipe_chooser = RecipeChooserWidget(self.list_tab)
        self.recipe_chooser.pack(side="left", fill="both", expand=True, padx=20)

        self.grocery_list = GroceryListWiget(self.list_tab)
        self.grocery_list.pack(side="right", fill="both", expand=True, padx=20)

if __name__ == "__main__":
    app = App()