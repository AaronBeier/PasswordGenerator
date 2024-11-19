import sys
from PySide6 import QtCore, QtWidgets, QtGui
from GeneratorWidget import GeneratorWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    icon = QtGui.QIcon() # TODO: Does not work when exporting as a singular executable
    icon.addFile("icon.png") # Icon from Google Icons

    widget = GeneratorWidget()
    widget.setWindowTitle("Password Generator")
    widget.setWindowIcon(icon)
    widget.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    widget.resize(720, 100)
    widget.show()

    sys.exit(app.exec())