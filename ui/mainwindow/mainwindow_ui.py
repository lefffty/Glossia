# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.10.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QListWidget, QListWidgetItem, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)
from .resources import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(711, 396)
        icon = QIcon()
        icon.addFile(u":/icons/icons/app.png", QSize(),
                     QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 231, 391))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 231, 391))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.appLabel = QLabel(self.verticalLayoutWidget_2)
        self.appLabel.setObjectName(u"appLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.appLabel.setFont(font)
        self.appLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.appLabel)

        self.createVocabBtn = QPushButton(self.verticalLayoutWidget_2)
        self.createVocabBtn.setObjectName(u"createVocabBtn")
        font1 = QFont()
        font1.setPointSize(12)
        self.createVocabBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.createVocabBtn)

        self.exitBtn = QPushButton(self.verticalLayoutWidget_2)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.exitBtn)

        self.vocabsListWidget = QListWidget(self.verticalLayoutWidget_2)
        self.vocabsListWidget.setObjectName(u"vocabsListWidget")
        self.vocabsListWidget.setFont(font1)

        self.verticalLayout_2.addWidget(self.vocabsListWidget)

        self.vocabWidget = QWidget(self.centralwidget)
        self.vocabWidget.setObjectName(u"vocabWidget")
        self.vocabWidget.setEnabled(False)
        self.vocabWidget.setGeometry(QRect(240, 0, 481, 391))
        self.verticalLayoutWidget = QWidget(self.vocabWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 451, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.vocabNameLabel = QLabel(self.verticalLayoutWidget)
        self.vocabNameLabel.setObjectName(u"vocabNameLabel")
        font2 = QFont()
        font2.setPointSize(18)
        self.vocabNameLabel.setFont(font2)
        self.vocabNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vocabNameLabel)

        self.entriesListWidget = QListWidget(self.verticalLayoutWidget)
        self.entriesListWidget.setObjectName(u"entriesListWidget")
        font3 = QFont()
        font3.setPointSize(16)
        self.entriesListWidget.setFont(font3)

        self.verticalLayout.addWidget(self.entriesListWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addRowBtn = QPushButton(self.verticalLayoutWidget)
        self.addRowBtn.setObjectName(u"addRowBtn")
        self.addRowBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.addRowBtn)

        self.deleteRowBtn = QPushButton(self.verticalLayoutWidget)
        self.deleteRowBtn.setObjectName(u"deleteRowBtn")
        self.deleteRowBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.deleteRowBtn)

        self.deleteVocabBtn = QPushButton(self.verticalLayoutWidget)
        self.deleteVocabBtn.setObjectName(u"deleteVocabBtn")
        self.deleteVocabBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.deleteVocabBtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Glossia", None))
        self.appLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Glossia", None))
        self.createVocabBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Create new vocabulary", None))
        self.exitBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Exit", None))
        self.vocabNameLabel.setText("")
        self.addRowBtn.setText(
            QCoreApplication.translate("MainWindow", u"Add", None))
        self.deleteRowBtn.setText(
            QCoreApplication.translate("MainWindow", u"Delete", None))
        self.deleteVocabBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Delete vocabulary", None))
    # retranslateUi
