# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 21:52:10 2025

@author: gokhan2
"""

GRAPH_FRAME_STYLE = """
QFrame {
    background-color:#1a1d2e;
    border-radius: 7px;
    padding: 1px;
}
"""

connections_style = """
/* ---- Genel Widget Ayarları ---- */
QWidget {
    background: #232946;
    color: #e3e6eb;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 15px;
}

/* ---- Başlık ve Label ---- */
QLabel {
    color: #e3e6eb;
    font-size: 15px;
    font-weight: 500;
}
QLabel#title, QLabel[heading="true"] {
    font-size: 19px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

/* ---- LineEdit ve ComboBox ---- */
QLineEdit, QComboBox {
    background-color: #1a1d2e;
    border: 1.5px solid #394867;
    border-radius: 7px;
    padding: 7px 12px;
    color: #e3e6eb;
    font-size: 15px;
    selection-background-color: #4e5d82;
}
QComboBox QAbstractItemView {
    background: #232946;
    color: #e3e6eb;
    border-radius: 7px;
    selection-background-color: #4e5d82;
}

/* ---- Butonlar ---- */
QPushButton {
    background-color: #394867;
    color: #eceff4;
    border: none;
    border-radius: 7px;
    padding: 8px 22px;
    font-size: 15px;
    font-weight: 600;
    transition: background 0.2s;
}
QPushButton:hover {
    background-color: #4e5d82;
    color: #fff;
}
QPushButton:pressed {
    background-color: #222e4c;
}
QPushButton#connectBtn {
    background-color: #007bff;
    color: #fff;
    font-weight: bold;
}
QPushButton#connectBtn:hover {
    background-color: #3399ff;
}

QPushButton#findBtn {
    background-color: #2376ae;
    color: #f3f6fa;
    font-weight: 600;
}
QPushButton#findBtn:hover {
    background-color: #3fa5e8;
}

/* ---- RadioButton ---- */
QRadioButton {
    color: #e3e6eb;
    font-size: 15px;
    spacing: 12px;
    padding: 3px 0px;
}
QRadioButton::indicator {
    width: 18px;
    height: 18px;
    border-radius: 9px;
    border: 2px solid #4e5d82;
    background: #1a1d2e;
}
QRadioButton::indicator:checked {
    background: #5e81ac;
    border: 2px solid #5e81ac;
}
QRadioButton::indicator:unchecked {
    border: 2px solid #4e5d82;
}

/* ---- FindWindow için ---- */
FindWindow, #FindWindow {
    background: #1a1d2e;
    color: #e3e6eb;
    border-radius: 10px;
}
FindWindow QLabel {
    font-size: 15px;
    color: #e3e6eb;
}

/* ---- ScrollBar ---- */
QScrollBar:vertical, QScrollBar:horizontal {
    background: #232946;
    border: none;
    width: 10px;
    margin: 0px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #4e5d82;
    border-radius: 5px;
    min-height: 20px;
    min-width: 20px;
}
QScrollBar::add-line, QScrollBar::sub-line {
    border: none;
    background: none;
}
"""
visualization_style ="""




/* Genel arkaplan ve font */
QWidget {
    background: #23272e;
    color: #e3e6eb;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 15px;
}

/* Label stilleri */
QLabel {
    color: #e3e6eb;
    font-size: 15px;
    font-weight: 500;
}

/* Butonlar */
QPushButton {
    background-color: #3b4252;
    color: #eceff4;
    border: none;
    border-radius: 7px;
    padding: 8px 18px;
    font-size: 15px;
    font-weight: 600;
    transition: background 0.2s;
}
QPushButton:hover {
    background-color: #5e81ac;
    color: #fff;
}
QPushButton:pressed {
    background-color: #4c566a;
}

/* ComboBox */
QComboBox {
    background-color: #2d323b;
    color: #e3e6eb;
    border: 1px solid #4c566a;
    border-radius: 6px;
    padding: 5px 12px;
    min-width: 90px;
}
QComboBox QAbstractItemView {
    background-color: #2d323b;
    color: #eceff4;
    selection-background-color: #434c5e;
    border-radius: 5px;
}

/* CheckBox */
QCheckBox {
    spacing: 8px;
    font-size: 15px;
    color: #e3e6eb;
}
QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border-radius: 5px;
    border: 2px solid #4c566a;
    background: #3b4252;
}
QCheckBox::indicator:checked {
    background: #5e81ac;
    border: 2px solid #5e81ac;
}

/* Dosya dialogları */
QFileDialog {
    background: #23272e;
    color: #e3e6eb;
}

/* pyqtgraph arka planı için özel stil */
pg.PlotWidget, QGraphicsView {
    background: #1e2228;
    border-radius: 10px;
    border: 1px solid #434c5e;
}

/* Scrollbar stilleri */
QScrollBar:vertical, QScrollBar:horizontal {
    background: #23272e;
    border: none;
    width: 10px;
    margin: 0px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: #4c566a;
    border-radius: 5px;
    min-height: 20px;
    min-width: 20px;
}
QScrollBar::add-line, QScrollBar::sub-line {
    border: none;
    background: none;
    
}

"""


