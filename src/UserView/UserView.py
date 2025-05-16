from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt, QModelIndex


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

        self.themes_model = QSqlTableModel()
        self.themes_model_initialisation()
        self.tv_themes.setModel(self.themes_model)
        self.tv_themes.clicked.connect(self.themes_model_select_row)
        self.theme_id = -1

        self.measures_model = QSqlTableModel()
        self.measures_model_refreshing()
        self.tv_measures.setModel(self.measures_model)
        self.tv_measures.clicked.connect(self.measures_model_select_row)

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

    def themes_model_initialisation(self):
        self.logger.debug("UserView::initialise_themes_model - Entered method")
        self.themes_model.setQuery(QSqlQuery('SELECT id, name, about FROM themes WHERE deleted == 0'))
        self.themes_model.select()
        self.themes_model.setHeaderData(1, Qt.Horizontal, "id")
        self.themes_model.setHeaderData(1, Qt.Horizontal, "name")
        self.themes_model.setHeaderData(2, Qt.Horizontal, "about")
        self.logger.debug("UserView::initialise_themes_model - Exited method")

    def themes_model_select_row(self, index):
        self.theme_id = index.model().data(index.model().index(index.row(), 0))
        self.measures_model_refreshing()

    def measures_model_query(self, theme_id):
        return QSqlQuery(f'SELECT '
                            f'sl.name,'
                            f'm.date,'
                            f'm.value,'
                            f'ut.name '
                         f'FROM '
                            f'measures AS m '
                                f'LEFT JOIN souls AS sl ON m.soulId == sl.id '
                                f'LEFT JOIN unitTypes AS ut ON m.unitTypeId == ut.id '
                         f'WHERE '
                            f'm.themeId == {theme_id} AND m.deleted == 0')

    def measures_model_refreshing(self):
        self.logger.debug("UserView::initialise_measures_model - Entered method")
        self.measures_model.setQuery(self.measures_model_query(self.theme_id))
        self.measures_model.select()
        self.measures_model.setHeaderData(0, Qt.Horizontal, "name")
        self.measures_model.setHeaderData(1, Qt.Horizontal, "date")
        self.measures_model.setHeaderData(2, Qt.Horizontal, "value")
        self.measures_model.setHeaderData(3, Qt.Horizontal, "unit")
        self.logger.debug("UserView::initialise_measures_model - Exited method")

    def measures_model_select_row(self, i):
        self.logger.debug("DbManager::add_row - Entered method")
        self.delrow = i.row()
        self.logger.debug("DbManager::add_row - Exited method")

    def exit_from_window(self):
        self.main_window = UserView()
        self.main_window.showMaximized()
        self.logger.debug("main - App terminated")
        self.logger.debug("main - Exited function")
        self.close()


# Database Manager class
if __name__ == "__main__":
    print('пусто')