from qt_core import *

class Ui_Tasks_Widget(object):
    def setup_ui(self):
        # if not parent.objectName():
            # parent.setObjectName('TaskWindow')

            # parent.resize(500, 100)
        self.content()

    def content(self):
        # Content
        self.content_frame = QFrame()
        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Spacer
        spacer_1 = QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Content top
        self.content_top = QFrame()
        self.content_top.setStyleSheet("background-color: #282a36; color: #ffffff")

        # Content top layout
        self.content_layout_top = QHBoxLayout(self.content_top)
        self.content_layout_top.setContentsMargins(20, 5, 20, 0)
        self.content_layout_top.setSpacing(5)
        
        # Content bottom
        self.content_bottom = QFrame()
        self.content_bottom.setStyleSheet("background-color: #282a36; color: #ffffff")

        # Content bottom layout
        self.content_layout_bottom = QHBoxLayout(self.content_bottom)
        self.content_layout_bottom.setContentsMargins(20, 0, 20, 5)
        self.content_layout_bottom.setSpacing(0)

        # Content top components
        self.cb_tasks = QComboBox()
        self.cb_tasks.addItem('CER-196 - TESTE 1')
        self.cb_tasks.addItem('CER-198 - TESTE 2')
        self.cb_tasks.addItem('CER-203 - TESTE 3')
        self.cb_tasks.setFixedWidth(150)

        self.bt_play = QPushButton("P")
        self.bt_play.setMinimumWidth(35)
        self.bt_play.setMaximumWidth(35)

        self.txt_time = QLineEdit('0m')
        self.txt_time.setReadOnly(True)
        self.txt_time.setAlignment(Qt.AlignRight)

        self.bt_send_work = QPushButton("S")
        self.bt_send_work.setMinimumWidth(35)
        self.bt_send_work.setMaximumWidth(35)

        self.bt_reset_work_time = QPushButton("R")
        self.bt_reset_work_time.setMinimumWidth(35)
        self.bt_reset_work_time.setMaximumWidth(35)

        self.bt_delete_content_work = QPushButton("D")
        self.bt_delete_content_work.setMinimumWidth(35)
        self.bt_delete_content_work.setMaximumWidth(35)
        self.bt_delete_content_work.clicked.connect(self.toggle_bt_delete_content_work)


        # Add to content top layout
        self.content_layout_top.addWidget(self.cb_tasks)
        self.content_layout_top.addItem(spacer_1)
        self.content_layout_top.addWidget(self.bt_play)
        self.content_layout_top.addWidget(self.txt_time)
        self.content_layout_top.addWidget(self.bt_send_work)
        self.content_layout_top.addItem(spacer_1)
        self.content_layout_top.addWidget(self.bt_reset_work_time)
        self.content_layout_top.addWidget(self.bt_delete_content_work)


        # Content bottom components
        self.lb_task_tittle = QLabel("Teste titulo")

        # Add to content bottom layout
        self.content_layout_bottom.addWidget(self.lb_task_tittle)
        self.content_layout_bottom.addItem(spacer_1)

        # Add widgets to content layout
        self.content_layout.addWidget(self.content_top)
        self.content_layout.addWidget(self.content_bottom)
        # self.main_layout.addWidget(content)
        # self.toggle_bt_delete_content_work()

    def toggle_bt_delete_content_work(self):
        for i in reversed(range(self.content_layout.count())): 
            self.content_layout.itemAt(i).widget().setParent(None)