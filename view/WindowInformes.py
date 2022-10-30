# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Informes_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QToolButton, QWidget)

class Ui_Form_informes(object):
    def setupUi(self, Form_informes):
        if not Form_informes.objectName():
            Form_informes.setObjectName(u"Form_informes")
        Form_informes.resize(280, 189)
        self.background_frame = QFrame(Form_informes)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setGeometry(QRect(-10, 30, 641, 441))
        self.background_frame.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.pushButton_Servicios_Ade = QPushButton(self.background_frame)
        self.pushButton_Servicios_Ade.setObjectName(u"pushButton_Servicios_Ade")
        self.pushButton_Servicios_Ade.setGeometry(QRect(10, 80, 141, 81))
        self.pushButton_Servicios_Ade.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color:rgb(170,0,0);")
        self.pushButton_Reparaciones_Ef = QPushButton(self.background_frame)
        self.pushButton_Reparaciones_Ef.setObjectName(u"pushButton_Reparaciones_Ef")
        self.pushButton_Reparaciones_Ef.setGeometry(QRect(150, 10, 141, 71))
        self.pushButton_Reparaciones_Ef.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color:rgb(170,0,0);")
        self.pushButton_Viaticos = QPushButton(self.background_frame)
        self.pushButton_Viaticos.setObjectName(u"pushButton_Viaticos")
        self.pushButton_Viaticos.setGeometry(QRect(150, 80, 141, 81))
        self.pushButton_Viaticos.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color:rgb(170,0,0);")
        self.pushButton_CajaChica = QPushButton(self.background_frame)
        self.pushButton_CajaChica.setObjectName(u"pushButton_CajaChica")
        self.pushButton_CajaChica.setGeometry(QRect(10, 0, 141, 81))
        self.pushButton_CajaChica.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color:rgb(170,0,0);")
        self.frame_encabezado = QFrame(Form_informes)
        self.frame_encabezado.setObjectName(u"frame_encabezado")
        self.frame_encabezado.setGeometry(QRect(0, 0, 281, 31))
        self.frame_encabezado.setMaximumSize(QSize(641, 31))
        self.frame_encabezado.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.frame_encabezado.setFrameShape(QFrame.StyledPanel)
        self.frame_encabezado.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_encabezado)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 51, 16))
        self.label.setStyleSheet(u"color:white;")
        self.frame_2 = QFrame(self.frame_encabezado)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 10, 121, 21))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.toolButton_CloseP = QToolButton(self.frame_2)
        self.toolButton_CloseP.setObjectName(u"toolButton_CloseP")
        self.toolButton_CloseP.setGeometry(QRect(90, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icon/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_CloseP.setIcon(icon)
        self.toolButton_MaxiP = QToolButton(self.frame_2)
        self.toolButton_MaxiP.setObjectName(u"toolButton_MaxiP")
        self.toolButton_MaxiP.setGeometry(QRect(60, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icon/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_MaxiP.setIcon(icon1)
        self.toolButton_MiniP = QToolButton(self.frame_2)
        self.toolButton_MiniP.setObjectName(u"toolButton_MiniP")
        self.toolButton_MiniP.setGeometry(QRect(30, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icon/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_MiniP.setIcon(icon2)
        self.toolButton_restaure = QToolButton(self.frame_2)
        self.toolButton_restaure.setObjectName(u"toolButton_restaure")
        self.toolButton_restaure.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icon/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_restaure.setIcon(icon3)
        self.toolButton_restaure.raise_()
        self.toolButton_CloseP.raise_()
        self.toolButton_MaxiP.raise_()
        self.toolButton_MiniP.raise_()

        self.retranslateUi(Form_informes)

        QMetaObject.connectSlotsByName(Form_informes)
    # setupUi

    def retranslateUi(self, Form_informes):
        Form_informes.setWindowTitle(QCoreApplication.translate("Form_informes", u"Form", None))
        self.pushButton_Servicios_Ade.setText(QCoreApplication.translate("Form_informes", u"Servicios adeudados", None))
        self.pushButton_Reparaciones_Ef.setText(QCoreApplication.translate("Form_informes", u"Reparaciones efectuadas", None))
        self.pushButton_Viaticos.setText(QCoreApplication.translate("Form_informes", u"Viaticos", None))
        self.pushButton_CajaChica.setText(QCoreApplication.translate("Form_informes", u"Caja Chica", None))
        self.label.setText(QCoreApplication.translate("Form_informes", u"Informes", None))
        self.toolButton_CloseP.setText(QCoreApplication.translate("Form_informes", u"...", None))
        self.toolButton_MaxiP.setText(QCoreApplication.translate("Form_informes", u"...", None))
        self.toolButton_MiniP.setText(QCoreApplication.translate("Form_informes", u"...", None))
        self.toolButton_restaure.setText(QCoreApplication.translate("Form_informes", u"...", None))
    # retranslateUi

