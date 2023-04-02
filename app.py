import customtkinter as ctk
dimensions = []

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        global startline

        self.title("Box Bot")
        self.minsize(400, 600)
        self.maxsize(400, 600)
## Text ##:
        self.title = ctk.CTkLabel(
            master=self,
            text= "Box Bot",
            width=120,
            height=25,
            font=("Arial Rounded MT Bold", 50,"bold")
            )
        
        self.lengthtext = ctk.CTkLabel(
            master=self,
            text= "Insert Length:",
            font=("", 25,"bold")
            )
        
        self.widthtext = ctk.CTkLabel(
            master=self,
            text= "Insert Width:",
            font=("", 25,"bold")
            )
        
        self.heighttext = ctk.CTkLabel(
            master=self,
            text= "Insert Height:",
            font=("", 25,"bold")
            )
# Entries #
        self.lengthinput = ctk.CTkEntry(
            master=self,
            height=25,
            width=200,
            border_width=2,
            corner_radius=10
        )
        self.widthinput = ctk.CTkEntry(
            master=self,
            height=25,
            width=200,
            border_width=2,
            corner_radius=10
        )
        self.heightinput = ctk.CTkEntry(
            master=self,
            height=25,
            width=200,
            border_width=2,
            corner_radius=10
        )

## Option Menu ##       
        self.fragile = ctk.CTkOptionMenu(
            master=self,
            values=["Non-Fragile", "Fragile"]
        )


## Buttons ##
        self.addtolist= ctk.CTkButton(
            master=self,
            width=200,
            height=32,
            corner_radius=10,
            text="Add to List",
            command=self.addtolist
        )
        self.result= ctk.CTkButton(
            master=self,
            width=300,
            height=70,
            corner_radius=10,
            text="Calculate Map",
        )
        self.cancel= ctk.CTkButton(
            master=self,
            width=300,
            height=25,
            corner_radius=10,
            text="Delete last item",
            command=self.delete
        )

## Textbox ##
        self.textbox = ctk.CTkTextbox(
            master=self, 
            width=400,
            height=275,
            corner_radius=0
        )
        self.textbox.configure(state="disabled")

        self.title.grid(row=0, column=0, columnspan=2)

        self.lengthtext.grid(row=1, column=0, pady=5)
        self.widthtext.grid(row=2, column=0, pady=5)
        self.heighttext.grid(row=3, column=0, pady=5)

        self.lengthinput.grid(row=1, column=1, pady=5, sticky="w")
        self.widthinput.grid(row=2, column=1, pady=5, sticky="w")
        self.heightinput.grid(row=3, column=1, pady=5)
        
        self.fragile.grid(row=4, column=0,pady=5)
        self.addtolist.grid(row=4, column=1, pady=5)

        self.textbox.grid(row=5, column=0, columnspan=2)

        self.result.grid(row=6, column=0, columnspan=2, pady=5)
        self.cancel.grid(row=7, column=0, columnspan=2, pady=5)

    def addtolist(self):
        self.textbox.configure(state="normal")
        global dimensions

        l = float(self.lengthinput.get())
        w = float(self.widthinput.get())
        h = float(self.heightinput.get())

        dim = [l, w, h]

        dimensions.append(dim)

        self.textbox.insert("0.0" ,f"{l} x {w} x {h}\n")

        self.textbox.configure(state="disabled")

    def delete(self):
        global dimensions
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0","2.0")
        self.textbox.configure(state="disabled")
        dimensions.pop(-1)
        print(dimensions)








if __name__ == "__main__":
    app = App()
    app.grid_rowconfigure(0)
    app.grid_columnconfigure(0,weight=1)
    app.mainloop()

