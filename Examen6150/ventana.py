import  gi
import math

gi.require_version ('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 15-12-2017")



        cajaGeneral = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.add(cajaGeneral)

        frameDatos = Gtk.Frame()
        cajaInvisibleV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameDatos.add(cajaInvisibleV1)

        cajaInvisibleH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        self.btnAceptar = Gtk.Button(label= "Aceptar")
        self.btnCancelar = Gtk.Button (label = "Cancelar")

        self.txtMarca = Gtk.Entry()
        self.lblMarca = Gtk.Label("Marca")

        self.cmbMarca = Gtk.ComboBox()

        self.lblResumo = Gtk.Label()
        self.frmMarco = Gtk.Frame()

        cajaInvisibleH1.pack_start(self.lblMarca, True, False, 0)
        cajaInvisibleH1.pack_start(self.btnAceptar, False, False, 0)

        cajaInvisibleH2.pack_start(self.txtMarca, False, True, 0)
        cajaInvisibleH2.pack_start(self.btnCancelar, False, False, 0)

        cajaInvisibleH3.pack_start(self.cmbMarca, False, False, 0)
        cajaInvisibleH3.pack_start(self.lblResumo, False, False, 0)

        self.btnAceptar.connect("clicked", self.on_btn_btnacep, self.txtMarca, "aceptar")
        self.btnCancelar.connect("clicked", self.on_btn_btncanc, self.txtMarca, "cancelar")



        cajaInvisibleV1.add(cajaInvisibleH1)
        cajaInvisibleV1.add(cajaInvisibleH2)
        cajaInvisibleV1.add(cajaInvisibleH3)


        cajaGeneral.add(frameDatos)


        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_btnacep(self, boton, txt, nome):
        if nome == "aceptar":
            self.txtMarca.get_text(self.cmbMarca)
        else:
            self.lblResumo.set_text(str("Error"))

    def on_btn_btncanc(self, boton, txt, nome):
        if nome == "cancelar":
            self.lblResumo.set_text(str("Marca non X borrada"))
        else:
            self.lblResumo.set_text(str("Marca X borrada"))






if __name__=="__main__":
    fiestra = FiestraPrincipal()
    Gtk.main()