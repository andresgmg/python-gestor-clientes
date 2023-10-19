# Importaciones y librerias
from tkinter import *
from tkinter import ttk
import db



# Configuracion de la ventana principal
class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(width=False, height=True)



# Build de la ventana principal
class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()

    def build(self):
        # Top Frame
        frame = Frame(self)
        frame.pack()

        # Scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Treeview
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('RUT', 'Nombre', 'Apellido')
        treeview['yscrollcommand'] = scrollbar.set
        treeview.pack()

        # Column format
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("RUT", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)

        # Heading format
        treeview.heading("#0", anchor=CENTER)
        treeview.heading("RUT", text="RUT", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)

        # Database Import
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.rut,
                values=(cliente.rut, cliente.nombre, cliente.apellido))

        # Pack
        treeview.pack()



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()