# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'servicios_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QWidget)

class Ui_Form_servicios(object):
    def setupUi(self, Form_servicios):
        if not Form_servicios.objectName():
            Form_servicios.setObjectName(u"Form_servicios")
        Form_servicios.resize(621, 480)
        self.background_frame = QFrame(Form_servicios)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setGeometry(QRect(-20, 30, 641, 441))
        self.background_frame.setStyleSheet(u"background:white;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.tableWidget_servicios = QTableWidget(self.background_frame)
        self.tableWidget_servicios.setObjectName(u"tableWidget_servicios")
        self.tableWidget_servicios.setGeometry(QRect(20, 60, 621, 391))
        self.label_Servicios = QLabel(self.background_frame)
        self.label_Servicios.setObjectName(u"label_Servicios")
        self.label_Servicios.setGeometry(QRect(30, 10, 51, 16))
        self.label_Servicios.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color:rgb(170,0,0);")
        self.comboBox_servicios = QComboBox(self.background_frame)
        self.comboBox_servicios.setObjectName(u"comboBox_servicios")
        self.comboBox_servicios.setGeometry(QRect(88, 10, 91, 21))
        self.comboBox_servicios.setIconSize(QSize(30, 30))
        self.toolButton_ver = QToolButton(self.background_frame)
        self.toolButton_ver.setObjectName(u"toolButton_ver")
        self.toolButton_ver.setGeometry(QRect(200, 10, 31, 22))
        self.toolButton_ver.setAutoFillBackground(False)
        self.toolButton_ver.setStyleSheet(u"background:rgb(170, 0, 0)")
        icon = QIcon()
        icon.addFile(u"./assets/icon/view.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_ver.setIcon(icon)
        self.toolButton_vereliminar2 = QToolButton(self.background_frame)
        self.toolButton_vereliminar2.setObjectName(u"toolButton_vereliminar2")
        self.toolButton_vereliminar2.setGeometry(QRect(240, 10, 31, 22))
        self.toolButton_vereliminar2.setAutoFillBackground(False)
        self.toolButton_vereliminar2.setStyleSheet(u"background:rgb(170, 0, 0)")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_vereliminar2.setIcon(icon1)
        self.frame_encabezado = QFrame(Form_servicios)
        self.frame_encabezado.setObjectName(u"frame_encabezado")
        self.frame_encabezado.setGeometry(QRect(-10, 0, 641, 31))
        self.frame_encabezado.setMaximumSize(QSize(641, 31))
        self.frame_encabezado.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.frame_encabezado.setFrameShape(QFrame.StyledPanel)
        self.frame_encabezado.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_encabezado)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 161, 16))
        self.label.setStyleSheet(u"color:white;")
        self.pushButton_3 = QPushButton(self.frame_encabezado)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(580, 30, 31, 31))
        self.frame_2 = QFrame(self.frame_encabezado)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(509, 10, 121, 21))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.toolButton_CloseP = QToolButton(self.frame_2)
        self.toolButton_CloseP.setObjectName(u"toolButton_CloseP")
        self.toolButton_CloseP.setGeometry(QRect(90, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icon/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_CloseP.setIcon(icon2)
        self.toolButton_MaxiP = QToolButton(self.frame_2)
        self.toolButton_MaxiP.setObjectName(u"toolButton_MaxiP")
        self.toolButton_MaxiP.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icon/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_MaxiP.setIcon(icon3)
        self.toolButton_MiniP = QToolButton(self.frame_2)
        self.toolButton_MiniP.setObjectName(u"toolButton_MiniP")
        self.toolButton_MiniP.setGeometry(QRect(30, 0, 22, 22))
        icon4 = QIcon()
        icon4.addFile(u"./assets/icon/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_MiniP.setIcon(icon4)
        self.toolButton_restaure = QToolButton(self.frame_2)
        self.toolButton_restaure.setObjectName(u"toolButton_restaure")
        self.toolButton_restaure.setGeometry(QRect(60, 0, 22, 22))
        icon5 = QIcon()
        icon5.addFile(u"./assets/icon/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_restaure.setIcon(icon5)
        self.toolButton_restaure.raise_()
        self.toolButton_CloseP.raise_()
        self.toolButton_MaxiP.raise_()
        self.toolButton_MiniP.raise_()

        self.retranslateUi(Form_servicios)

        QMetaObject.connectSlotsByName(Form_servicios)
    # setupUi

    def retranslateUi(self, Form_servicios):
        Form_servicios.setWindowTitle(QCoreApplication.translate("Form_servicios", u"Form", None))
        self.label_Servicios.setText(QCoreApplication.translate("Form_servicios", u"Servicios", None))
        self.toolButton_ver.setText(QCoreApplication.translate("Form_servicios", u"...", None))
        self.toolButton_vereliminar2.setText(QCoreApplication.translate("Form_servicios", u"...", None))
        self.label.setText(QCoreApplication.translate("Form_servicios", u"Servicios", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form_servicios", u"PushButton", None))
        self.toolButton_CloseP.setText(QCoreApplication.translate("Form_servicios", u"...", None))
        self.toolButton_MaxiP.setText(QCoreApplication.translate("Form_servicios", u"...", None))
        self.toolButton_MiniP.setText(QCoreApplication.translate("Form_servicios", u"...", None))
        self.toolButton_restaure.setText(QCoreApplication.translate("Form_servicios", u"...", None))
    # retranslateUi

