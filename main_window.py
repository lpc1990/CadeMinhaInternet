# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fr_status_da_internet = QFrame(self.centralwidget)
        self.fr_status_da_internet.setObjectName(u"fr_status_da_internet")
        self.fr_status_da_internet.setGeometry(QRect(60, 10, 236, 150))
        self.fr_status_da_internet.setFrameShape(QFrame.StyledPanel)
        self.fr_status_da_internet.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_status_da_internet)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_status_da_internet = QLabel(self.fr_status_da_internet)
        self.lb_status_da_internet.setObjectName(u"lb_status_da_internet")

        self.verticalLayout.addWidget(self.lb_status_da_internet)

        self.img_status_da_internet = QLabel(self.fr_status_da_internet)
        self.img_status_da_internet.setObjectName(u"img_status_da_internet")
        self.img_status_da_internet.setPixmap(QPixmap(u"images/sinal_verde.png"))
        self.img_status_da_internet.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.img_status_da_internet)

        self.lb_online_offline = QLabel(self.fr_status_da_internet)
        self.lb_online_offline.setObjectName(u"lb_online_offline")

        self.verticalLayout.addWidget(self.lb_online_offline)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.btn_monitora_internet = QPushButton(self.fr_status_da_internet)
        self.btn_monitora_internet.setObjectName(u"btn_monitora_internet")

        self.verticalLayout_3.addWidget(self.btn_monitora_internet)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 160, 341, 51))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 230, 311, 27))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_escolher_servidor = QLabel(self.layoutWidget)
        self.lb_escolher_servidor.setObjectName(u"lb_escolher_servidor")

        self.horizontalLayout_2.addWidget(self.lb_escolher_servidor)

        self.btn_selecionar_servidor = QPushButton(self.layoutWidget)
        self.btn_selecionar_servidor.setObjectName(u"btn_selecionar_servidor")

        self.horizontalLayout_2.addWidget(self.btn_selecionar_servidor)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(-10, 260, 381, 25))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.label_5)

        self.cb_servidores = QComboBox(self.layoutWidget1)
        self.cb_servidores.setObjectName(u"cb_servidores")

        self.horizontalLayout_9.addWidget(self.cb_servidores)

        self.btn_testar_internet_servidor_selecionado = QPushButton(self.layoutWidget1)
        self.btn_testar_internet_servidor_selecionado.setObjectName(u"btn_testar_internet_servidor_selecionado")
        self.btn_testar_internet_servidor_selecionado.setMinimumSize(QSize(0, 0))
        self.btn_testar_internet_servidor_selecionado.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_testar_internet_servidor_selecionado)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.label_6)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 290, 361, 151))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(2, 16777215))

        self.horizontalLayout_10.addWidget(self.label_7)

        self.frame = QFrame(self.layoutWidget2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget3 = QWidget(self.frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 10, 321, 136))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_download = QLabel(self.layoutWidget3)
        self.lb_download.setObjectName(u"lb_download")

        self.horizontalLayout_3.addWidget(self.lb_download)

        self.text_download = QLineEdit(self.layoutWidget3)
        self.text_download.setObjectName(u"text_download")
        self.text_download.setMaximumSize(QSize(240, 16777215))
        self.text_download.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.text_download)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_download_2 = QLabel(self.layoutWidget3)
        self.lb_download_2.setObjectName(u"lb_download_2")
        self.lb_download_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_download_2)

        self.text_upload = QLineEdit(self.layoutWidget3)
        self.text_upload.setObjectName(u"text_upload")
        self.text_upload.setMaximumSize(QSize(240, 16777215))
        self.text_upload.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_upload.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.text_upload)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_download_3 = QLabel(self.layoutWidget3)
        self.lb_download_3.setObjectName(u"lb_download_3")

        self.horizontalLayout_5.addWidget(self.lb_download_3)

        self.text_ping = QLineEdit(self.layoutWidget3)
        self.text_ping.setObjectName(u"text_ping")
        self.text_ping.setMaximumSize(QSize(240, 16777215))
        self.text_ping.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.text_ping)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_download_4 = QLabel(self.layoutWidget3)
        self.lb_download_4.setObjectName(u"lb_download_4")

        self.horizontalLayout_6.addWidget(self.lb_download_4)

        self.text_servidor = QLineEdit(self.layoutWidget3)
        self.text_servidor.setObjectName(u"text_servidor")
        self.text_servidor.setMaximumSize(QSize(240, 16777215))
        self.text_servidor.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.text_servidor)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_download_5 = QLabel(self.layoutWidget3)
        self.lb_download_5.setObjectName(u"lb_download_5")

        self.horizontalLayout_7.addWidget(self.lb_download_5)

        self.text_operadora = QLineEdit(self.layoutWidget3)
        self.text_operadora.setObjectName(u"text_operadora")
        self.text_operadora.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_7.addWidget(self.text_operadora)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_10.addWidget(self.frame)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(2, 16777215))

        self.horizontalLayout_10.addWidget(self.label_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_status_da_internet.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Status da internet</span></p></body></html>", None))
        self.img_status_da_internet.setText("")
        self.lb_online_offline.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Online</span></p></body></html>", None))
        self.btn_monitora_internet.setText(QCoreApplication.translate("MainWindow", u"Monitorar Internet", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Teste de Velocidade</span></p></body></html>", None))
        self.label_3.setText("")
        self.lb_escolher_servidor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Escolher Servidor?</span></p></body></html>", None))
        self.btn_selecionar_servidor.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.btn_testar_internet_servidor_selecionado.setText(QCoreApplication.translate("MainWindow", u"Testar", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.lb_download.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Download:</span></p></body></html>", None))
        self.lb_download_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Upload:</span></p></body></html>", None))
        self.lb_download_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ping:</span></p></body></html>", None))
        self.lb_download_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Servidor:</span></p></body></html>", None))
        self.lb_download_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Operadora:</span></p></body></html>", None))
        self.label_8.setText("")
    # retranslateUi

