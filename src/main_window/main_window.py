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

from src.db_manager import DbManager
from src.logger import logger, app_folder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.debug("MainWindow::__init__ - Entered method")

        self.setWindowTitle("Example simple pyqt5 app")
        
        # Create a widget to serve as layout for the main window
        widget_main_window = QWidget(self)
        self.setCentralWidget(widget_main_window)
        layout_main_window = QVBoxLayout()
        widget_main_window.setLayout(layout_main_window)
        
        # Instantiate buttons for the main window
        button_magic = QPushButton("Press HERE for the MAGIC")
        button_exit = QPushButton("Press HERE to EXIT")
        
        # Add buttons to the main window layout
        layout_main_window.addWidget(button_magic)
        layout_main_window.addWidget(button_exit)

        # Attach callbacks to buttons
        button_magic.setCheckable(True)
        button_magic.clicked.connect(self.on_button_clicked)

        button_exit.setCheckable(True)
        button_exit.clicked.connect(self.close)
        
        # Ensure buttons resize to the whole window
        button_magic.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_exit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set the main window to show as maximised
        self.showMaximized()

        logger.debug("MainWindow::__init__ - Exited method")

    def on_button_clicked(self):
        
        logger.debug("MainWindow::on_button_clicked - Entered method")
        logger.debug("MainWindow::on_button_clicked - Button has been clicked")

        # Create alert window message
        alert = QMessageBox()
        alert.setWindowTitle("Information")
        alert_msg = """
        You clicked the button!
        
        This will open a database viewer and modifier.
        
        The app folder is: """
        alert_msg += str(app_folder)
        alert.setText(alert_msg)

        # Add standard buttons to the alert window and set OK as default
        alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        alert.setDefaultButton(QMessageBox.Ok)
        
        # Start the window
        logger.debug("MainWindow::on_button_clicked - Alert message started")
        # Note: do not maximise alert windows as it might lead to button display issues
        alert_value = alert.exec()

        # Return to main window if user cancels alert window
        if alert_value == QMessageBox.Cancel:
            alert.close()
            logger.debug("MainWindow::on_button_clicked - Alert message terminated")
        # Proceed to next window if user accepts alert window
        else:
            logger.debug("MainWindow::on_button_clicked - Alert message terminated")
        
            # Instantiate the database manager
            db_manager = DbManager('QSQLITE', 'sportsdatabase.db', app_folder)
            table_model = QSqlTableModel()
            db_manager.initialise_model(table_model)

            view_primary = db_manager.create_view("Table Model (View Primary)", table_model)
            view_primary.clicked.connect(db_manager.find_row)
            
            # Create a window to display the database viewer and modifier
            dlg = QDialog(self)
            layout_database_window = QVBoxLayout()
            layout_database_window.addWidget(view_primary)
            
            # Add buttons to the window to interact with the database viewer and modifier
            button_add_row = QPushButton("Add a row")
            button_add_row.clicked.connect(lambda: db_manager.add_row(table_model))
            layout_database_window.addWidget(button_add_row)

            button_del_row = QPushButton("Delete a row")
            button_del_row.clicked.connect(lambda: table_model.removeRow(view_primary.currentIndex().row()))
            layout_database_window.addWidget(button_del_row)

            button_done = QPushButton("Done")
            button_done.clicked.connect(dlg.close)
            layout_database_window.addWidget(button_done)
            
            # Set layout and start the window
            dlg.setLayout(layout_database_window)
            dlg.setWindowTitle("Database Demo")
            logger.debug("MainWindow::on_button_clicked - Database dialog started")
            dlg.showMaximized()
            dlg.exec()
            logger.debug("MainWindow::on_button_clicked - Database dialog terminated")
            logger.debug("MainWindow::on_button_clicked - Exited method")

if __name__ == "__main__":
    print('пусто')