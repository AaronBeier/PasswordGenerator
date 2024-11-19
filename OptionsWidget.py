import random
import secrets
import string
from PySide6 import QtCore, QtWidgets, QtGui

class OptionsWidget(QtWidgets.QWidget):
    def __init__(self, generator):
        super().__init__()

        self.generator = generator
        self.clipboard = QtGui.QClipboard()

        self.letters_checkbox = QtWidgets.QCheckBox("Use Letters")
        self.letters_checkbox.setCheckState(QtCore.Qt.Checked)

        self.numbers_checkbox = QtWidgets.QCheckBox("Use Numbers")
        self.numbers_checkbox.setCheckState(QtCore.Qt.Checked)

        self.symbols_checkbox = QtWidgets.QCheckBox("Use Symbols")
        self.symbols_checkbox.setCheckState(QtCore.Qt.Unchecked)

        self.hide_checkbox = QtWidgets.QCheckBox("Hide Password")
        self.hide_checkbox.setCheckState(QtCore.Qt.Checked)

        self.length_spinbox = QtWidgets.QSpinBox()
        self.length_spinbox.setMinimum(8)
        self.length_spinbox.setMaximum(96)
        self.length_spinbox.setValue(16)

        self.generate_button = QtWidgets.QPushButton("Generate")        
        self.copy_button = QtWidgets.QPushButton("Copy")

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.letters_checkbox)
        self.layout.addWidget(self.numbers_checkbox)
        self.layout.addWidget(self.symbols_checkbox)
        self.layout.addWidget(self.hide_checkbox)
        self.layout.addWidget(self.length_spinbox)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.copy_button)
        
        self.hide_checkbox.stateChanged.connect(self.toggle_password_view)
        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_password)
        
    @QtCore.Slot()
    def toggle_password_view(self):
        self.generator.password_textbox.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password if self.hide_checkbox.isChecked() else QtWidgets.QLineEdit.EchoMode.Normal)

    @QtCore.Slot()
    def generate_password(self):
        alphabet = []

        if self.letters_checkbox.isChecked():
            alphabet.extend(list(string.ascii_letters))

        if self.numbers_checkbox.isChecked():
            alphabet.extend(list(string.digits))

        if self.symbols_checkbox.isChecked():
            alphabet.extend(list(string.punctuation))

        if len(alphabet) == 0:
            QtWidgets.QMessageBox.critical(self, "Error", "You have no character set selected")
            return

        password = ''
        for _ in range(self.length_spinbox.value()):
            password += secrets.choice(alphabet)

        self.generator.password_textbox.setText(password)

    @QtCore.Slot()
    def copy_password(self):
        self.clipboard.setText(self.generator.password_textbox.text())