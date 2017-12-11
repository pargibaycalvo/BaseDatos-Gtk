import gi
import Base_Datos.inicio
import sqlite3 as dbapi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FichasGym(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GYM - pargibay 6150")
        self.set_border_width(10)
        self.set_default_size(200, 150)

        cajaGeneral = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaGeneral)

        lbltitulo = Gtk.Label(xalign=0)
        lbltitulo.set_markup("<b>Fichas de Clientes</b>")
        cajaGeneral.add(lbltitulo)

        frameFichas = Gtk.Frame(label="Fichas Clientes")
        cajaInvisibleV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameFichas.add(cajaInvisibleV1)

        frameOpciones = Gtk.Frame(label="")
        cajaInvisibleV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameOpciones.add(cajaInvisibleV2)

        cajaInvisibleH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        btnConsUs = Gtk.Button(label="Concultar Clientes")
        btnConsUs.connect("clicked", self.on_btn_consulta)

        btnCons = Gtk.Button(label="Concultar Ficha")
        btnCons.connect("clicked", self.on_btn_cons)
        self.Cons = Gtk.Label(xalign=0)
        self.txtCons = Gtk.Entry()

        btnExit = Gtk.Button(label="Cerrar Sesion")
        btnExit.connect("clicked", self.on_btn_close)
        self.Exit = Gtk.Label(xalign=0)

        cajaInvisibleV2.pack_start(btnConsUs, True, False, 0)
        cajaInvisibleV1.pack_start(self.txtCons, True, False, 0)
        cajaInvisibleV1.pack_start(btnCons, True, False, 0)
        cajaInvisibleV2.pack_start(btnExit, True, False, 0)

        cajaInvisibleV1.add(cajaInvisibleH1)
        cajaInvisibleV2.add(cajaInvisibleH2)

        cajaGeneral.add(frameFichas)
        cajaGeneral.add(frameOpciones)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_consulta(self, boton):
        Base_Datos.baselog.DataBase()
        self.destroy()

    def on_btn_cons(self, boton):
        base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
        cursor = base.cursor()
        reg = (self.txtCons.get_text())
        cursor.execute("SELECT * FROM clientes WHERE dni='%s'" % reg)
        print("Cliente")
        print("---")
        for i in cursor:
            print("Nombre=", i[0])
            print("Apellidos=", i[1])
            print("Deporte=", i[8])
            print("Objetivos=", i[9])
            print("Fisioterapeuta=", i[10])
            print("Personal Trainer=", i[11])
            print("Sauna=", i[12])
            print("---")


    def on_btn_close(self, widget):
        self.destroy()
        Base_Datos.inicio.VentanaInicio()

if __name__ == "__main__":
    fiestra = FichasGym()
    Gtk.main()


