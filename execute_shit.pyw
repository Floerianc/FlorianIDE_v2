import sys
from PyQt5 import QtWidgets
from GUI_v4 import *

class Application(Ui_PythonIDE):
    def __init__(self, Form) -> None:
        self.setupUi(Form)
        # hotkeys
        self.shortcut = QShortcut(QKeySequence("Ctrl+O"), Form)
        self.shortcut.activated.connect(self.open_file)

        self.quick_save_shortcut = QShortcut(QKeySequence("Ctrl+S"), Form)
        self.quick_save_shortcut.activated.connect(self.quick_save)

        self.save_shortcut = QShortcut(QKeySequence("Shift+Ctrl+S"), Form)
        self.save_shortcut.activated.connect(self.save_input)

        self.exit_shortcut = QShortcut(QKeySequence("Esc"), Form)
        self.exit_shortcut.activated.connect(self.exit)

        self.exit_and_save_shortcut = QShortcut(QKeySequence("Shift+Esc"), Form)
        self.exit_and_save_shortcut.activated.connect(self.exit_and_save)

        self.run_shortcut = QShortcut(QKeySequence("F5"), Form)
        self.run_shortcut.activated.connect(self.run_input)

        self.run_in_file_shortcut = QShortcut(QKeySequence("Shift+F5"), Form)
        self.run_in_file_shortcut.activated.connect(self.run_input_in_file)

        self.about_shortcut = QShortcut(QKeySequence("F9"), Form)
        self.about_shortcut.activated.connect(self.about_window)
        self.actionAbout.triggered.connect(self.about_window)

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QMainWindow()
ui = Application(Form)
Form.show()
app.exec()