# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hashGenerator.ui'
#
# Created: Tue Dec 18 00:25:17 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!
#
# Author:M. Sami GÜRPINAR
#      
from PyQt4 import QtCore, QtGui
import hashlib

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


		
class Generator(object):
    ''' 
    Class including hash genarating methods

    '''
    
    def __init__(self,ui):
        self.ui = ui
    
    def md5(self,text):
        self.hash = hashlib.md5(text).hexdigest()
        self.ui.textEdit.setText(self.hash)
    
    def sha(self,text):
        self.hash = hashlib.sha1(text).hexdigest()
        self.ui.textEdit.setText(self.hash)
    
    def sha224(self,text):
        self.hash = hashlib.sha224(text).hexdigest()
        self.ui.textEdit.setText(self.hash)

    def sha256(self,text):
        self.hash = hashlib.sha256(text).hexdigest()
        self.ui.textEdit.setText(self.hash)

    def sha384(self,text):
        self.hash = hashlib.sha384(text).hexdigest()
        self.ui.textEdit.setText(self.hash)

    def sha512(self,text):
        self.hash = hashlib.sha512(text).hexdigest()
        self.ui.textEdit.setText(self.hash)
    


	
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(280, 338)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(11, 20, 78, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(172, 300, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.clickedButton)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(11, 61, 258, 227))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.generator = Generator(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Hash Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "SHA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "SHA224", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "SHA256", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form", "SHA384", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Form", "SHA512", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Generate", None, QtGui.QApplication.UnicodeUTF8))

    def clickedButton(self):
        if self.comboBox.currentText() == "MD5":
            self.generator.md5(self.lineEdit.text().toUtf8())
        elif self.comboBox.currentText() == "SHA":
            self.generator.sha(self.lineEdit.text().toUtf8())
        elif self.comboBox.currentText() == "SHA224":
            self.generator.sha224(self.lineEdit.text().toUtf8())
        elif self.comboBox.currentText() == "SHA256":
            self.generator.sha256(self.lineEdit.text().toUtf8())
        elif self.comboBox.currentText() == "SHA384":
            self.generator.sha384(self.lineEdit.text().toUtf8())
        else: 
            self.generator.sha512(self.lineEdit.text().toUtf8())
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

