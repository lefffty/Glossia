# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 209)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 50, 331, 111))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.wordLabel = QLabel(self.formLayoutWidget)
        self.wordLabel.setObjectName(u"wordLabel")
        font = QFont()
        font.setPointSize(24)
        self.wordLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.wordLabel)

        self.wordLineEdit = QLineEdit(self.formLayoutWidget)
        self.wordLineEdit.setObjectName(u"wordLineEdit")
        self.wordLineEdit.setEnabled(False)
        self.wordLineEdit.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.wordLineEdit)

        self.translationLabel = QLabel(self.formLayoutWidget)
        self.translationLabel.setObjectName(u"translationLabel")
        self.translationLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.translationLabel)

        self.translationLineEdit = QLineEdit(self.formLayoutWidget)
        self.translationLineEdit.setObjectName(u"translationLineEdit")
        self.translationLineEdit.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.translationLineEdit)

        self.formatLabel = QLabel(Dialog)
        self.formatLabel.setObjectName(u"formatLabel")
        self.formatLabel.setGeometry(QRect(90, 10, 211, 41))
        self.formatLabel.setFont(font)
        self.formatLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toNextPairBtn = QPushButton(Dialog)
        self.toNextPairBtn.setObjectName(u"toNextPairBtn")
        self.toNextPairBtn.setGeometry(QRect(30, 170, 161, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.toNextPairBtn.setFont(font1)
        self.toFinishBtn = QPushButton(Dialog)
        self.toFinishBtn.setObjectName(u"toFinishBtn")
        self.toFinishBtn.setEnabled(False)
        self.toFinishBtn.setGeometry(QRect(200, 170, 161, 31))
        self.toFinishBtn.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.wordLabel.setText(QCoreApplication.translate("Dialog", u"Word", None))
        self.wordLineEdit.setText("")
        self.translationLabel.setText(QCoreApplication.translate("Dialog", u"Translation", None))
        self.formatLabel.setText("")
        self.toNextPairBtn.setText(QCoreApplication.translate("Dialog", u"NEXT", None))
        self.toFinishBtn.setText(QCoreApplication.translate("Dialog", u"FINISH", None))
    # retranslateUi

