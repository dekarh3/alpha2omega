from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

# from src.logger import logger, app_folder

import os
try:
    from src.hide import SOULS, THEMES, UNIT_TYPES, NOTES, SUBJECTS, MEASURES, REFS
except ImportError:
    SOULS = []
    THEMES = []
    UNIT_TYPES = []
    NOTES = []
    SUBJECTS = []
    MEASURES = []
    REFS = []

class DbManager():

    db_connected = None

    def __init__(self, db_type, db_name, db_folder, logger):
        self.db_type = db_type
        # Include the extension in the name (e.g. `test.db`)
        self.db_name = db_name
        self.db_folder = db_folder
        self.logger = logger
        self.delrow = -1
        self.logger = logger

        if DbManager.db_connected is None:
            try:
                DbManager.db_connected = QSqlDatabase.addDatabase(self.db_type)
                DbManager.db_connected.setDatabaseName(os.path.join(self.db_folder, self.db_name))
            except Exception as error:
                logger.exception("DbManager::__init__ - Error: Connection not established - " + str(error))
            else:
                logger.debug("DbManager::__init__ - Connection established for "
                        + str(self.db_name)
                        + " of type "
                        + str(self.db_type)
                        + " at location "
                        + str(os.path.join(self.db_folder, self.db_name))
                        )

        if not os.path.exists(os.path.join(self.db_folder, self.db_name)):
            self.create_db()

        logger.debug("DbManager::__init__ - Database Manager for "
                + str(os.path.join(self.db_folder, self.db_name))
                + " instantiated"
                )

        logger.debug("DbManager::__init__ - Exited method")

    def __del__(self):
        self.logger.debug("DbManager::__del__ - Entered method")
        self.db_connected.close()
        self.logger.debug("DbManager::__del__ - Database Manager for "
                + str(os.path.join(self.db_folder, self.db_name))
                + " deleted"
                )
        self.logger.debug("DbManager::__del__ - Exited method")

    def create_db(self):
        self.logger.debug("DbManager::create_db - Entered method")
        if not self.db_connected.open():
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Error in Database Creation")
          retval = msg.exec_()
          self.logger.exception("DbManager::create_db - Error in Database Creation")
          return False

        query = QSqlQuery()
        query.exec_(
            'CREATE TABLE "souls" ('
                '"id"           INTEGER NOT NULL UNIQUE,'
                '"name"         TEXT NOT NULL,'
                '"about"        TEXT,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                ')'
            ')'
        )
        for soul in SOULS:
            query.exec_(soul)

        query.exec_(
            'CREATE TABLE "themes" ('
                '"id"           INTEGER NOT NULL UNIQUE,'
                '"name"         TEXT NOT NULL,'
                '"about"        TEXT,'
                '"nameIndex"    INTEGER NOT NULL DEFAULT 0,'
                '"date"         INTEGER NOT NULL,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                '"oneString"    TEXT GENERATED ALWAYS AS (IIF ('
                    'nameIndex == 0,'
                    'name || \' (\' || about || \')\','
                    'name || \'-\' || nameIndex || \' (\' || about || \')\''
                ')),'
                '"nameAndIndex" TEXT GENERATED ALWAYS AS (IIF ('
                    'nameIndex == 0,'
                    'name,'
                    'name || \'-\' || nameIndex'
                ')),'            
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                ')'
            ')'
        )
        for theme in THEMES:
            query.exec_(theme)

        query.exec_(
            'CREATE TABLE "unitTypes" ('
                '"id"	        INTEGER NOT NULL UNIQUE,'
                '"name"	        TEXT NOT NULL,'
                '"about"	    TEXT,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                ')'
            ')'
        )
        for unit_type in UNIT_TYPES:
            query.exec_(unit_type)

        query.exec_(
            'CREATE TABLE "notes" ('
                '"id"	        INTEGER NOT NULL UNIQUE,'
                '"name"	        TEXT NOT NULL,'
                '"about"        TEXT,'
                '"nameIndex"	INTEGER NOT NULL DEFAULT 0,'
                '"date"	        INTEGER NOT NULL,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                '"oneString"    TEXT GENERATED ALWAYS AS (IIF ('
                    'nameIndex == 0,'
                    'name || \' (\' || about || \')\','
                    'name || \'-\' || nameIndex || \' (\' || about || \')\''
                ')),'
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                ')'
            ')'
        )
        for note in NOTES:
            query.exec_(note)

        query.exec_(
            'CREATE TABLE "subjects" ('
                '"id"	        INTEGER NOT NULL UNIQUE,'
                '"name"	        TEXT NOT NULL,'
                '"about"	    TEXT,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                ')'
            ')'
        )
        for subject in SUBJECTS:
            query.exec_(subject)

        query.exec_(
            'CREATE TABLE "measures" ('
                '"id"	        INTEGER NOT NULL UNIQUE,'
                '"soulId"	    INTEGER NOT NULL,'
                '"themeId"	    INTEGER NOT NULL,'
                '"date"	        INTEGER NOT NULL,'
                '"value"	    REAL NOT NULL,'
                '"unitTypeId"	INTEGER NOT NULL,'
                '"sign"	        INTEGER NOT NULL,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                '),'
                'FOREIGN KEY("soulId") REFERENCES "souls"("id"),'
                'FOREIGN KEY("themeId") REFERENCES "themes"("id"),'
                'FOREIGN KEY("unitTypeId") REFERENCES "unitTypes"("id")'
            ')'
        )
        for measure in MEASURES:
            query.exec_(measure)

        query.exec_(
            'CREATE TABLE "refs" ('
                '"id"           INTEGER NOT NULL UNIQUE,'
                '"subjectId"	INTEGER NOT NULL,'
                '"noteId"	    INTEGER NOT NULL,'
                '"date"	        INTEGER NOT NULL,'
                '"value"	    REAL NOT NULL,'
                '"unitTypeId"	INTEGER NOT NULL,'
                '"sign"	        INTEGER NOT NULL,'
                '"deleted"	    INTEGER NOT NULL DEFAULT 0,'
                'PRIMARY KEY('
                    '"id"       AUTOINCREMENT'
                '),'
                'FOREIGN KEY("subjectId") REFERENCES "subjects"("id"),'
                'FOREIGN KEY("unitTypeId") REFERENCES "unitTypes"("id"),'
                'FOREIGN KEY("noteId") REFERENCES "notes"("id")'
            ')'
        )
        for ref in REFS:
            query.exec_(ref)

        self.logger.debug("DbManager::create_db - Created table of tennismen with initial values")
        self.logger.debug("DbManager::create_db - Exited method")
        return True

    def create_view(self, title, model):
        self.logger.debug("DbManager::create_view - Entered method")
        view = QTableView()
        view.setModel(model)
        view.setWindowTitle(title)
        self.logger.debug("DbManager::create_view - Exited method")
        return view

    def add_row(self, model):
        self.logger.debug("DbManager::add_row - Entered method")
        # print ("Model row number: " + str(model.rowCount()))
        ret = model.insertRows(model.rowCount(), 1)
        # print ("Model insert state: " + str(ret))
        self.logger.debug("DbManager::add_row - Exited method")

if __name__ == "__main__":
    print('пусто')