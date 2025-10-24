# import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox

# define the resturantmanagementapp class
class RestuarantOrderManagement:
    # initialize the application
    def __init__(self, root):
        self.root= root # the main window of the app
        self.root.title(
            "Restuarant Management App"
        ) # set the title of the window

        # a dictionary to store the menu items and their prices
        self.menu_items = {
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":3,
            "PIZZA MEAL":4,
            "CHEESE BURGER":2.5,
            "DRINKS":1
        }

        self.exchange_rate = 123 # exchange rate for currency conversion

        self.setup_background(root) # set up the background image

        # create a frame to hold the widget
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # center the frame

        # heading label
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        # ditionaries to store labels and entry references
        self.menu_labels = {}
        self.menu_quantities = {}

        # create label and entry widgets for each menu items
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial",12)
            )
            label.grid(row=i, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        # currency selection
        self.currecy_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
        )
        # dropdown for currency selection
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currecy_var,
            state = ("readonly"),
            width = 18,
            values=('USD','BDT')
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0) # set default currency

        # update prices when currccy changes
        self.currecy_var.trace('w',self.update_menu_prices)

        # button to place the order 
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    # method to set up the background image 
    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

        original_image = tk.PhotoImage(file="background.png")
        background_image = original_image.subsample(
            original_image.width() // bg_width,
            original_image.height() // bg_height
        )
        canvas.create_image(0,0, anchor=tk.NW, image=background_image)
        canvas.image = background_image

    # method to update the menu prices based on the selected currecy
    def update_menu_prices(self, *args):
        currency = self.currecy_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price})")

    # method to place an order 
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currecy_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
            
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            # show error of no items are ordered
            messagebox.showerror("Error","Please order at least one item")

# block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestuarantOrderManagement(root)
    root.geometry("800x600") # set window size
    root.mainloop() # start GUI loop