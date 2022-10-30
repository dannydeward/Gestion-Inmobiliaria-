import sys
from PySide6.QtWidgets import QApplication
from controllers.MainWindow import MainWindowForm


#esta es la funcion de inicio de la aplicacion. que nos lleva a ala venta principal 

if __name__=='__main__':
    app= QApplication()
    
    window=MainWindowForm()
    window.show()
    
    sys.exit(app.exec())