from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QGraphicsDropShadowEffect




class GeneralCaracteristicas():
    def __init__(self, ui):
        self.ui=ui
        self.remove_titulo()
        self.ui.frame_encabezado.mouseMoveEvent=self. Move_window
        self.funcion_buttons()
  
    def maximax_window(self):
        self.ui.showMaximized()
        self.ui.toolButton_MaxiP.setVisible(False)
        
    def mini_window(self):
        self.ui.showMinimized()
        self.ui.toolButton_MiniP()
        
         
    def restaure_window(self):
        self.ui.showNormal()
        self.ui.toolButton_MaxiP.setVisible(True)
    
    def funcion_buttons(self):
        self.ui.toolButton_MaxiP.clicked.connect(self.maximax_window)
        self.ui.toolButton_restaure.clicked.connect(self.restaure_window)
        self.ui.toolButton_MiniP.clicked.connect(self.mini_window)
        self.ui.toolButton_CloseP.clicked.connect(self.ui.close)
       
     
    def remove_titulo(self):# funcion para remover el titulo del widget y dejar transparente el fondo gris
        self.ui.setAttribute(Qt.WA_TranslucentBackground,True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        self.self_window_shadow()
       
    def mouse_press_event(self,event): #conecta con funcion mousePressEvent en Mianwiondow-carpatea controllers
            self.drag_pos=event.globalPos()
            
    def Move_window(self, event):
         if event.buttons()== Qt.LeftButton:
             self.ui.move(self.ui.pos() + event.globalPos()-self.drag_pos)
             self.drag_pos =event.globalPos()
             
    def  self_window_shadow(self): # funcion
        shadow= QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.ui.background_frame.setGraphicsEffect(shadow)
       
       
  