import sqlite3 as dbapi

import paquete.formtrainer
import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class DataBaseRecep(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Base de Datos Clientes-GYM")
        self.set_default_size(250,150)
        self.set_border_width(10)

        columnas=["Nombre","Apellido","Teléfono",
                  "CP","DNI","Direccion",
                  "Poblacion","Provincia","Deportes",
                  "Objetivo","Fisio","Trainer",
                  "Sauna"]

        modelo = Gtk.ListStore(str, str, int, int, int, str, str, str, str, str, str, str, str)

        base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
        cursor = base.cursor()
        cursor.execute("SELECT * FROM clientes")

        for i in cursor:
            modelo.append(i)

        vista = Gtk.TreeView(model=modelo)
        for i in range(len(columnas)):
            celda = Gtk.CellRendererText()
            celda.set_property("editable", False)
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)

            vista.append_column(columna)

        btnReturn = Gtk.Button(label="Atrás")
        btnReturn.connect("clicked", self.on_btn_return)
        self.Conndb = Gtk.Label(xalign=0)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        cajaH.pack_start(vista, False, False, 0)
        cajaH.pack_start(btnReturn,True, False, 0)
        self.add(cajaH)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_return(self, boton):
        paquete.form.FormularioGym()
        self.destroy()

if __name__ == "__main__":
    DataBaseRecep()
    Gtk.main()
