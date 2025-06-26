from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt, QModelIndex, QDateTime

from datetime import datetime
from io import StringIO

import src.img_rc
from src.uis import UserView_ui

UserView_form, UserView_base = loadUiType(StringIO(UserView_ui))

def measures_model_query(theme_id):
    return QSqlQuery("SELECT "
                        "m.id,"
                        "sl.name || ' → ' || "
                        "IIF (m.sign < 0, '-', '') ||"
                        "m.value || ' ' || "
                        "ut.name || "
                        "' (' || strftime('%d.%m %H:%M', m.date, 'unixepoch') || ')',"
                        "date, "
                        "value, "
                        "unitTypeId, "
                        "sign "
                     'FROM '
                        'measures AS m '
                            'LEFT JOIN souls AS sl ON m.soulId == sl.id '
                            'LEFT JOIN unitTypes AS ut ON m.unitTypeId == ut.id '
                     'WHERE '
                        f'm.themeId == {theme_id} AND m.deleted == 0')

def themes_model_query():
    return QSqlQuery('SELECT '
                        'id, '
                        'oneString, '
                        'name, '
                        'nameIndex, '
                        'about, '
                        'date '
                     'FROM '
                        'themes '
                     'WHERE '
                        'deleted == 0')


class UserView(UserView_form, UserView_base):
    def __init__(self, db_manager, logger):
        self.main_window = None
        self.delrow = None
        self.measures_model = None
        self.theme_id = None
        self.themes_model = None
        self.logger = logger
        self.logger.debug("UserView::__init__ - Entered method")
        self.logger.debug("Definition:: widget_main_window_ui created")
        super(UserView_base, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Темы и измерения")

        self.themes_model_initialize()
        self.measures_model_initialize()

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

    def themes_model_initialize(self):
        self.logger.debug("UserView::initialise_themes_model - Entered method")
        self.themes_model = QSqlTableModel()
        self.themes_model.setQuery(themes_model_query())
        self.themes_model.select()
        self.themes_model.setHeaderData(1, Qt.Horizontal, "")
        self.tv_themes.setModel(self.themes_model)
        self.tv_themes.hideColumn(0)
        self.tv_themes.hideColumn(2)
        self.tv_themes.hideColumn(3)
        self.tv_themes.hideColumn(4)
        self.tv_themes.hideColumn(5)
        header_themes = self.tv_themes.horizontalHeader()
        header_themes.setStretchLastSection(True)
        self.tv_themes.clicked.connect(self.themes_model_select_row)
        self.theme_id = -1
        self.tbt_run_delete.hide()
        self.tbt_show_delete.hide()
        self.tbt_cancel.hide()
        self.tbt_duplicate.hide()
        self.tbt_save.hide()
        self.logger.debug("UserView::initialise_themes_model - Exited method")

    def themes_model_select_row(self, index):
        self.logger.debug("UserView::themes_model_select_row - Exited method")
        self.theme_id = index.model().data(index.model().index(index.row(), 0))
        self.measures_model_refresh(self.theme_id)
        selected_indexes = self.tv_themes.selectedIndexes() # Получаем индексы выделенных ячеек
        if not selected_indexes:
            return None  # Ничего не выделено
        selected_rows = {index.row() for index in selected_indexes} # Получаем уникальные номера строк
        row = selected_rows.pop() # Если выделено несколько строк, берем первую
        self.let_name.setText(self.themes_model.index(row, 2).data())
        self.let_name_index.setText(str(self.themes_model.index(row, 3).data()))
        self.let_about.setText(self.themes_model.index(row, 4).data())
        datetime_date = datetime.fromtimestamp(self.themes_model.index(row, 5).data())
        self.dtet_date.setDateTime(QDateTime(
            datetime_date.year, datetime_date.month, datetime_date.day, datetime_date.hour,
            datetime_date.minute, datetime_date.second)
        )
        self.logger.debug("UserView::themes_model_select_row - Exited method")

    def measures_model_initialize(self):
        self.logger.debug("UserView::measures_model_initialize - Entered method")
        self.measures_model = QSqlTableModel()
        self.tv_measures.setModel(self.measures_model)
        header_measures = self.tv_measures.horizontalHeader()
        header_measures.setStretchLastSection(True)
        self.measures_model_refresh()
        self.tv_measures.clicked.connect(self.measures_model_select_row)
        self.logger.debug("UserView::measures_model_initialize - Exited method")

    def measures_model_refresh(self, theme_id=1):
        self.logger.debug("UserView::measures_model_refresh - Entered method")
        self.measures_model.setQuery(measures_model_query(theme_id))
        self.measures_model.select()
        self.measures_model.setHeaderData(1, Qt.Horizontal, "")
        self.tv_measures.hideColumn(0)
        self.tv_measures.hideColumn(2)
        self.tv_measures.hideColumn(3)
        self.tv_measures.hideColumn(4)
        self.tv_measures.hideColumn(5)
        self.logger.debug("UserView::measures_model_refresh - Exited method")

    def measures_model_select_row(self, i):
        self.logger.debug("UserView::measures_model_select_row - Entered method")
        self.delrow = i.row()
        self.logger.debug("UserView::measures_model_select_row - Entered method")

    def exit_from_window(self):
        self.main_window = UserView()
        self.main_window.showMaximized()
        self.logger.debug("main - App terminated")
        self.logger.debug("main - Exited function")
        self.close()


# Database Manager class
if __name__ == "__main__":
    print('пусто')