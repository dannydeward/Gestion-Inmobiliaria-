from PySide6.QtWidgets import QWidget, QToolButton, QGraphicsSceneMouseEvent

from view.Window_Propi import Ui_Form_Propiedad

from view.Caracteristicas_Generales import GeneralCaracteristicas



class PropiWindowForm(QWidget, Ui_Form_Propiedad):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ui=GeneralCaracteristicas(self)
        self.buttons_funcion()
        
        
        
    def mousePressEvent(self,event):#mover la ventana con el cursos
        self.ui.mouse_press_event(event)



    def open_tablet_Agregar (self,event):
        self.toolButton_Agregarp.clicked.connect(self.tableWidget_agregar)
        self.tableWidget_agregar.setVisible(True)
                                
    
    def buttons_funcion (self):
        self.toolButton_Agregarp.clicked.connect(self.open_tablet_Agregar)