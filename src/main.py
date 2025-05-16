#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication

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

    user_view = UserView(db_manager, logger)
    user_view.show()

    logger.debug("main - App started")
    sys.exit(app.exec())

if __name__ == "__main__":
    sys.exit(main())