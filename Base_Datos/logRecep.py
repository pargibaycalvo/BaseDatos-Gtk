import gi
import Base_Datos.form
import Base_Datos.formtrainer
import sqlite3 as dbapi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaLogin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Login GYM - pargibay 6150")
        self.set_border_width(10)
        self.set_default_size(350, 150)

        cajaGeneral = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaGeneral)

        lbltitulo = Gtk.Label()
        lbltitulo.set_markup("<b>Sesion Recepcion</b>")
        cajaGeneral.add(lbltitulo)

        frameLogin = Gtk.Frame()
        cajaInvisibleV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameLogin.add(cajaInvisibleV)

        lblNombre = Gtk.Label(label="User", xalign=0)
        self.txtNombre = Gtk.Entry()
        lblPass = Gtk.Label(label="Password", xalign=0)
        self.txtPass = Gtk.Entry()
        self.txtPass.set_visibility(False)
        btnLogear = Gtk.Button(label="Entry")
        btnLogear.connect("clicked", self.on_btn_Clicked)
        self.lblCorInc = Gtk.Label(xalign=0)
        btnReturn = Gtk.Button(label="Return")
        btnReturn.connect("clicked", self.on_btn_Return)

        cajaInvisibleV.pack_start(lblNombre, True, False, 0)
        cajaInvisibleV.pack_start(self.txtNombre, True, False, 0)
        cajaInvisibleV.pack_start(lblPass, True, False, 0)
        cajaInvisibleV.pack_start(self.txtPass, True, False, 0)
        cajaInvisibleV.pack_start(btnLogear, True, False, 10)
        cajaInvisibleV.pack_start(btnReturn, True, False, 0)
        cajaInvisibleV.pack_start(self.lblCorInc, True, False, 0)

        cajaGeneral.add(frameLogin)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_Clicked(self, widget):
        base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/userrecep.db")
        cursor = base.cursor()
        usr = (self.txtNombre.get_text())
        pas = (self.txtPass.get_text())
        cursor.execute('SELECT * from gym WHERE user=? AND pass=?',(usr, pas))

        if (cursor.fetchone()is not None):
            self.lblCorInc.set_text(str("Login Correcto"))
            Base_Datos.form.FormularioGym()
            self.destroy()
        else:
            self.lblCorInc.set_text(str("Credenciales incorrectas"))

    def on_btn_Return(self, boton):
        Base_Datos.inicio.VentanaInicio()
        self.destroy()


if __name__ == "__main__":
    fiestra = VentanaLogin()
    Gtk.main()