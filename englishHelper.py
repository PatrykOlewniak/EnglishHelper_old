import sys
from PyQt5.QtWidgets import QApplication, QDialog
from mainLayout import Ui_Dialog


class EnglishHelperMainWindow(QDialog):
    def __init__ (self, parent=None):
        super(EnglishHelperMainWindow, self).__init__(parent)
        self.ui_glowne = Ui_Dialog()
        self.ui_glowne.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = EnglishHelperMainWindow()
    form.show()
    #app.setQuitOnLastWindowClosed( False)  # by zamykalo okno w odp kolejnosci, likwiduje "QObject::startTimer: QTimer can only be used with threads started" ... blad
    sys.exit(app.exec_())
