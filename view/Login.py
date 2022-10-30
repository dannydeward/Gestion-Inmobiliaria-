# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(391, 163)
        Form.setMaximumSize(QSize(400, 300))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 401, 171))
        self.frame.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 40, 49, 16))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 70, 51, 16))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 40, 113, 22))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 70, 113, 22))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 110, 75, 24))
        self.pushButton.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color:rgb(170,0,0);")
        self.frame_encabezado = QFrame(self.frame)
        self.frame_encabezado.setObjectName(u"frame_encabezado")
        self.frame_encabezado.setGeometry(QRect(0, 0, 391, 31))
        self.frame_encabezado.setMaximumSize(QSize(16777211, 16777215))
        self.frame_encabezado.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.frame_encabezado.setFrameShape(QFrame.StyledPanel)
        self.frame_encabezado.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_encabezado)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 51, 16))
        self.label_3.setStyleSheet(u"color:white;")
        self.pushButton_3 = QPushButton(self.frame_encabezado)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(580, 30, 31, 31))
        self.frame_2 = QFrame(self.frame_encabezado)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(270, 10, 121, 21))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.toolButton_CloseP = QToolButton(self.frame_2)
        self.toolButton_CloseP.setObjectName(u"toolButton_CloseP")
        self.toolButton_CloseP.setGeometry(QRect(90, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"../assets/icon/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_CloseP.setIcon(icon)
        self.toolButton_MaxiP = QToolButton(self.frame_2)
        self.toolButton_MaxiP.setObjectName(u"toolButton_MaxiP")
        self.toolButton_MaxiP.setGeometry(QRect(60, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"../assets/icon/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_MaxiP.setIcon(icon1)
        self.toolButton_MiniP = QToolButton(self.frame_2)
        self.toolButton_MiniP.setObjectName(u"toolButton_MiniP")
        self.toolButton_MiniP.setGeometry(QRect(30, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"../assets/icon/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_MiniP.setIcon(icon2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pasword", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Entar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.toolButton_CloseP.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_MaxiP.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_MiniP.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi

