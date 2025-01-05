#!/usr/bin/env python3

# MIT License

# Copyright (c) 2023-2024 Achille MARTIN

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

from src.logger import logger

import os

# Database Manager class
class DbManager():

    # Ensure one connection to a database per application
    db_connected = None

    def __init__(self, db_type, db_name, db_folder):

        self.db_type = db_type
        # Include the extension in the name (e.g. `test.db`)
        self.db_name = db_name
        self.db_folder = db_folder
        self.delrow = -1

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

        # Initial database creation
        if not os.path.exists(os.path.join(self.db_folder, self.db_name)):
            self.create_db()

        logger.debug("DbManager::__init__ - Database Manager for "
                + str(os.path.join(self.db_folder, self.db_name))
                + " instantiated"
                )

        logger.debug("DbManager::__init__ - Exited method")

    def __del__(self):
        logger.debug("DbManager::__del__ - Entered method")
        self.db_connected.close()
        logger.debug("DbManager::__del__ - Database Manager for "
                + str(os.path.join(self.db_folder, self.db_name))
                + " deleted"
                )
        logger.debug("DbManager::__del__ - Exited method")

    def create_db(self):
        logger.debug("DbManager::create_db - Entered method")
        if not self.db_connected.open():
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Error in Database Creation")
          retval = msg.exec_()
          logger.exception("DbManager::create_db - Error in Database Creation")
          return False

        query = QSqlQuery()
        query.exec_("create table tennismen(id int primary key, ""firstname varchar(20), lastname varchar(20))")

        query.exec_("insert into tennismen values(101, 'Andre', 'Agassi')")
        query.exec_("insert into tennismen values(102, 'Novak', 'Djokovic')")
        query.exec_("insert into tennismen values(103, 'Daniil', 'Medvedev')")
        query.exec_("insert into tennismen values(104, 'Andy', 'Murray')")
        query.exec_("insert into tennismen values(105, 'Rafael', 'Nadal')")
        logger.debug("DbManager::create_db - Created table of tennismen with initial values")
        logger.debug("DbManager::create_db - Exited method")
        return True

    def initialise_model(self, model):
        logger.debug("DbManager::initialise_model - Entered method")
        model.setTable('tennismen')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "First name")
        model.setHeaderData(2, Qt.Horizontal, "Last name")
        logger.debug("DbManager::initialise_model - Exited method")

    def create_view(self, title, model):
        logger.debug("DbManager::create_view - Entered method")
        view = QTableView()
        view.setModel(model)
        view.setWindowTitle(title)
        logger.debug("DbManager::create_view - Exited method")
        return view

    def add_row(self, model):
        logger.debug("DbManager::add_row - Entered method")
        # print ("Model row number: " + str(model.rowCount()))
        ret = model.insertRows(model.rowCount(), 1)
        # print ("Model insert state: " + str(ret))
        logger.debug("DbManager::add_row - Exited method")

    def find_row(self, i):
        logger.debug("DbManager::add_row - Entered method")
        self.delrow = i.row()
        logger.debug("DbManager::add_row - Exited method")


if __name__ == "__main__":
    print('пусто')