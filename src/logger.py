import logging
import os.path

from src.constants import app_folder

logger_logging_level = logging.DEBUG
logger_output_file_name = "pyqt5-app.log"
logger_output_prefix_format = "[%(asctime)s] [%(levelname)s] - %(message)s"
logger_output_file_path = os.path.join(app_folder, str(logger_output_file_name))

logger = logging.getLogger(__name__)
logging.basicConfig(
    level = logger_logging_level,
    format = '[%(asctime)s] [%(levelname)s] - %(message)s',
    handlers = [
        logging.FileHandler(logger_output_file_path),   # Логи в файл
        logging.StreamHandler()                         # Логи в консоль
    ]
)

