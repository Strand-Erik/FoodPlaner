import customtkinter as ctk
from src.gui.wigets.list_tab_widgets.grocery_list_wiget import GroceryListWiget
from src.gui.wigets.list_tab_widgets.list_tab_model import ListTabModel
from src.gui.wigets.list_tab_widgets.recipe_chooser_widget import RecipeChooserWidget

class ListTab:
    def __init__(self, tab: ctk.CTkFrame):
        self.tab: ctk.CTkFrame = tab
        self.init_tab()
        

    def init_tab(self):
        self.model = ListTabModel()

        self.recipe_chooser = RecipeChooserWidget(self.tab, self.model)
        self.recipe_chooser.pack(side="left", fill="both", expand=True, padx=20)

        self.grocery_list = GroceryListWiget(self.tab, self.model)
        self.grocery_list.pack(side="right", fill="both", expand=True, padx=20)
