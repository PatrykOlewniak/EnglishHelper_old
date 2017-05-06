import sys
from PyQt5.QtWidgets import QApplication, QDialog
from mainLayout import Ui_Dialog




app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
sys.exit(app.exec_())