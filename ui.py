# Importaciones y librerias
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import db
import helpers



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



# Ventana de creacion de cliente
class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="RUT: ").grid(row=0, column=0)
        Label(frame, text="NOMBRE: ").grid(row=1, column=0)
        Label(frame, text="APELLIDO: ").grid(row=2, column=0)

        # Entries
        rut = Entry(frame)
        rut.grid(row=0, column=1)
        rut.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        apellido = Entry(frame)
        apellido.grid(row=2, column=1)
        apellido.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        crear = Button(frame, text="Crear", command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [False, False, False]
        self.crear = crear
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def create_client(self):
        self.master.treeview.insert(
                parent='', index='end', iid=self.rut.get(),
                values=(self.rut.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.crear(self.rut.get(), self.nombre.get(), self.apellido.get())
        showinfo(title="Exito!", message=f"Cliente {self.nombre.get()} {self.apellido.get()} creado con exito!")
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = helpers.rut_validator(valor, db.Clientes.lista) if index == 0 else \
            (valor.isalpha() and len(valor) > 1 and len(valor) < 30)
        event.widget.configure({"bg":"green" if valido else "red"})
        # cambiar el estado del boton en base a las validaciones
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [True, True, True] else DISABLED)



# Ventana de modificacion de cliente
class ModifyClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Modificar/Editar cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="RUT: ").grid(row=0, column=0)
        Label(frame, text="NOMBRE: ").grid(row=1, column=0)
        Label(frame, text="APELLIDO: ").grid(row=2, column=0)

        # Entries
        rut = Entry(frame)
        rut.grid(row=0, column=1)
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        apellido = Entry(frame)
        apellido.grid(row=2, column=1)
        apellido.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, 'values')
        rut.insert(0, campos[0])
        rut.config(state=DISABLED)
        nombre.insert(0, campos[1])
        apellido.insert(0, campos[2])

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        editar = Button(frame, text="Editar", command=self.modify_client)
        editar.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [True, True]
        self.editar = editar
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def modify_client(self):
        cliente = self.master.treeview.focus()
        self.master.treeview.item(cliente, values=(self.rut.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.modificar(self.rut.get(), self.nombre.get(), self.apellido.get())
        showinfo(title="EXITO!", message=f"cliente {self.nombre.get()} {self.apellido.get()} modificado con exito!")
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = valor.isalpha() and len(valor) > 1 and len(valor) < 30
        event.widget.configure({"bg":"green" if valido else "red"})
        # cambiar el estado del boton en base a las validaciones
        self.validaciones[index] = valido
        self.editar.config(state=NORMAL if self.validaciones == [True, True] else DISABLED)



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

        #Botones
        frame = Frame(self)
        frame.pack(pady=10)

        Button(frame, text="Crear", command=self.create).grid(row=0, column=0, padx=5)
        Button(frame, text="Modificar", command=self.modify).grid(row=0, column=1, padx=5)
        Button(frame, text="Eliminar", command=self.delete).grid(row=0, column=2, padx=5)

        # Para acceder a el como un widget en otros metodos
        self.treeview = treeview

    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            confirmar = askokcancel(title="confiarmar borrado", message=f"Estas seguro de borrar a {campos[1]} {campos[2]}?")
            if confirmar:
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])
                showinfo(title="EXITO!", message=f"cliente {campos[1]} {campos[2]} eliminado con exito!")
        else: showinfo(title="ERROR!", message="No hay un cliente seleccionado!")

    def create(self):
        CreateClientWindow(self)

    def modify(self):
        ModifyClientWindow(self) if self.treeview.focus() else showinfo(title="ERROR!", message="No hay un cliente seleccionado!")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()