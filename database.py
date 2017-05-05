import sqlite3

class Database:
    @staticmethod
    def create_database():
        try:
            db = sqlite3.connect("englishHelper.db")
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE englishWords (
                    id_ENG               INTEGER        PRIMARY KEY AUTOINCREMENT UNIQUE,
                    word                 VARCHAR (80)  NOT NULL,
                    description          VARCHAR (1024),
                    category             VARCHAR (128),
                    importance           INTEGER (2)    DEFAULT (0),
                    creationDate         DATETIME       DEFAULT ( (DATETIME('now') ) ),
                    lastViewdate         DATETIME,
                    viewcount            INTEGER (4)    DEFAULT (0),
                    correctanswers       INTEGER (4)    DEFAULT (0),
                    mastered             INTEGER (1)    DEFAULT (0),
                    difficult            INTEGER (2)    DEFAULT (1),
                    synonyms             VARCHAR (2056),
                    partofspeech         VARCHAR (256));
                    """)

            cursor.execute("""
                            CREATE TABLE polishWords (
                                id_ENG               INTEGER        PRIMARY KEY AUTOINCREMENT UNIQUE,
                                word                 VARCHAR (80)  NOT NULL,
                                description          VARCHAR (1024),
                                category             VARCHAR (128),
                                importance           INTEGER (2)    DEFAULT (0),
                                creationDate         DATETIME       DEFAULT ( (DATETIME('now') ) ),
                                lastViewdate         DATETIME,
                                viewcount            INTEGER (4)    DEFAULT (0),
                                correctanswers       INTEGER (4)    DEFAULT (0),
                                mastered             INTEGER (1)    DEFAULT (0),
                                difficult            INTEGER (2)    DEFAULT (1),
                                synonyms             VARCHAR (2056),
                                partofspeech         VARCHAR (256));
                                """)
            db.close()
        except sqlite3.OperationalError:
            print ("Table exist")







    def connection(self):
        pass


k = Database()
k.create_database()