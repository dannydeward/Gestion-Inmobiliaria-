# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_InqPro.ui'
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
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Form_Inqui_Propi(object):
    def setupUi(self, Form_Inqui_Propi):
        if not Form_Inqui_Propi.objectName():
            Form_Inqui_Propi.setObjectName(u"Form_Inqui_Propi")
        Form_Inqui_Propi.resize(640, 449)
        Form_Inqui_Propi.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"")
        self.toolButton_agreInqpropi = QToolButton(Form_Inqui_Propi)
        self.toolButton_agreInqpropi.setObjectName(u"toolButton_agreInqpropi")
        self.toolButton_agreInqpropi.setGeometry(QRect(0, 30, 111, 71))
        self.toolButton_agreInqpropi.setStyleSheet(u"color: rgb(170,0,0);\n"
"")
        self.toolButton_Ctacte_In = QToolButton(Form_Inqui_Propi)
        self.toolButton_Ctacte_In.setObjectName(u"toolButton_Ctacte_In")
        self.toolButton_Ctacte_In.setGeometry(QRect(0, 320, 111, 61))
        self.toolButton_Ctacte_In.setStyleSheet(u"color: rgb(170,0,0);")
        self.toolButton_edit_Inqui = QToolButton(Form_Inqui_Propi)
        self.toolButton_edit_Inqui.setObjectName(u"toolButton_edit_Inqui")
        self.toolButton_edit_Inqui.setGeometry(QRect(0, 110, 111, 61))
        self.toolButton_edit_Inqui.setStyleSheet(u"color: rgb(170,0,0);")
        self.toolButton_Ctacte_Prop = QToolButton(Form_Inqui_Propi)
        self.toolButton_Ctacte_Prop.setObjectName(u"toolButton_Ctacte_Prop")
        self.toolButton_Ctacte_Prop.setGeometry(QRect(0, 250, 111, 61))
        self.toolButton_Ctacte_Prop.setStyleSheet(u"color: rgb(170,0,0);")
        self.toolButton_edit_prop = QToolButton(Form_Inqui_Propi)
        self.toolButton_edit_prop.setObjectName(u"toolButton_edit_prop")
        self.toolButton_edit_prop.setGeometry(QRect(0, 180, 111, 61))
        self.toolButton_edit_prop.setStyleSheet(u"color: rgb(170,0,0);")
        self.toolButton_Borrar_InqProp = QToolButton(Form_Inqui_Propi)
        self.toolButton_Borrar_InqProp.setObjectName(u"toolButton_Borrar_InqProp")
        self.toolButton_Borrar_InqProp.setGeometry(QRect(0, 390, 111, 61))
        self.toolButton_Borrar_InqProp.setStyleSheet(u"color: rgb(170,0,0);")
        self.line = QFrame(Form_Inqui_Propi)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(103, 30, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget = QWidget(Form_Inqui_Propi)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 30, 531, 421))
        self.verticalLayout_inquipropi = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_inquipropi.setObjectName(u"verticalLayout_inquipropi")
        self.verticalLayout_inquipropi.setContentsMargins(0, 0, 0, 0)
        self.frame_InqPropi = QFrame(self.verticalLayoutWidget)
        self.frame_InqPropi.setObjectName(u"frame_InqPropi")
        self.frame_InqPropi.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"")
        self.frame_InqPropi.setFrameShape(QFrame.StyledPanel)
        self.frame_InqPropi.setFrameShadow(QFrame.Raised)

        self.verticalLayout_inquipropi.addWidget(self.frame_InqPropi)

        self.frame_encabezado = QFrame(Form_Inqui_Propi)
        self.frame_encabezado.setObjectName(u"frame_encabezado")
        self.frame_encabezado.setGeometry(QRect(0, 0, 641, 31))
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
        self.background_frame = QFrame(Form_Inqui_Propi)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setGeometry(QRect(0, 30, 641, 421))
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.background_frame.raise_()
        self.toolButton_agreInqpropi.raise_()
        self.toolButton_Ctacte_In.raise_()
        self.toolButton_edit_Inqui.raise_()
        self.toolButton_Ctacte_Prop.raise_()
        self.toolButton_edit_prop.raise_()
        self.toolButton_Borrar_InqProp.raise_()
        self.line.raise_()
        self.verticalLayoutWidget.raise_()
        self.frame_encabezado.raise_()

        self.retranslateUi(Form_Inqui_Propi)

        QMetaObject.connectSlotsByName(Form_Inqui_Propi)
    # setupUi

    def retranslateUi(self, Form_Inqui_Propi):
        Form_Inqui_Propi.setWindowTitle(QCoreApplication.translate("Form_Inqui_Propi", u"Form", None))
        self.toolButton_agreInqpropi.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Agregar Nuevo", None))
        self.toolButton_Ctacte_In.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Cta cte Inquilino", None))
        self.toolButton_edit_Inqui.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Editar Propietario", None))
        self.toolButton_Ctacte_Prop.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Cta cte propietario", None))
        self.toolButton_edit_prop.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Editar Inquilino ", None))
        self.toolButton_Borrar_InqProp.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Borrar", None))
        self.label.setText(QCoreApplication.translate("Form_Inqui_Propi", u"Inquilino/propietario", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form_Inqui_Propi", u"PushButton", None))
        self.toolButton_CloseP.setText(QCoreApplication.translate("Form_Inqui_Propi", u"...", None))
        self.toolButton_MaxiP.setText(QCoreApplication.translate("Form_Inqui_Propi", u"...", None))
        self.toolButton_MiniP.setText(QCoreApplication.translate("Form_Inqui_Propi", u"...", None))
        self.toolButton_restaure.setText(QCoreApplication.translate("Form_Inqui_Propi", u"...", None))
    # retranslateUi

