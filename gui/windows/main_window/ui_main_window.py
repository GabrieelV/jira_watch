from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Parametros iniciais
        parent.resize(500, 130)
        parent.setMinimumSize(500, 130)
        # parent.setWindowFlags(Qt.FramelessWindowHint)

        # parent.setMaximumSize(500, 130)

        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.top_menu()
        self.content()
        # self.content()
        self.bottom_bar()

        # Set central widget
        parent.setCentralWidget(self.central_frame)

    def top_menu(self):
        # Top Menu
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color: #4170a9; color: #f8f8f2")
        self.top_bar.setMaximumHeight(35)
        self.top_bar.setMinimumHeight(35)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(20, 0, 20, 0)

        # Top label
        self.lb_filtro = QLabel("Filtro")
        self.lb_filtro.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.cb_projetos = QComboBox()
        self.cb_projetos.setFixedWidth(150)

        self.cb_projetos.addItem("Teste 1")
        self.cb_projetos.addItem("Teste 2")
        self.cb_projetos.addItem("Teste 3 aaaaa123")

        self.bt_add_task_space = QPushButton('+')
        self.bt_add_task_space.setMinimumWidth(35)
        self.bt_add_task_space.setMaximumWidth(35)

        # Add to layout
        self.top_bar_layout.addWidget(self.lb_filtro)
        self.top_bar_layout.addWidget(self.cb_projetos)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.bt_add_task_space)

        # Adicionar widgets
        self.main_layout.addWidget(self.top_bar)
        
    def content(self):
        # Content
        content = QFrame()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Spacer
        spacer_1 = QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Content top
        content_top = QFrame()
        content_top.setStyleSheet("background-color: #282a36; color: #ffffff")

        # Content top layout
        content_layout_top = QHBoxLayout(content_top)
        content_layout_top.setContentsMargins(20, 5, 20, 0)
        content_layout_top.setSpacing(5)
        
        # Content bottom
        content_bottom = QFrame()
        content_bottom.setStyleSheet("background-color: #000000; color: #ffffff")

        # Content bottom layout
        content_layout_bottom = QHBoxLayout(content_bottom)
        content_layout_bottom.setContentsMargins(20, 0, 20, 5)
        content_layout_bottom.setSpacing(0)

        # Content top components
        cb_tasks = QComboBox()
        cb_tasks.addItem('CER-196 - TESTE 1')
        cb_tasks.addItem('CER-198 - TESTE 2')
        cb_tasks.addItem('CER-203 - TESTE 3')
        cb_tasks.setFixedWidth(150)

        bt_play = QPushButton("P")
        bt_play.setMinimumWidth(35)
        bt_play.setMaximumWidth(35)

        txt_time = QLineEdit('0m')
        txt_time.setReadOnly(True)
        txt_time.setAlignment(Qt.AlignRight)

        bt_send_work = QPushButton("S")
        bt_send_work.setMinimumWidth(35)
        bt_send_work.setMaximumWidth(35)

        bt_reset_work_time = QPushButton("R")
        bt_reset_work_time.setMinimumWidth(35)
        bt_reset_work_time.setMaximumWidth(35)

        bt_delete_content_work = QPushButton("D")
        bt_delete_content_work.setMinimumWidth(35)
        bt_delete_content_work.setMaximumWidth(35)


        # Add to content top layout
        content_layout_top.addWidget(cb_tasks)
        content_layout_top.addItem(spacer_1)
        content_layout_top.addWidget(bt_play)
        content_layout_top.addWidget(txt_time)
        content_layout_top.addWidget(bt_send_work)
        content_layout_top.addItem(spacer_1)
        content_layout_top.addWidget(bt_reset_work_time)
        content_layout_top.addWidget(bt_delete_content_work)


        # Content bottom components
        lb_task_tittle = QLabel("Teste titulo")

        # Add to content bottom layout
        content_layout_bottom.addWidget(lb_task_tittle)
        content_layout_bottom.addItem(spacer_1)

        # Add widgets to content layout
        content_layout.addWidget(content_top)
        content_layout.addWidget(content_bottom)
        self.main_layout.addWidget(content)

    def bottom_bar(self):

        # Bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        # self.bottom_bar.setStyleSheet("background-color: #282a36; color: #000000")
        self.bottom_bar.setStyleSheet("background-color: #ffffff; color: #000000")

        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")

        self.main_layout.addWidget(self.pages)
        self.main_layout.addWidget(self.bottom_bar)

        # Adicionar widgets
        # self.main_layout.addWidget(self.content)
        # self.main_layout.addWidget(self.bottom_bar)

        # Set central widget
