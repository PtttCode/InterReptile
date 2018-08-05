# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:31:32 2018

@author: PATIR
"""

import sys
import os

from PyQt5.QtWidgets import QApplication , QMainWindow

from reptileUI import Ui_MainWindow


def run(path):    
        try:
            app=0 
            app = QApplication(sys.argv)
            app.aboutToQuit.connect(app.deleteLater)
            w = QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(w,1)
            #ui.importData()
            w.show()
            ui.lineEdit.setText(path)
            ui.importDataAct()
            sys.exit(app.exec_())
        except Exception as e:
            pass
