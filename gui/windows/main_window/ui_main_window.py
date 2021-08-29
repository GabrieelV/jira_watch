from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Parametros iniciais
        parent.resize(500, 130)
        parent.setMinimumSize(500, 130)
        parent.setMaximumSize(500, 130)

        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")

        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Top Menu
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color: #4170a9; color: #f8f8f2")
        self.top_bar.setMaximumHeight(35)
        self.top_bar.setMinimumHeight(35)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(20, 0, 20, 0)

        # Top label
        self.top_label_filtro = QLabel("Filtro")
        self.top_label_filtro.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Add to layout
        self.top_bar_layout.addWidget(self.top_label_filtro)
        self.top_bar_layout.addItem(self.top_spacer)
        

        # Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # Content layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        # self.bottom_bar.setStyleSheet("background-color: #282a36; color: #000000")
        self.bottom_bar.setStyleSheet("background-color: #ffffff; color: #000000")

        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")

        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Adicionar widgets
        self.main_layout.addWidget(self.top_bar)
        self.main_layout.addWidget(self.content)
        # self.main_layout.addWidget(self.bottom_bar)

        # Set central widget
        parent.setCentralWidget(self.central_frame)
