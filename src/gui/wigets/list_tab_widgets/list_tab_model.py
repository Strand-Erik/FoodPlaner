import customtkinter as ctk

from src.gui.wigets.list_tab_widgets.grocery_list_wiget import GroceryListWiget
from src.gui.wigets.list_tab_widgets.recipe_chooser_widget import RecipeChooserWidget

class ListTabModel:
    def __init__(self, tab: ctk.CTkFrame):
        self.tab: ctk.CTkFrame = tab
        self.init_tab()
        

    def init_tab(self):
        self.recipe_chooser = RecipeChooserWidget(self.tab)
        self.recipe_chooser.pack(side="left", fill="both", expand=True, padx=20)

        self.grocery_list = GroceryListWiget(self.tab)
        self.grocery_list.pack(side="right", fill="both", expand=True, padx=20)
