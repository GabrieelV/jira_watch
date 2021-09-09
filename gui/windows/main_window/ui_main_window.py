from qt_core import *
from gui.windows.main_window.ui_task_window import Ui_Tasks_Widget


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Parametros iniciais
        parent.setFixedSize(500, 130)
        # parent.resize(500, 130)
        # parent.setMinimumSize(500, 130)
        # parent.setWindowFlags(Qt.FramelessWindowHint)
        # parent.setMaximumSize(500, 130)
        self.parent = parent

        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")

        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.bar_top_frame = QFrame()
        self.bar_top_frame.setStyleSheet("background-color: #282a36")
        self.bar_top_layout = QVBoxLayout(self.bar_top_frame)
        self.bar_top_layout.setContentsMargins(0, 0, 0, 0)
        self.bar_top_layout.setSpacing(0)

        self.tasks_frame = QFrame()
        self.tasks_frame.setStyleSheet("background-color: #282a36")
        self.tasks_layout = QVBoxLayout(self.tasks_frame)
        self.tasks_layout.setContentsMargins(0, 0, 0, 0)
        self.tasks_layout.setSpacing(0)

        self.bar_bottom_frame = QFrame()
        self.bar_bottom_frame.setStyleSheet("background-color: #282a36")
        self.bar_bottom_layout = QVBoxLayout(self.bar_bottom_frame)
        self.bar_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bar_bottom_layout.setSpacing(0)

        self.main_layout.addWidget(self.bar_top_frame)
        self.main_layout.addWidget(self.tasks_frame)
        self.main_layout.addWidget(self.bar_bottom_frame)

        self.top_menu()
        self.bottom_bar()

        # First task
        self.task_list = list()
        self.task_list.append(Ui_Tasks_Widget())
        self.task_list[0].setup_ui()
        self.tasks_layout.addWidget(self.task_list[0].content_frame)

        # Set central widget
        parent.setCentralWidget(self.central_frame)

    def top_menu(self):
        # Top Menu
        top_bar = QFrame()
        top_bar.setStyleSheet("background-color: #4170a9; color: #f8f8f2")
        top_bar.setMaximumHeight(35)
        top_bar.setMinimumHeight(35)
        top_bar_layout = QHBoxLayout(top_bar)
        top_bar_layout.setContentsMargins(20, 0, 20, 0)

        # Top label
        lb_filtro = QLabel("Filtro")
        lb_filtro.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        cb_projetos = QComboBox()
        cb_projetos.setFixedWidth(150)

        cb_projetos.addItem("Teste 1")
        cb_projetos.addItem("Teste 2")
        cb_projetos.addItem("Teste 3 aaaaa123")

        bt_add_task_space = QPushButton('+')
        bt_add_task_space.setMinimumWidth(35)
        bt_add_task_space.setMaximumWidth(35)
        bt_add_task_space.clicked.connect(self.toggle_add_task_window)

        # Add to layout
        top_bar_layout.addWidget(lb_filtro)
        top_bar_layout.addWidget(cb_projetos)
        top_bar_layout.addItem(top_spacer)
        top_bar_layout.addWidget(bt_add_task_space)

        # Adicionar widgets
        self.bar_top_layout.addWidget(top_bar)
        
    def bottom_bar(self):

        # Bottom bar
        bottom_bar = QFrame()
        bottom_bar.setMinimumHeight(30)
        bottom_bar.setMaximumHeight(30)
        # self.bottom_bar.setStyleSheet("background-color: #282a36; color: #000000")
        bottom_bar.setStyleSheet("background-color: #ffffff; color: #000000")

        # self.pages = QStackedWidget()
        # self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")

        # self.main_layout.addWidget(self.pages)
        self.bar_bottom_layout.addWidget(bottom_bar)

        # Adicionar widgets
        # self.main_layout.addWidget(self.content)
        # self.main_layout.addWidget(self.bottom_bar)

        # Set central widget

    def toggle_add_task_window(self):
        lenght_size_list = len(self.task_list)
        if lenght_size_list < 5:
            self.task_list.append(Ui_Tasks_Widget())
            self.task_list[lenght_size_list].setup_ui()
            self.tasks_layout.addWidget(self.task_list[lenght_size_list].content_frame)
            height = self.parent.height() + 60
            self.parent.setFixedSize(500, height)
