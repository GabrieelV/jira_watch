from qt_core import *

class Ui_Tasks_Widget(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('TaskWindow')

            parent.resize(500, 100)