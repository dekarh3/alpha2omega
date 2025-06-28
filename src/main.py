#!/usr/bin/env python3
from src.logger import logger, logger_output_file_path
from PyQt5.QtWidgets import QApplication

import sys

from src.constants import app_folder
from src.DbManager import DbManager
from src.RootView.RootView import RootView

def main():
    try:
        logger.debug("main - logger instantiated")
        logger.debug("main - Log output file can be found at: " + str(logger_output_file_path))


        app = QApplication(sys.argv)

        db_manager = DbManager('QSQLITE', 'alpa2omega.db', app_folder, logger) #, app_folder)

        user_view = RootView(db_manager, logger)
        user_view.show()
    except Exception as e:
        logger.error("An error occurred: %s", e)

    logger.debug("main - App started")
    logger.debug('sys.path:' + ' '.join(sys.path))
    sys.exit(app.exec())

if __name__ == "__main__":
    sys.exit(main())