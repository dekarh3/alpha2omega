from PyQt5.QtSql import QSqlTableModel
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt


from io import StringIO

# from src.main import table_model, db_manager
from src.uis import UserView_ui

UserView_form, UserView_base = loadUiType(StringIO(UserView_ui))

class UserView(UserView_form, UserView_base):
    def __init__(self, db_manager, logger):
        self.logger = logger
        self.logger.debug("UserView::__init__ - Entered method")
        self.logger.debug("Definition:: widget_main_window_ui created")
        super(UserView_base, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Темы и измерения")

        themes_model = QSqlTableModel()
        self.initialise_themes_model(themes_model)
        self.tv_themes.setModel(themes_model)
        self.tv_themes.clicked.connect(db_manager.find_row)

        measures_model = QSqlTableModel()
        self.initialise_measures_model(measures_model)
        self.tv_measures.setModel(measures_model)
        self.tv_measures.clicked.connect(db_manager.find_row)

        # Create a window to display the database viewer and modifier
        # dlg = QDialog(self)
        # layout_database_window = QVBoxLayout()
        # layout_database_window.addWidget(view_primary)

        # Add buttons to the window to interact with the database viewer and modifier
        # button_add_row = QPushButton("Add a row")
        self.button_add_row.clicked.connect(lambda: db_manager.add_row(table_model))
        # layout_database_window.addWidget(button_add_row)

        # button_del_row = QPushButton("Delete a row")
        self.button_del_row.clicked.connect(lambda: table_model.removeRow(self.tv_themes.currentIndex().row()))
        # layout_database_window.addWidget(button_del_row)

        # button_done = QPushButton("Done")
        self.button_done.clicked.connect(self.close)
        # layout_database_window.addWidget(button_done)

        # Set layout and start the window
        # dlg.setLayout(layout_database_window)
        self.logger.debug("UserView::on_button_clicked - Database dialog started")
        self.showMaximized()
        self.logger.debug("UserView::on_button_clicked - Database dialog terminated")
        self.logger.debug("UserView::on_button_clicked - Exited method")

    def initialise_themes_model(self, model):
        self.logger.debug("UserView::initialise_themes_model - Entered method")
        model.setTable('themes')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, Qt.Horizontal, "id")
        model.setHeaderData(1, Qt.Horizontal, "name")
        model.setHeaderData(2, Qt.Horizontal, "about")
        model.setHeaderData(3, Qt.Horizontal, "nameIndex")
        model.setHeaderData(4, Qt.Horizontal, "date")
        self.logger.debug("UserView::initialise_themes_model - Exited method")

    def initialise_measures_model(self, model):
        self.logger.debug("UserView::initialise_measures_model - Entered method")
        model.setTable('measures')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, Qt.Horizontal, "id")
        model.setHeaderData(1, Qt.Horizontal, "soulId")
        model.setHeaderData(2, Qt.Horizontal, "themeId")
        model.setHeaderData(3, Qt.Horizontal, "date")
        model.setHeaderData(4, Qt.Horizontal, "value")
        model.setHeaderData(5, Qt.Horizontal, "unitTypeId")
        model.setHeaderData(6, Qt.Horizontal, "sign")
        self.logger.debug("UserView::initialise_measures_model - Exited method")

    def exit_from_window(self):
        self.main_window = UserView()
        self.main_window.showMaximized()
        self.close()


# Database Manager class
if __name__ == "__main__":
    print('пусто')