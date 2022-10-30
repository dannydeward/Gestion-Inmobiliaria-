from PySide6.QtWidgets import QWidget

from view.Main_Window import Form_mainWindow
from controllers.Propi_Window import PropiWindowForm
from controllers.InqProp_Window import InquiPropForm
from controllers.Servicios_Window import ServiForm
from controllers.Tecnico_Window import TecniForm
from controllers.Informes_Window import InforForm

from view.Caracteristicas_Generales import GeneralCaracteristicas
#ventana principal de programa donde encontramos los diferentes accesos, cada botos se dirige a una ventana con acciones diferentes 

class MainWindowForm (QWidget, Form_mainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui=GeneralCaracteristicas(self)
        
        self.toolButton_Pro.clicked.connect(self.open_propiedad)
        self.toolButton_InqPro.clicked.connect(self.open_Inqprop)
        self.toolButton_Ser.clicked.connect(self.open_servicios)
        self.toolButton_Tecni.clicked.connect(self.open_tecnico)
        self.toolButton_Infor.clicked.connect(self.open_informes)
        
        
    def mousePressEvent(self,event):#mover la ventana con el cursos
         self.ui.mouse_press_event(event)
         
    
    def open_propiedad(self):
        window=PropiWindowForm()
        window.show()
        
    def open_Inqprop(self):
        window=InquiPropForm()
        window.show()
        
    def open_servicios(self):
        window=ServiForm()
        window.show()
        
    def open_tecnico(self):
        window=TecniForm()
        window.show()
        
    def open_informes(self):
        window=InforForm()
        window.show()