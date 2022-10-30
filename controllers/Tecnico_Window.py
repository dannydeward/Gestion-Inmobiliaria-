from PySide6.QtWidgets import QWidget

from view.WindowTecnico import Ui_Form_Tecnicos

from view.Caracteristicas_Generales import GeneralCaracteristicas



class TecniForm(QWidget, Ui_Form_Tecnicos):
    
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.ui=GeneralCaracteristicas(self)
        
        
    def mousePressEvent(self,event):#mover la ventana con el cursos
        self.ui.mouse_press_event(event)