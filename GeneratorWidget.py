from PySide6 import QtCore, QtWidgets, QtGui
from OptionsWidget import OptionsWidget

class GeneratorWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.monospace_font = QtGui.QFont("nonexistant") # Needs a Font which does not exist - https://forum.qt.io/post/208937
        self.monospace_font.setStyleHint(QtGui.QFont.Monospace)
        
        self.password_textbox = QtWidgets.QLineEdit()
        self.password_textbox.setReadOnly(True)
        self.password_textbox.setFont(self.monospace_font)
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_textbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.options_widget = OptionsWidget(self)
 
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.password_textbox)
        self.layout.addWidget(self.options_widget)