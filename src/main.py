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

from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlTableModel

import sys

from src.logger import logger, logger_output_file_path, app_folder
from src.DbManager import DbManager
from src.UserView.UserView import UserView

def main():
    # Define path reference: app folder is the reference for the device

    logger.debug("main - logger instantiated")
    logger.debug("main - Log output file can be found at: " + str(logger_output_file_path))


    app = QApplication(sys.argv)

    db_manager = DbManager('QSQLITE', 'alpa2omega.db', app_folder, logger) #, app_folder)

    theme_table = UserView(db_manager, logger)
    theme_table.show()

    logger.debug("main - App started")
    sys.exit(app.exec())
    #logger.debug("main - App terminated")
    #logger.debug("main - Exited function")

if __name__ == "__main__":
    sys.exit(main())