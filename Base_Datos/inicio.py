import gi
import Base_Datos.log
import Base_Datos.logTrainer
import Base_Datos.logRecep
import sys

gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gio

class VentanaInicio(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="")
        self.set_default_size(350,100)
        self.set_border_width(10)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(cajaH)

        cabeceira = Gtk.HeaderBar(title="Bienvenido al GYM-pargibay")
        cabeceira.set_subtitle("Inicie sesion")
        cabeceira.props.show_close_button = True
        self.set_titlebar(cabeceira)

        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(), "linked")

        frameLoginAdmin = Gtk.Frame()
        cajaInvisibleV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameLoginAdmin.add(cajaInvisibleV)

        btnAdmin = Gtk.Button(label="Administrador")
        btnAdmin.connect("clicked", self.on_btn_Admin)
        btnTrainer = Gtk.Button(label="Entrenadores")
        btnTrainer.connect("clicked", self.on_btn_Trainer)
        btnRecep = Gtk.Button(label="Recepcion")
        btnRecep.connect("clicked", self.on_btn_Recep)
        btnExit = Gtk.Button(label="Salir")
        btnExit.connect("clicked", self.on_btn_Exit)

        cajaInvisibleV.pack_start(btnRecep, True, False, 0)
        cajaInvisibleV.pack_start(btnTrainer, True, False, 0)
        cajaInvisibleV.pack_start(btnAdmin, True, False, 20)
        cajaInvisibleV.pack_start(btnExit, True, False, 0)

        cajaH.add(frameLoginAdmin)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_Admin(self, boton):
        Base_Datos.log.VentanaLogin()
        self.destroy()

    def on_btn_Trainer(self, boton):
        Base_Datos.logTrainer.VentanaLogin()
        self.destroy()

    def on_btn_Recep(self, boton):
        Base_Datos.logRecep.VentanaLogin()
        self.destroy()

    def on_btn_Exit(self, boton):
        sys.exit()

if __name__ == "__main__":
    fiestra = VentanaInicio()
    Gtk.main()