from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

# from src.logger import logger, app_folder

import os

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
        query.exec_("create table tennismen(id int primary key, ""firstname varchar(20), lastname varchar(20))")

        query.exec_("insert into tennismen values(101, 'Andre', 'Agassi')")
        query.exec_("insert into tennismen values(102, 'Novak', 'Djokovic')")
        query.exec_("insert into tennismen values(103, 'Daniil', 'Medvedev')")
        query.exec_("insert into tennismen values(104, 'Andy', 'Murray')")
        query.exec_("insert into tennismen values(105, 'Rafael', 'Nadal')")
        self.logger.debug("DbManager::create_db - Created table of tennismen with initial values")
        self.logger.debug("DbManager::create_db - Exited method")
        return True

    def initialise_model(self, model):
        self.logger.debug("DbManager::initialise_model - Entered method")
        model.setTable('tennismen')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "First name")
        model.setHeaderData(2, Qt.Horizontal, "Last name")
        self.logger.debug("DbManager::initialise_model - Exited method")

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

    def find_row(self, i):
        self.logger.debug("DbManager::add_row - Entered method")
        self.delrow = i.row()
        self.logger.debug("DbManager::add_row - Exited method")

if __name__ == "__main__":
    print('пусто')