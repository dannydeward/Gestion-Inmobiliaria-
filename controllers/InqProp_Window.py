from PySide6.QtWidgets import QWidget

from view.WindowInqProp import Ui_Form_Inqui_Propi

from view.Caracteristicas_Generales import GeneralCaracteristicas



class InquiPropForm(QWidget, Ui_Form_Inqui_Propi):
    
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.ui=GeneralCaracteristicas(self)
        
        
    def mousePressEvent(self,event):#mover la ventana con el cursos
        self.ui.mouse_press_event(event)