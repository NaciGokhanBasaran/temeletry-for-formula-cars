# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:33:24 2025

@author: gokhan2
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout,QLabel, QPushButton, QWidget, QHBoxLayout, QStackedWidget, QFrame
import sys
from PyQt5.QtCore import Qt
from MainPage import MainPage
from ConnectionsPage import ConnectionsPage
from VisualizePage import VisualizePage



from commanFuncs import updateData,ReadData

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Settings Page")
        label.setStyleSheet("font-size: 32px; color: #ffffff;")
        layout.addWidget(label, alignment=Qt.AlignCenter)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BauFormula")
        self.resize(1800, 900)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        
        navbar_frame = QFrame()
        navbar_frame.setFixedWidth(250)
        navbar_frame.setStyleSheet("""
            QFrame {
                background-color: #1a1d2e;
                border-top-left-radius: 15px;
                border-bottom-left-radius: 15px;
            }
        """)
        navbar_layout = QVBoxLayout(navbar_frame)
        navbar_layout.setAlignment(Qt.AlignTop)
        navbar_layout.setSpacing(15)
        navbar_layout.setContentsMargins(15, 30, 15, 15)

        
        button_style = """
            QPushButton {
                background-color: #1a1d2e;
                color: #ffffff;
                border: none;
                padding: 12px;
                font-size: 16px;
                text-align: left;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2c2f48;
            }
            QPushButton:checked {
                background-color: #007bff;
                font-weight: bold;
            }
        """

        self.main_btn = QPushButton("Main")
        self.conn_btn = QPushButton("Connections")
        self.vis_btn = QPushButton("Visualize")
        self.sett_btn = QPushButton("Settings")

        
        for btn in [self.main_btn, self.conn_btn, self.vis_btn, self.sett_btn]:
            btn.setCheckable(True)
            btn.setStyleSheet(button_style)
            navbar_layout.addWidget(btn)

       
        self.stack = QStackedWidget()
        self.stack.addWidget(MainPage())
        self.stack.addWidget(ConnectionsPage())
        self.stack.addWidget(VisualizePage())
        self.stack.addWidget(SettingsPage())

      
        self.main_btn.clicked.connect(lambda: self.set_page(0))
        self.conn_btn.clicked.connect(lambda: self.set_page(1))
        self.vis_btn.clicked.connect(lambda: self.set_page(2))
        self.sett_btn.clicked.connect(lambda: self.set_page(3))

        main_layout.addWidget(navbar_frame)
        main_layout.addWidget(self.stack)

     
        self.setStyleSheet("""
            QWidget {
                background-color: #232946;
                font-family: 'Segoe UI', sans-serif;
            }
        """)

        self.set_page(0)
        #navbar_frame.setVisible(0) 

    def set_page(self, index):
        self.stack.setCurrentIndex(index)
        buttons = [self.main_btn, self.conn_btn, self.vis_btn, self.sett_btn]
        for i, btn in enumerate(buttons):
            btn.setChecked(i == index)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
   
   




