import sys
from PyQt5.QtWidgets import QApplication, QDialog
from mainLayout import Ui_Dialog
import sqlite3
from database import Database



class EnglishHelper(QDialog):

    def __init__ (self, parent=None):
        super(EnglishHelper, self).__init__(parent)
        #self.ui_glowne = Ui_Dialog()
        #self.ui_glowne.setupUi(self)
        EHdatabase=Database()
        EHdatabase.connection()
        self.button_connections()


    def insert_to_english_Words (self):
        """JUST TESTING"""
        self.cursor.execute("INSERT INTO englishWords "
                            "(word, description, category, example,importance, "
                            "difficult, synonyms, partofspeech ) "
                            "VALUES (?, ?, ?, ?, ?, ? , ?, ?)", (19, 19, 1, 91, 19, 19, 1, 1))

        self.db.commit()



    def button_connections(self):
        self.ui_glowne.shuffleButton.clicked.connect(self.shufle_word_from_DB)
        self.ui_glowne.checkButton.clicked.connect(self.checked_pressed_func)
        self.ui_glowne.pushButton.clicked.connect(self.add_button_pressed_func)

    def shufle_word_from_DB(self):
        self.ui_glowne.kategoriaComboBox_2.addItem("kkk")
        category = self.ui_glowne.kategoriaComboBox_2.currentText()
        print(category)

    def checked_pressed_func(self):
        print("CHECKED PRESSED")
        self.insert_to_english_Words()

    def add_button_pressed_func(self):
        print("BUTTON ADD PRESSED")

    def comboBoxes_get_values(self):
        self.cursor.execute("SELECT category from englishWords")
        self.db.commit()
        k=self.cursor.fetchall()
        print(k)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = EnglishHelper()
    form.show()
    sys.exit(app.exec_())
