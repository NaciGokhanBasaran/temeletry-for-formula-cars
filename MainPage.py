# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 18:51:55 2025

@author: gokhan2
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout,QFrame
)
from PyQt5.QtCore import Qt,QTimer
import datetime
import threading
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import requests
import sys
import serial
import time
import pyqtgraph as pg
import json 
from style import *

from commanFuncs import updateData,ReadData

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BauFormula")
        
        self.setStyleSheet("""
            QWidget {
                background-color: #23272e;
                color: #f4f4f4;
                font-family: 'Segoe UI', 'Arial', sans-serif;
                font-size: 15px;
            }
            QLabel {
                background: transparent;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #2d8cf0;
                color: white;
                border: none;
                border-radius: 7px;
                padding: 10px 25px;
                font-size: 16px;
                font-weight: bold;
                margin: 10px;
                transition: background 0.3s;
            }
            QPushButton:hover {
                background-color: #1765ad;
            }
            QGroupBox {
                border: 2px solid #2d8cf0;
                border-radius: 10px;
                margin-top: 10px;
            }
        """)
        layout = QHBoxLayout()
        
       
        self.place1 = QVBoxLayout() 
        self.place2 = QVBoxLayout()
        self.place3 = QVBoxLayout()
        
        #layout.addLayout(self.place1,stretch =1)
        layout.addLayout(self.place2,stretch =2)
        layout.addLayout(self.place3,stretch =1)
        
        
        """for i in range(10):
            self.place1.addWidget(QLabel("lorem ipsum dolor sit amet "+str(i)))"""
        
        #place 2 widgets 
        
        
        
        
        self.x =[]
        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []
        self.y5 = []
        self.y6 = []
        self.y7 = []
        
        self.plotWidget1 = pg.PlotWidget()
        self.curve = self.plotWidget1.plot(self.x, self.y1, symbol='o', symbolBrush='w')

        self.plot1Frame=QFrame()
        self.plot1Frame.setStyleSheet(GRAPH_FRAME_STYLE)
        
        self.graph_layout=QVBoxLayout()
        self.pen1 = pg.mkPen(color='orange')
        self.plotWidget1.plot(self.x, self.y1,pen =self.pen1)

        self.plotWidget1.showGrid(x=True, y=True, alpha=0.3)
        self.plotWidget1.setLimits(xMin=0, xMax=4000)
        self.plotWidget1.setLimits(yMin=0, yMax=1000)
        
        self.graph_layout.addWidget(self.plotWidget1)
        self.plot1Frame.setLayout(self.graph_layout)

        
        self.place2.addWidget(self.plot1Frame, stretch=1)
          
        
        self.plotWidget2 = pg.PlotWidget()
        self.curve = self.plotWidget2.plot(self.x, self.y1, symbol='o', symbolBrush='pink')

        self.plot2Frame=QFrame()
        self.plot2Frame.setStyleSheet(GRAPH_FRAME_STYLE)
        
        self.graph_layout=QVBoxLayout()
        self.pen2 = pg.mkPen(color='#42f54e')
        self.pen3 = pg.mkPen(color='#f00030')
        self.plotWidget2.plot(self.x, self.y1,pen =self.pen2)

        self.plotWidget2.showGrid(x=True, y=True, alpha=0.3)
        self.plotWidget2.setLimits(xMin=0, xMax=4000)
        self.plotWidget2.setLimits(yMin=0, yMax=1000)
        
        self.graph_layout.addWidget(self.plotWidget2)
        self.plot2Frame.setLayout(self.graph_layout)

        
        self.place2.addWidget(self.plot2Frame, stretch=1)
        
       
        self.place2_bottom = QHBoxLayout()
        self.place2.addLayout(self.place2_bottom,stretch =1)
        
        self.barplotWidget1 = pg.PlotWidget()
        self.barplotWidget1.showGrid(x=True, y=True, alpha=0.3)
        self.barplotWidget1.setLimits(xMin=0, xMax=4000)
        self.barplotWidget1.setLimits(yMin=0, yMax=1000)
        
        self.barplot1 = pg.BarGraphItem(x=self.x, height=self.y4, width=0.3, brush='g')
        self.barplotWidget1.addItem(self.barplot1)
        
        self.barplot1Frame = QFrame()
        self.barplot1Frame.setStyleSheet(GRAPH_FRAME_STYLE)
        
        self.barplot1Layout = QVBoxLayout()
        self.barplot1Layout.addWidget(self.barplotWidget1)
        self.barplot1Frame.setLayout(self.barplot1Layout)
        
        self.place2_bottom.addWidget(self.barplot1Frame, stretch=1)
        
        
        
        self.barplotWidget2 = pg.PlotWidget()
        self.barplotWidget2.showGrid(x=True, y=True, alpha=0.3)
        self.barplotWidget2.setLimits(xMin=0, xMax=4000)
        self.barplotWidget2.setLimits(yMin=0, yMax=1000)
        
        self.barplot2 = pg.BarGraphItem(x=self.x, height=self.y5, width=0.3, brush='b')
        self.barplotWidget2.addItem(self.barplot2)
        
        self.barplot2Frame = QFrame()
        self.barplot2Frame.setStyleSheet(GRAPH_FRAME_STYLE)
        
        self.barplot2Layout = QVBoxLayout()
        self.barplot2Layout.addWidget(self.barplotWidget2)
        self.barplot2Frame.setLayout(self.barplot2Layout)
        
        self.place2_bottom.addWidget(self.barplot2Frame, stretch=1)
        
        
        
        #Place 3 
        self.speed_list =[]

        self.speed =0 
        self.taken_path =0
        self.speed_label = QLabel(f"km/h")

        self.place3.addWidget(self.speed_label,stretch =1)
        self.speed_label.setStyleSheet("""margin:10px;
                                       background-color:#1a1d2e;
                                       border-radius: 7px;padding: 1px;
                                       font-size: 56px;font-weight: bold;
                                       color: #d8e0ed;""")
                                       

        
        self.barplotWidget3 = pg.PlotWidget()
        self.place3.addWidget(self.barplotWidget3,stretch =2)
        
        
        
        
        
        self.barplot3 = pg.BarGraphItem(x=self.x, height=self.y6, width=0.3, brush='r')
        self.barplotWidget3.addItem(self.barplot3)
        
        self.barplotWidget4 = pg.PlotWidget()
        self.place3.addWidget(self.barplotWidget4,stretch =2)
        
        
        
        
        
        
        self.barplot4 = pg.BarGraphItem(x=self.x, height=self.y7, width=0.3, brush='w')
        self.barplotWidget4.addItem(self.barplot4)
        
        
        
        self.save_button = QPushButton("Save")
        self.place3.addWidget(self.save_button,stretch =1)
        self.save_button.clicked.connect(self.save2excel)

        
        self.setLayout(layout)
       
        # eğer connect başarılı ise !!!!!!!!!!!!!!!!!!!!!!!!!!
        data_config = ReadData() 
        if data_config["connect"] =="true":
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_threaded)
            self.timer.start(1000)
    def parse_line(self,line):
        result = {}
        try:
            # 1. Virgülle parçala
            parts = line.split(',')
    
            for part in parts:
                # 2. ':' ile böl → anahtar ve değer
                if ':' in part:
                    key, value = part.strip().split(':')
                    result[key] = int(value)
        except Exception as e:
            print(f"[!] Ayrıştırma hatası: {e}")
        
        return result
    def get_data(self):
        
        
        # if connect ==True:
        with open("app_data.json","r") as file:
            data = json.load(file)
        
        if data["connection_type"] =="web":
            url = data["url"]
    
            
            response = requests.get(url)
    
            
            if response.status_code == 200:
                
                data = response.json()
                
            
                if(len(self.x) ==0):
                    self.x.append(1)
                else :
                    self.x.append(self.x[-1]+1)
                #print(data)
                self.y1.append(int(data["d1"]))
                self.y2.append(int(data["d2"]))
                self.y3.append(int(data["d3"]))
                self.y4.append(int(data["d4"]))
                self.y5.append(int(data["d5"]))
                self.y6.append(int(data["d6"]))
                self.y7.append(int(data["d7"]))
                self.speed = data["d8"]
                self.speed_list.append(self.speed)
        else:
            
            
            BAUD = 9600
            PORT =data["com_port"]
            try:
                ser = serial.Serial(PORT, BAUD, timeout=1)
                
                print(f" Bağlantı kuruldu: {PORT}")

                while True:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        data = self.parse_line(line)
                        if(len(self.x) ==0):
                            self.x.append(1)
                        else :
                            self.x.append(self.x[-1]+1)
                        #print(data)
                        self.y1.append(int(data["d1"]))
                        self.y2.append(int(data["d2"]))
                        self.y3.append(int(data["d3"]))
                        self.y4.append(int(data["d4"]))
                        self.y5.append(int(data["d5"]))
                        self.y6.append(int(data["d6"]))
                        self.y7.append(int(data["d7"]))
                        self.speed = data["d8"]
                        self.speed_list.append(self.speed)

            except serial.SerialException as e:
                print(f" {e}")
            
            
            
        
    def draw(self):
        
        self.plotWidget1.clear()
        self.plotWidget2.clear()
        self.curve = self.plotWidget1.plot(self.x, self.y1, symbol='o', symbolBrush='w')

    
        
        self.plotWidget1.plot(self.x, self.y1,pen =self.pen1)
        self.plotWidget2.plot(self.x, self.y2, pen=self.pen2)
        self.plotWidget2.plot(self.x, self.y1, pen=self.pen3)
        
    
       
        self.barplotWidget1.clear()
        self.barplotWidget2.clear()
        self.barplotWidget3.clear()
        self.barplotWidget4.clear()
    
        
        self.barplot1 = pg.BarGraphItem(x=self.x, height=self.y4, width=0.3, brush='g')
        self.barplotWidget1.addItem(self.barplot1)
    
        self.barplot2 = pg.BarGraphItem(x=self.x, height=self.y5, width=0.3, brush='b')
        self.barplotWidget2.addItem(self.barplot2)
    
        self.barplot3 = pg.BarGraphItem(x=self.x, height=self.y6, width=0.3, brush='r')
        self.barplotWidget3.addItem(self.barplot3)
    
        self.barplot4 = pg.BarGraphItem(x=self.x, height=self.y7, width=0.3, brush='w')
        self.barplotWidget4.addItem(self.barplot4)
        
        self.speed_label.setText(
        
        f"{self.speed} km/h"
    )
    def update_threaded(self):
        t = threading.Thread(target=self.update)
        t.start()

    def update(self):
        self.get_data()
        QTimer.singleShot(0, self.draw)
    
   
    
    def save2excel(self):
        
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "BauFormulaData.xlsx",         
            "Excel Files (*.xlsx);;All Files (*)"
        )
    
        if path:  
            data = {
                "d1": self.y1,
                "d2": self.y2,
                "d3": self.y3,
                "d4": self.y4,
                "d5": self.y5,
                "d6": self.y6,
                "d7": self.y7,
                "speed": self.speed_list
            }
            df = pd.DataFrame(data)
            df.to_excel(path, index=False)
            
