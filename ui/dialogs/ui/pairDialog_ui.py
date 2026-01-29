# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pairDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(252, 108)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 70, 161, 31))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 221, 51))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.wordLabel = QLabel(self.formLayoutWidget)
        self.wordLabel.setObjectName(u"wordLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.wordLabel)

        self.wordLineEdit = QLineEdit(self.formLayoutWidget)
        self.wordLineEdit.setObjectName(u"wordLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.wordLineEdit)

        self.translationLabel = QLabel(self.formLayoutWidget)
        self.translationLabel.setObjectName(u"translationLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.translationLabel)

        self.translationLineEdit = QLineEdit(self.formLayoutWidget)
        self.translationLineEdit.setObjectName(u"translationLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.translationLineEdit)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.wordLabel.setText(QCoreApplication.translate("Dialog", u"word", None))
        self.translationLabel.setText(QCoreApplication.translate("Dialog", u"translation", None))
    # retranslateUi

