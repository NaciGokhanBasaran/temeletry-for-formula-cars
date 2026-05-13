# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 19:35:27 2025

@author: gokhan2
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QButtonGroup, QPushButton, QComboBox,QApplication
)
from PyQt5.QtCore import Qt
import requests
import serial.tools.list_ports
import json
import sys
import threading
from style import connections_style


from commanFuncs import updateData,ReadData


data_config = ReadData()
            
            
            
class FindWindow(QWidget):
    def __init__(self, Com_Ports):
        super().__init__()
        self.Com_Ports = Com_Ports
        self.setWindowTitle("COM Port Scanner")
        self.setFixedSize(300, 200)

        self.layout = QVBoxLayout()
        self.label = QLabel("Doğru Port: Taranıyor...")
        self.label.setStyleSheet("font-size: 14px; color: white;")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #1a1d2e; color: white;")

        threading.Thread(target=self.find_Port, daemon=True).start()

    def find_Port(self):
        for port in self.Com_Ports:
            try:
                ser = serial.Serial(port, 9600, timeout=1)
                ser.close()
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line[0] =="d":
                   
                    self.label.setText(f"Doğru Port: {port}")
                    print(f" {port} başarılı +")
                    return
            except Exception as e:
                print(f" {port} başarısız -", str(e))

        self.label.setText("Uygun port bulunamadı.")
    
     
        
        
        
        

class ConnectionsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget {
                background-color: #232946;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                background-color: #1a1d2e;
                border: 1px solid #394867;
                border-radius: 6px;
                padding: 6px;
                color: white;
            }
            QPushButton {
                background-color: #394867;
                color: white;
                border-radius: 6px;
                padding: 6px 14px;
            }
            QPushButton:hover {
                background-color: #4e5d82;
            }
            QPushButton#connectBtn {
                background-color: #007bff;
                font-weight: bold;
            }
            QPushButton#connectBtn:hover {
                background-color: #3399ff;
            }
            QRadioButton {
                spacing: 10px;
            }
        """)
        self.Com_Ports =[]
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(50, 40, 50, 20)
        layout.setSpacing(20)

        
        title = QLabel("Connections")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        
        type_layout = QHBoxLayout()
        type_label = QLabel("Connection Type")
        self.web_radio = QRadioButton("Web")
        self.uart_radio = QRadioButton("UART")
        self.web_radio.setChecked(True)

        self.type_group = QButtonGroup()
        self.type_group.addButton(self.web_radio)
        self.type_group.addButton(self.uart_radio)

        type_layout.addWidget(type_label)
        type_layout.addSpacing(10)
        type_layout.addWidget(self.web_radio)
        type_layout.addWidget(self.uart_radio)
        layout.addLayout(type_layout)

        
        self.url_input = QLineEdit(data_config["url"])
        self.url_input.setPlaceholderText("Enter URL")
        layout.addWidget(QLabel("URL"))
        layout.addWidget(self.url_input)

        
        layout.addWidget(QLabel("COM Port"))
        port_layout = QHBoxLayout()
        self.com_port_box = QComboBox()
        self.com_port_box.setEditable(True)
       

        self.find_button = QPushButton("Find")
        port_layout.addWidget(self.com_port_box)
        port_layout.addWidget(self.find_button)
        layout.addLayout(port_layout)

        
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect)
        self.connect_button.setObjectName("connectBtn")

        button_layout.addWidget(self.save_button)
       
        button_layout.addWidget(self.connect_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        
        self.web_radio.toggled.connect(self.update_visibility)
        self.update_visibility()
        
        
        self.find_button.clicked.connect(self.open_find_window)
        self.save_button.clicked.connect(self.save)
        self.connect_button.clicked.connect(self.check_connection)
        self.find_com_ports()
        
        
        self.setStyleSheet(connections_style)
    
    
    
    def connect(self):
        updateData(data_config["connection_type"],data_config["url"],data_config["com_port"],"true")
    
    
    
    def update_visibility(self):   
        is_web = self.web_radio.isChecked()
        self.url_input.setEnabled(is_web)
        
        self.com_port_box.setEnabled(not is_web)
        self.find_button.setEnabled(not is_web)
        
    def save(self):   
        
        #değişecek
        config = {}  
    
        
        if self.web_radio.isChecked():
            config["connection_type"] = "web"
            config["url"] = self.url_input.text()
            config["com_port"] =data_config["com_port"]
            
            updateData("web",self.url_input.text(),data_config["com_port"],data_config["connect"])
        else:
            
            updateData("xbee",self.url_input.text(),data_config["com_port"],data_config["connect"])
    
        
        

            
    def find_com_ports(self):
        self.com_port_box.clear()
        ports = serial.tools.list_ports.comports()
        if not ports:
            self.com_port_box.addItem("No COM ports found")
        else:
            for port in ports:
                self.com_port_box.addItem(port.device)
                print(port[0])
                self.Com_Ports.append(port[0])

    def check_connection(self):
        if self.web_radio.isChecked():
            url = self.url_input.text()
            try:
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    print("başarılı")
                else:
                    print(f"başarısız")
            except Exception as e:
                print("başarısız :", str(e))
        else:
            port = self.com_port_box.currentText()
            try:
                ser = serial.Serial(port, 9600, timeout=1)
                ser.close()
                print(" başarılı")
            except Exception as e:
                print("başarısız", str(e))
    def open_find_window(self):
        self.find_window = FindWindow(self.Com_Ports)
        self.find_window.show()
        
