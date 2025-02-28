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

from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QDialog, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtSql import QSqlTableModel
from PyQt5.uic import loadUiType

from io import StringIO

from src.DbManager import DbManager
from src.logger import logger, app_folder
from src.uis import ThemeTable_ui

ThemeTable_form, ThemeTable_base = loadUiType(StringIO(ThemeTable_ui))

class ThemeTable(ThemeTable_form, ThemeTable_base):
    def __init__(self):
        logger.debug("ThemeTable::__init__ - Entered method")
        logger.debug("Definition:: widget_main_window_ui created")
        super(ThemeTable_base, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("ThemeTable - Example simple pyqt5 app")

        # Instantiate the database manager
        db_manager = DbManager('QSQLITE', 'sportsdatabase.db', app_folder)
        table_model = QSqlTableModel()
        db_manager.initialise_model(table_model)

        # view_primary = db_manager.create_view("Table Model (View Primary)", table_model)
        self.view_primary.setModel(table_model)
        self.view_primary.clicked.connect(db_manager.find_row)

        # Create a window to display the database viewer and modifier
        # dlg = QDialog(self)
        # layout_database_window = QVBoxLayout()
        # layout_database_window.addWidget(view_primary)

        # Add buttons to the window to interact with the database viewer and modifier
        # button_add_row = QPushButton("Add a row")
        self.button_add_row.clicked.connect(lambda: db_manager.add_row(table_model))
        # layout_database_window.addWidget(button_add_row)

        # button_del_row = QPushButton("Delete a row")
        self.button_del_row.clicked.connect(lambda: table_model.removeRow(self.view_primary.currentIndex().row()))
        # layout_database_window.addWidget(button_del_row)

        # button_done = QPushButton("Done")
        self.button_done.clicked.connect(self.close)
        # layout_database_window.addWidget(button_done)

        # Set layout and start the window
        # dlg.setLayout(layout_database_window)
        self.setWindowTitle("Database Demo")
        logger.debug("ThemeTable::on_button_clicked - Database dialog started")
        self.showMaximized()
        logger.debug("ThemeTable::on_button_clicked - Database dialog terminated")
        logger.debug("ThemeTable::on_button_clicked - Exited method")

    def exit_from_window(self):
        self.main_window = ThemeTable()
        self.main_window.showMaximized()
        self.close()


# Database Manager class
if __name__ == "__main__":
    print('пусто')