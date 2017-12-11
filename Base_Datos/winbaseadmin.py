import gi
import sqlite3 as dbapi
import Base_Datos.formAdmin

gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from Base_Datos import formAdmin

class DataBaseAdmin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Base de Datos Clientes-GYM")
        self.set_default_size(250,150)
        self.set_border_width(10)

        self.columnas=["Nombre","Apellido","Teléfono",
                  "CP","DNI","Direccion",
                  "Poblacion","Provincia","Deportes",
                  "Objetivo","Fisio","Trainer",
                  "Sauna"]

        self.modelo = Gtk.ListStore(str, str, int, int, int, str, str, str, str, str, str, str, str)

        base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
        cursor = base.cursor()
        cursor.execute("SELECT * FROM clientes")

        for i in cursor:
            self.modelo.append(i)

        vista = Gtk.TreeView(model=self.modelo)
        for i in range(len(self.columnas)):
            celda = Gtk.CellRendererText(editable=True)
            columna = Gtk.TreeViewColumn(self.columnas[i], celda, text=i)
            celda.connect("edited", self.on_edit, self.modelo, i, self.columnas[i])

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
        Base_Datos.formAdmin.FormularioGym()
        self.destroy()

    def on_edit(self, editar):
        base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
        cursor = base.cursor()
        cursor.execute("UPDATE clientes set" +self.columnas+ " = '"+self.modelo+"' WHERE DNI = ' "+self.columnas[4]+"'")
        base.commit()

if __name__ == "__main__":
    DataBaseAdmin()
    Gtk.main()
