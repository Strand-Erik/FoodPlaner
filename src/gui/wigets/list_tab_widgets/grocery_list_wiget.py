from typing import List
import customtkinter as ctk
from src.gui.wigets.list_tab_widgets.list_tab_model import ListTabModel

class GroceryListWiget(ctk.CTkFrame):
    def __init__(self, parent, model: ListTabModel):
        super().__init__(parent)
        self.parent = parent
        self.title_font = ctk.CTkFont(family="Roboto", size=35)
        self.button_font = ctk.CTkFont(family="Roboto", size=25)
        self.ingredient_font = ctk.CTkFont(family="Roboto", size=23)

        # Title label for the Grocery List
        self.title_label = ctk.CTkLabel(self, text="Grocery List", font=self.title_font, anchor="w")
        self.title_label.pack(fill="x", padx=20, pady=5)

        # Scrollable frame for the grocery list
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)

        # Button saving grocery list to history
        self.history_button = ctk.CTkButton(self, text="Save To History", font=self.button_font, width=40, command=self.save_to_history_action)
        self.history_button.pack(pady=8)

        # Prototype data
        fake_data: List[str] = [
            'Äpplen - 3 st',
            'Mjölk - 3 dl',
            'Mjöl - 5 kg',
            'Socker - 5 hg',
            'Ägg - 4 st',
            'Smör - 3 hg',
            'Bananer - 3 st',
            'Tomater - 5 st',
            'Gurka - 5 st',
            'Morötter - 2 st',
            'Kycklingbröst - 4 kg',
            'Bacon - 5 hg',
            'Salt - 1 kg',
            'Peppar - 1 kg',
            'Vetemjöl - 4 hg',
            'Grahamsmjöl - 3 hg',
            'Ris - 4 kg',
            'Pasta - 1 kg'
        ]

        self.show_igredients(fake_data)

    def show_igredients(self, ingredients: List[str]):
        for ingredient in ingredients:
            item_label = ctk.CTkLabel(self.scrollable_frame, text=ingredient, font=self.ingredient_font)
            item_label.pack(anchor='w', padx=(40, 0), pady=(0, 10))

    def save_to_history_action(self):
        print("Test save to history")