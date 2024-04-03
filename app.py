#!/usr/bin/env python3

import customtkinter as ctk
from src.gui.wigets.list_tab_widgets.list_tab_model import ListTabModel

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("src/gui/themes/dark-blue.json")
        ctk.set_appearance_mode('system')

        self.title('Recipe to Grocery List App')
        self.geometry('1500x800')

        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(expand=True, fill="both")

        self.initialize_list_tabs()
        
        self.mainloop()

    def initialize_list_tabs(self):
        self.list_tab = self.tabs.add("List")
        self.recipes_tab = self.tabs.add("Recipes")
        self.history_tab = self.tabs.add("History")

        ListTabModel(self.list_tab)


if __name__ == "__main__":
    app = App()