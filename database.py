import sqlite3

class Database:
    def __init__(self):
       self.connection()

    def create_database(self):
        try:
            self.cursor.execute("""
              CREATE TABLE englishWords (
                    id_ENG               INTEGER        PRIMARY KEY AUTOINCREMENT UNIQUE,
                    word                 VARCHAR (80)  NOT NULL,
                    description          VARCHAR (1024),
                    category             VARCHAR (128),
                    example              VARCHAR (512),
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

            self.cursor.execute("""
              CREATE TABLE polishWords (
                    id_PL                INTEGER        PRIMARY KEY AUTOINCREMENT UNIQUE,
                    word                 VARCHAR (80)  NOT NULL,
                    description          VARCHAR (1024),
                    category             VARCHAR (128),
                    example              VARCHAR (512),
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
            self.cursor.execute("""
                            CREATE TABLE PL_ENG(
                              id_PL INTEGER NOT NULL,
                              id_ENG INTEGER NOT NULL,
                              PRIMARY KEY (id_PL, id_ENG)
                            );
                                """)
            self.db.close()
        except sqlite3.OperationalError:
            print ("Table exist")


    def connection(self):
        self.db = sqlite3.connect("englishHelper.db")
        self.cursor = self.db.cursor()



#k.create_database()

