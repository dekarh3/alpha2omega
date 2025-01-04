from PyQt5.QtWidgets import QApplication

import sys

from src.logger import logger, logger_output_file_path
from src.main_window.main_window import MainWindow

def main():
    # Define path reference: app folder is the reference for the device

    logger.debug("main - logger instantiated")
    logger.debug("main - Log output file can be found at: " + str(logger_output_file_path))

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    logger.debug("main - App started")
    sys.exit(app.exec())
    logger.info("main - App terminated")

    # The application will only reach here when exiting or event loop has stopped.
    logger.debug("main - Exited function")

if __name__ == "__main__":
    sys.exit(main())