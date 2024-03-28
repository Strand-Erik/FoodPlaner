import customtkinter as ctk

class GroceryListWiget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Title label for the Grocery List
        self.title_label = ctk.CTkLabel(self, text="Grocery List", anchor="w")
        self.title_label.pack(fill="x")

        # Scrollable frame for the grocery list
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)

        for i in range(15):
            item_label = ctk.CTkLabel(self.scrollable_frame, text=f"Item {i+1}")
            item_label.pack()