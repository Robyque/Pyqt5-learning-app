# ==========<IMPORTS>========== #
from posixpath import split
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QListWidget,
    QDialog,
    QApplication,
    QAction,
    QWidget,
    QCheckBox,
    QVBoxLayout,
    QLabel,
    QDesktopWidget,
    QSizePolicy,
    QPushButton,
)
from PyQt5.QtGui import QPixmap, QIcon, QImage, QCursor
import os.path
from string import Template
import os
import qrcode
import random
import string
import time
from pytube import YouTube, Playlist
import urllib
import requests
from configparser import ConfigParser
import concurrent.futures
import pyodbc

# ============================#

main_py_dir = os.path.dirname(__file__)
config_path = "config/config.ini"
theme_path = "config/theme.ini"
config_abs_file_path = os.path.join(main_py_dir, config_path)
theme_abs_file_path = os.path.join(main_py_dir, theme_path)

# ====<Config>================#

config = ConfigParser()
config.read(config_abs_file_path)

# ====<Theme Config>=======================#

theme = ConfigParser()
theme.read(theme_abs_file_path)

# ====<Theme Manager>=====================#

# ===<Main Area Tabs>===#

tabwidget_panel = """QTabWidget::pane{ background: """
tab_bar = """QTabWidget::tab-bar{ background-color:"""
tab_bar_tab = """QTabBar::tab{ background-color: """
tab_bar_selected = """QTabBar::tab:selected{ background-color: """
tabwidget_background_color = theme["dracula"]["background_color"]
tab_bar_css = tab_bar + tabwidget_background_color + ";}"
tabwidget_panel_css = tabwidget_panel + tabwidget_background_color + ";}  "
tab_bar_tab_css = tab_bar_tab + tabwidget_background_color + ";}"
tab_bar_selected_css = tab_bar_selected + tabwidget_background_color + ";}"
tab_background_color = tab_bar_tab_css + tab_bar_selected_css


# ===<Main Window>===#

Background_Color = """background-color:"""
Background_Color_Color = theme["dracula"]["background_color"]
Main_Window_Background_Color = Background_Color + Background_Color_Color + ";"

# ===<Menu Buttons>======#

home_icon_abs_path = "images/32px/house-32px.png"
settings_icon_abs_path = "images/32px/settings-32px.png"
home_icon_path = os.path.join(main_py_dir, home_icon_abs_path)
settings_icon_path = os.path.join(main_py_dir, settings_icon_abs_path)
home_icon_css = """QPushButton{background-image: url(\""""
home_icon = home_icon_css + home_icon_path + '")}'
settings_icon_css = """QPushButton{background-image: url(\""""
settings_icon = settings_icon_css + settings_icon_path + '")}'

# ===<Other Menu Buttons>=== #

Button = """
QPushButton{border-radius: 10px; padding: 7px; background-color:"""
Button_Hover = """QPushButton::hover{ background-color:"""
Button_Pressed = """QPushButton::pressed{ background-color:"""
Button_Pressed_Color = theme["dracula"]["button_pressed_color"]
Button_Pressed_CSS = Button_Pressed + Button_Pressed_Color + ";}"
Button_Hover_Color = theme["dracula"]["button_hover_color"]
Button_Hover_CSS = Button_Hover + Button_Hover_Color + ";}"
Button_Color = theme["dracula"]["button_color"]
Button_Color_CSS = Button + Button_Color + ";}"
Button_CSS = Button_Color_CSS + Button_Hover_CSS + Button_Pressed_CSS

# ===<Tab Buttons>===#

tab_button = """QPushButton{color: #bd93f9;border-radius: 10px;padding:2px; border:1px;background-color: """
tab_button_hover = """QPushButton::hover{ background-color: """
tab_button_pressed = """QPushButton::pressed{ color:black;background-color: """
tab_button_color = theme["dracula"]["tab_button_color"]
tab_button_hover_color = theme["dracula"]["tab_button_hover"]
tab_button_pressed_color = theme["dracula"]["tab_button_pressed"]
tab_button_css = tab_button + tab_button_color + ";}"
tab_button_hover_css = tab_button_hover + tab_button_hover_color + ";}"
tab_button_pressed_css = tab_button_pressed + tab_button_pressed_color + ";}"
tabs_buttons = tab_button_css + tab_button_hover_css + tab_button_pressed_css

# ===<Tab TextEdit>===#

text_edit = """QTextEdit{border:2px solid """
text_edit_border_color = theme["dracula"]["border_color"]
text_edit_text_color = theme["dracula"]["text_color"]
text_edit_css = (
    text_edit + text_edit_border_color + ";" + "color: " + text_edit_text_color + ";}"
)
# ===<List view>===#
list_view = """QListView{border:2px solid"""
list_view_border_color = theme["dracula"]["border_color"]
list_view_text_color = theme["dracula"]["text_color"]
list_view_css = (
    list_view + list_view_border_color + ";" + "color: " + list_view_text_color + ";}"
)

# ============================#


class Ui_TheManager(object):
    def setupUi(self, TheManager):
        TheManager.setObjectName("TheManager")
        TheManager.setFixedSize(1300, 640)
        TheManager.setStyleSheet(Main_Window_Background_Color)
        self.centralwidget = QtWidgets.QWidget(TheManager)
        self.centralwidget.setObjectName("centralwidget")

        # ===<Side_Menu_Bar_Frame>===#

        self.Side_Menu_bar = QtWidgets.QFrame(self.centralwidget)
        self.Side_Menu_bar.setGeometry(QtCore.QRect(0, 0, 300, 651))
        self.Side_Menu_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Side_Menu_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Side_Menu_bar.setObjectName("Side_Menu_bar")

        # ===<Menu_Bar_Frame>===#

        self.Menu = QtWidgets.QFrame(self.Side_Menu_bar)
        self.Menu.setGeometry(QtCore.QRect(0, 37, 190, 200))
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Menu)
        self.verticalLayout.setObjectName("verticalLayout")

        # =>

        self.Account_Manager_Button = QtWidgets.QPushButton(self.Menu)
        self.Account_Manager_Button.setFlat(True)
        self.Account_Manager_Button.setObjectName("Account_Manager_Button")
        self.verticalLayout.addWidget(self.Account_Manager_Button)

        # =>

        self.Password_Generator_Button = QtWidgets.QPushButton(self.Menu)
        self.Password_Generator_Button.setFlat(True)
        self.Password_Generator_Button.setObjectName("Password_Generator_Button")
        self.verticalLayout.addWidget(self.Password_Generator_Button)
        # =>
        self.QRCode_Generator_Button = QtWidgets.QPushButton(self.Menu)
        self.QRCode_Generator_Button.setFlat(True)
        self.QRCode_Generator_Button.setObjectName("QRCode_Generator_Button")
        self.verticalLayout.addWidget(self.QRCode_Generator_Button)
        # =>
        self.Youtube_Downloader_Button = QtWidgets.QPushButton(self.Menu)
        self.Youtube_Downloader_Button.setFlat(True)
        self.Youtube_Downloader_Button.setObjectName("Youtube_Downloader_Button")
        self.verticalLayout.addWidget(self.Youtube_Downloader_Button)

        # =>

        self.FH4_Drift_Setup_Button = QtWidgets.QPushButton(self.Menu)
        self.FH4_Drift_Setup_Button.setFlat(True)
        self.FH4_Drift_Setup_Button.setObjectName("FH4_Drift_Setup_Button")
        self.verticalLayout.addWidget(self.FH4_Drift_Setup_Button)

        # ===<Utilities_Bar_Frame>===#

        self.Utilities_Bar = QtWidgets.QFrame(self.Side_Menu_bar)
        self.Utilities_Bar.setGeometry(QtCore.QRect(0, 0, 300, 41))
        self.Utilities_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Utilities_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Utilities_Bar.setObjectName("Utilities_Bar")

        # =>

        self.Home_Button = QtWidgets.QPushButton(self.Utilities_Bar)
        self.Home_Button.setGeometry(QtCore.QRect(5, 6, 34, 33))
        self.Home_Button.setText("")
        self.Home_Button.setFlat(True)
        self.Home_Button.setObjectName("Home_Button")
        # ===
        self.Settings_Button = QtWidgets.QPushButton(self.Utilities_Bar)
        self.Settings_Button.setGeometry(QtCore.QRect(35, 6, 34, 33))
        self.Settings_Button.setText("")
        self.Settings_Button.setFlat(True)
        self.Settings_Button.setObjectName("Settings")
        # ===<Main_Area_Frame>===#
        self.Main_Area = QtWidgets.QFrame(self.centralwidget)
        self.Main_Area.setGeometry(QtCore.QRect(299, 40, 891, 531))
        self.Main_Area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Area.setObjectName("Main_Area")
        # ===<Tab_Widget>===#
        self.tabWidget = QtWidgets.QTabWidget(self.Main_Area)
        self.tabWidget.setGeometry(QtCore.QRect(12, -14, 871, 541))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        # =>
        self.Startup_Tab = QtWidgets.QWidget()
        self.Startup_Tab.setObjectName("Startup_Tab")
        self.tabWidget.addTab(self.Startup_Tab, "")
        # ===<Account Manager>===#
        self.Account_Manager = QtWidgets.QWidget()
        self.Account_Manager.setObjectName("Account_Manager")
        # =>
        self.Account_Data_Frame = QtWidgets.QFrame(self.Account_Manager)
        self.Account_Data_Frame.setGeometry(QtCore.QRect(0, 0, 471, 201))
        self.Account_Data_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Account_Data_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Account_Data_Frame.setObjectName("Account_Data_Frame")
        # =>
        self.gridLayout = QtWidgets.QGridLayout(self.Account_Data_Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.Email_TextLine = QtWidgets.QTextEdit(self.Account_Data_Frame)
        self.Email_TextLine.setObjectName("Email_TextLine")
        self.gridLayout.addWidget(self.Email_TextLine, 4, 0, 1, 1)
        # =>
        self.Username_TextLine = QtWidgets.QTextEdit(self.Account_Data_Frame)
        self.Username_TextLine.setObjectName("Username_TextLine")
        self.gridLayout.addWidget(self.Username_TextLine, 3, 0, 1, 1)
        # =>
        self.Password_Textline = QtWidgets.QTextEdit(self.Account_Data_Frame)
        self.Password_Textline.setObjectName("Password_Textline")
        self.gridLayout.addWidget(self.Password_Textline, 6, 0, 1, 1)
        # =>
        self.Site_Name_TextLine = QtWidgets.QTextEdit(self.Account_Data_Frame)
        self.Site_Name_TextLine.setObjectName("Site_Name_TextLine")
        self.gridLayout.addWidget(self.Site_Name_TextLine, 0, 0, 1, 1)
        # =>
        self.Username_Checkbox = QtWidgets.QCheckBox(self.Account_Data_Frame)
        self.Username_Checkbox.setObjectName("Username_Checkbox")
        self.gridLayout.addWidget(self.Username_Checkbox, 2, 0, 1, 1)
        # =>
        self.Account_View_Frame = QtWidgets.QFrame(self.Account_Manager)
        self.Account_View_Frame.setGeometry(QtCore.QRect(0, 210, 301, 251))
        self.Account_View_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Account_View_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Account_View_Frame.setObjectName("Account_View_Frame")
        # =>
        self.Save_Button = QtWidgets.QPushButton(self.Account_View_Frame)
        self.Save_Button.setGeometry(QtCore.QRect(12, 12, 88, 31))
        self.Save_Button.setFlat(True)
        self.Save_Button.setObjectName("Save_Button")
        # =>
        self.Delete_Button = QtWidgets.QPushButton(self.Account_View_Frame)
        self.Delete_Button.setGeometry(QtCore.QRect(106, 12, 88, 31))
        self.Delete_Button.setFlat(True)
        self.Delete_Button.setObjectName("Delete_Button")
        # =>
        self.Reload_Button = QtWidgets.QPushButton(self.Account_View_Frame)
        self.Reload_Button.setGeometry(QtCore.QRect(201, 12, 88, 31))
        self.Reload_Button.setFlat(True)
        self.Reload_Button.setObjectName("Reload_Button")
        # =>
        self.Account_List = QtWidgets.QListView(self.Account_View_Frame)
        self.Account_List.setGeometry(QtCore.QRect(12, 46, 281, 192))
        self.Account_List.setObjectName("Account_List")
        # =>
        self.Account_Viewer_Frame = QtWidgets.QFrame(self.Account_Manager)
        self.Account_Viewer_Frame.setGeometry(QtCore.QRect(310, 210, 481, 251))
        self.Account_Viewer_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Account_Viewer_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Account_Viewer_Frame.setObjectName("Account_Viewer_Frame")
        # =>
        self.Account_Viewer = QtWidgets.QListView(self.Account_Viewer_Frame)
        self.Account_Viewer.setGeometry(QtCore.QRect(12, 46, 461, 192))
        self.Account_Viewer.setObjectName("Account_Viewer")
        # =>
        self.Edit_Button = QtWidgets.QPushButton(self.Account_Viewer_Frame)
        self.Edit_Button.setGeometry(QtCore.QRect(12, 12, 88, 31))
        self.Edit_Button.setFlat(True)
        self.Edit_Button.setObjectName("Edit_Button")
        self.tabWidget.addTab(self.Account_Manager, "")
        # ===<Password Generator>===#
        self.Password_Generator = QtWidgets.QWidget()
        self.Password_Generator.setObjectName("Password_Generator")
        self.Password_Generator_Frame = QtWidgets.QFrame(self.Password_Generator)
        self.Password_Generator_Frame.setGeometry(QtCore.QRect(0, 0, 611, 101))
        self.Password_Generator_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Password_Generator_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Password_Generator_Frame.setObjectName("Password_Generator_Frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Password_Generator_Frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # =>
        self.Format_Type_Frame = QtWidgets.QFrame(self.Password_Generator_Frame)
        self.Format_Type_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Format_Type_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Format_Type_Frame.setObjectName("Format_Type_Frame")
        # =>
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Format_Type_Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # =>
        self.ABCD_CheckBox = QtWidgets.QCheckBox(self.Format_Type_Frame)
        self.ABCD_CheckBox.setObjectName("ABCD_CheckBox")
        self.horizontalLayout.addWidget(self.ABCD_CheckBox)
        # =>
        self.Special_Characters_CheckBox = QtWidgets.QCheckBox(self.Format_Type_Frame)
        self.Special_Characters_CheckBox.setObjectName("Special_Characters_CheckBox")
        self.horizontalLayout.addWidget(self.Special_Characters_CheckBox)
        # =>
        self.numbers_CheckBox = QtWidgets.QCheckBox(self.Format_Type_Frame)
        self.numbers_CheckBox.setObjectName("numbers_CheckBox")
        self.horizontalLayout.addWidget(self.numbers_CheckBox)
        # =>
        self.abcd_CheckBox = QtWidgets.QCheckBox(self.Format_Type_Frame)
        self.abcd_CheckBox.setObjectName("abcd_CheckBox")
        self.horizontalLayout.addWidget(self.abcd_CheckBox)
        # =>
        self.ABCD_Only_CheckBox = QtWidgets.QCheckBox(self.Format_Type_Frame)
        self.ABCD_Only_CheckBox.setObjectName("ABCD_Only_CheckBox")
        self.horizontalLayout.addWidget(self.ABCD_Only_CheckBox)
        # =>
        self.gridLayout_3.addWidget(self.Format_Type_Frame, 1, 1, 1, 1)
        self.Save_Password_Button = QtWidgets.QPushButton(self.Password_Generator_Frame)
        self.Save_Password_Button.setObjectName("Save_Password_Button")
        self.gridLayout_3.addWidget(self.Save_Password_Button, 1, 0, 1, 1)
        # =>
        self.Password_TextEdit = QtWidgets.QTextEdit(self.Password_Generator_Frame)
        self.Password_TextEdit.setObjectName("Password_TextEdit")
        self.gridLayout_3.addWidget(self.Password_TextEdit, 0, 1, 1, 1)
        # =>
        self.Generate_Password_Button = QtWidgets.QPushButton(
            self.Password_Generator_Frame
        )
        self.Generate_Password_Button.setObjectName("Generate_Password_Button")
        self.gridLayout_3.addWidget(self.Generate_Password_Button, 0, 0, 1, 1)
        # =>
        self.Length_ComboBox = QtWidgets.QComboBox(self.Password_Generator_Frame)
        self.Length_ComboBox.setObjectName("Length_ComboBox")
        self.gridLayout_3.addWidget(self.Length_ComboBox, 0, 2, 1, 1)
        self.tabWidget.addTab(self.Password_Generator, "")
        # ===>
        self.QRCode_Generator = QtWidgets.QWidget()
        self.QRCode_Generator.setObjectName("QRCode_Generator")
        self.QRCode_Generator_Frame = QtWidgets.QFrame(self.QRCode_Generator)
        self.QRCode_Generator_Frame.setGeometry(QtCore.QRect(0, 10, 531, 121))
        self.QRCode_Generator_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.QRCode_Generator_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QRCode_Generator_Frame.setObjectName("QRCode_Generator_Frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.QRCode_Generator_Frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # =>
        self.Generate_QRCode_Button = QtWidgets.QPushButton(self.QRCode_Generator_Frame)
        self.Generate_QRCode_Button.setObjectName("Generate_QRCode_Button")
        self.gridLayout_2.addWidget(self.Generate_QRCode_Button, 1, 0, 1, 1)
        # =>
        self.TextEdit_Frame = QtWidgets.QFrame(self.QRCode_Generator_Frame)
        self.TextEdit_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextEdit_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextEdit_Frame.setObjectName("TextEdit_Frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TextEdit_Frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # =>
        self.Link_TextEdit = QtWidgets.QTextEdit(self.TextEdit_Frame)
        self.Link_TextEdit.setObjectName("Link_TextEdit")
        self.verticalLayout_2.addWidget(self.Link_TextEdit)
        # =>
        self.File_Name_TextEdit = QtWidgets.QTextEdit(self.TextEdit_Frame)
        self.File_Name_TextEdit.setObjectName("File_Name_TextEdit")
        self.verticalLayout_2.addWidget(self.File_Name_TextEdit)
        self.gridLayout_2.addWidget(self.TextEdit_Frame, 1, 1, 1, 1)
        # =>
        self.QRCode_Preview_Label = QtWidgets.QLabel(self.QRCode_Generator)
        self.QRCode_Preview_Label.setGeometry(QtCore.QRect(540, 10, 121, 121))
        self.QRCode_Preview_Label.setText("")
        self.QRCode_Preview_Label.setObjectName("QRCode_Preview_Label")
        self.tabWidget.addTab(self.QRCode_Generator, "")
        # ===>
        self.Youtube_Downloader = QtWidgets.QWidget()
        self.Youtube_Downloader.setObjectName("Youtube_Downloader")
        self.Video_Preview_Frame = QtWidgets.QFrame(self.Youtube_Downloader)
        self.Video_Preview_Frame.setGeometry(QtCore.QRect(0, 70, 391, 221))
        self.Video_Preview_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Video_Preview_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Video_Preview_Frame.setObjectName("Video_Preview_Frame")
        # =>
        self.Video_Thumbnail_Label = QtWidgets.QLabel(self.Video_Preview_Frame)
        self.Video_Thumbnail_Label.setGeometry(QtCore.QRect(12, 12, 211, 111))
        self.Video_Thumbnail_Label.setText("")
        self.Video_Thumbnail_Label.setTextFormat(QtCore.Qt.AutoText)
        self.Video_Thumbnail_Label.setObjectName("Video_Thumdail_Label")
        # =>
        self.Video_Title_Label = QtWidgets.QLabel(self.Video_Preview_Frame)
        self.Video_Title_Label.setGeometry(QtCore.QRect(12, 149, 371, 31))
        self.Video_Title_Label.setText("")
        self.Video_Title_Label.setObjectName("Video_Title_Label")
        # =>
        self.Video_Status_Label = QtWidgets.QLabel(self.Video_Preview_Frame)
        self.Video_Status_Label.setGeometry(QtCore.QRect(10, 180, 371, 31))
        self.Video_Status_Label.setObjectName("Video_Status_Label")
        # =>
        self.Video_Search_Frame = QtWidgets.QFrame(self.Youtube_Downloader)
        self.Video_Search_Frame.setGeometry(QtCore.QRect(0, 0, 661, 61))
        self.Video_Search_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Video_Search_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Video_Search_Frame.setObjectName("Video_Search_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Video_Search_Frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # =>
        self.Video_Search_Button = QtWidgets.QPushButton(self.Video_Search_Frame)
        self.Video_Search_Button.setFlat(True)
        self.Video_Search_Button.setObjectName("Video_Search_Button")
        self.horizontalLayout_2.addWidget(self.Video_Search_Button)
        # =>
        self.Video_Link_Search_TextEdit = QtWidgets.QTextEdit(self.Video_Search_Frame)
        self.Video_Link_Search_TextEdit.setAutoFillBackground(False)
        self.Video_Link_Search_TextEdit.setStyleSheet("")
        self.Video_Link_Search_TextEdit.setObjectName("Video_Link_Search_TextEdit")
        self.horizontalLayout_2.addWidget(self.Video_Link_Search_TextEdit)
        # =>
        self.Video_Format_Frame = QtWidgets.QFrame(self.Youtube_Downloader)
        self.Video_Format_Frame.setGeometry(QtCore.QRect(0, 300, 391, 51))
        self.Video_Format_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Video_Format_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Video_Format_Frame.setObjectName("Video_Format_Frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Video_Format_Frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # =>
        self.Video_CheckBox = QtWidgets.QCheckBox(self.Video_Format_Frame)
        self.Video_CheckBox.setObjectName("Video_CheckBox")
        self.horizontalLayout_3.addWidget(self.Video_CheckBox)
        # =>
        self.Video_File_Format_CheckBox = QtWidgets.QComboBox(self.Video_Format_Frame)
        self.Video_File_Format_CheckBox.setObjectName("Video_File_Format_CheckBox")
        self.horizontalLayout_3.addWidget(self.Video_File_Format_CheckBox)
        # =>
        self.Video_Rezolution_CheckBox = QtWidgets.QComboBox(self.Video_Format_Frame)
        self.Video_Rezolution_CheckBox.setObjectName("Video_Rezolution_CheckBox")
        self.horizontalLayout_3.addWidget(self.Video_Rezolution_CheckBox)
        # =>
        self.Video_Bites_CheckBox = QtWidgets.QComboBox(self.Video_Format_Frame)
        self.Video_Bites_CheckBox.setObjectName("Video_Bites_CheckBox")
        self.horizontalLayout_3.addWidget(self.Video_Bites_CheckBox)
        # =>
        self.Audio_Format_Frame = QtWidgets.QFrame(self.Youtube_Downloader)
        self.Audio_Format_Frame.setGeometry(QtCore.QRect(0, 360, 274, 52))
        self.Audio_Format_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Audio_Format_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Audio_Format_Frame.setObjectName("Audio_Format_Frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Audio_Format_Frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # =>
        self.Audio_CheckBox = QtWidgets.QCheckBox(self.Audio_Format_Frame)
        self.Audio_CheckBox.setObjectName("Audio_CheckBox")
        self.horizontalLayout_4.addWidget(self.Audio_CheckBox)
        # =>
        self.Audio_File_Format_CheckBox = QtWidgets.QComboBox(self.Audio_Format_Frame)
        self.Audio_File_Format_CheckBox.setFrame(True)
        self.Audio_File_Format_CheckBox.setObjectName("Audio_File_Format_CheckBox")
        self.horizontalLayout_4.addWidget(self.Audio_File_Format_CheckBox)
        # =>
        self.Audio_Bites_ComboBox = QtWidgets.QComboBox(self.Audio_Format_Frame)
        self.Audio_Bites_ComboBox.setObjectName("Audio_Bites_ComboBox")
        self.horizontalLayout_4.addWidget(self.Audio_Bites_ComboBox)
        # =>
        self.Youtube_Download_Button = QtWidgets.QPushButton(self.Youtube_Downloader)
        self.Youtube_Download_Button.setGeometry(QtCore.QRect(0, 420, 91, 31))
        self.Youtube_Download_Button.setFlat(True)
        self.Youtube_Download_Button.setObjectName("Youtube_Download_Button")
        self.tabWidget.addTab(self.Youtube_Downloader, "")
        # ===>
        self.FH4_Drift_Setup = QtWidgets.QWidget()
        self.FH4_Drift_Setup.setObjectName("FH4_Drift_Setup")
        self.tabWidget.addTab(self.FH4_Drift_Setup, "")
        # ===<Top_Menu_Bar_Frame>===#
        self.Top_Menu_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Menu_Bar.setGeometry(QtCore.QRect(299, 0, 1000, 41))
        self.Top_Menu_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Top_Menu_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Menu_Bar.setObjectName("Top_Menu_Bar")
        # ===<Buttom_Menu_Bar_Frame>===#
        self.Buttom_Menu_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Buttom_Menu_Bar.setGeometry(QtCore.QRect(299, 570, 1000, 52))
        self.Buttom_Menu_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Buttom_Menu_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Buttom_Menu_Bar.setObjectName("Buttom_Menu_Bar")
        self.Close_Button = QtWidgets.QPushButton(self.Buttom_Menu_Bar)
        self.Close_Button.setGeometry(QtCore.QRect(900, 21, 88, 31))
        self.Close_Button.setFlat(True)
        self.Close_Button.setObjectName("Close_Button")
        TheManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(TheManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TheManager)

        # ==========<Applied Css>========== #

        # ===<Menu Bar>===#

        self.Home_Button.setStyleSheet(home_icon)
        self.Settings_Button.setStyleSheet(settings_icon)
        self.Account_Manager_Button.setStyleSheet(Button_CSS)
        self.Password_Generator_Button.setStyleSheet(Button_CSS)
        self.QRCode_Generator_Button.setStyleSheet(Button_CSS)
        self.Youtube_Downloader_Button.setStyleSheet(Button_CSS)
        self.FH4_Drift_Setup_Button.setStyleSheet(Button_CSS)
        # ===<Buttom Bar>===#
        self.Close_Button.setStyleSheet(Button_CSS)
        # ===<Tab Widget>===#
        self.tabWidget.setStyleSheet(tab_background_color)
        # ==<Account Manager Tab>==#
        # >Buttons
        self.Save_Button.setStyleSheet(tabs_buttons)
        self.Delete_Button.setStyleSheet(tabs_buttons)
        self.Reload_Button.setStyleSheet(tabs_buttons)
        self.Edit_Button.setStyleSheet(tabs_buttons)
        # >TextEdit
        self.Email_TextLine.setStyleSheet(text_edit_css)
        self.Username_TextLine.setStyleSheet(text_edit_css)
        self.Site_Name_TextLine.setStyleSheet(text_edit_css)
        self.Password_Textline.setStyleSheet(text_edit_css)
        # >ListView
        self.Account_List.setStyleSheet(list_view_css)
        self.Account_Viewer.setStyleSheet(list_view_css)
        # ===========<Tabs Actions>======== #
        self.Home_Button.clicked.connect(self.Home_tab)
        self.Account_Manager_Button.clicked.connect(self.Account_Manager_Tab)
        self.Password_Generator_Button.clicked.connect(self.Password_Generator_Tab)
        self.QRCode_Generator_Button.clicked.connect(self.QRCode_Generator_Tab)
        self.Youtube_Downloader_Button.clicked.connect(self.Youtube_Downloader_Tab)
        self.FH4_Drift_Setup_Button.clicked.connect(self.FH4_Drift_Setup_Tab)

    # self.Close_Button.clicked.connect()

    def Home_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Account_Manager_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Password_Generator_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def QRCode_Generator_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Youtube_Downloader_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    def FH4_Drift_Setup_Tab(self):
        self.tabWidget.setCurrentIndex(5)
        # ==========<Functions>=========== #

    def retranslateUi(self, TheManager):
        _translate = QtCore.QCoreApplication.translate
        TheManager.setWindowTitle(_translate("TheManager", "The Manager"))
        self.Account_Manager_Button.setText(_translate("TheManager", "Account Manager"))
        self.Password_Generator_Button.setText(
            _translate("TheManager", "Password Generator")
        )
        self.QRCode_Generator_Button.setText(
            _translate("TheManager", "QRCode Generator")
        )
        self.Youtube_Downloader_Button.setText(
            _translate("TheManager", "Youtube Downloader")
        )
        self.FH4_Drift_Setup_Button.setText(_translate("TheManager", "FH4 Drift Setup"))
        self.Username_Checkbox.setText(_translate("TheManager", "Username"))
        self.Save_Button.setText(_translate("TheManager", "Save"))
        self.Delete_Button.setText(_translate("TheManager", "Delete"))
        self.Reload_Button.setText(_translate("TheManager", "Reload"))
        self.Edit_Button.setText(_translate("TheManager", "Edit"))
        self.ABCD_CheckBox.setText(_translate("TheManager", "ABCD"))
        self.Special_Characters_CheckBox.setText(_translate("TheManager", "?!.,"))
        self.numbers_CheckBox.setText(_translate("TheManager", "1234"))
        self.abcd_CheckBox.setText(_translate("TheManager", "abcd"))
        self.ABCD_Only_CheckBox.setText(_translate("TheManager", "Only ABCD"))
        self.Save_Password_Button.setText(_translate("TheManager", "Save"))
        self.Generate_Password_Button.setText(_translate("TheManager", "Generate"))
        self.Generate_QRCode_Button.setText(_translate("TheManager", "Generate QRCode"))
        self.Video_Status_Label.setText(_translate("TheManager", "Status:"))
        self.Video_Search_Button.setText(_translate("TheManager", "Search"))
        self.Video_Link_Search_TextEdit.setPlaceholderText(
            _translate("TheManager", "Enter youtube link")
        )
        self.Video_CheckBox.setText(_translate("TheManager", "Video"))
        self.Audio_CheckBox.setText(_translate("TheManager", "Audio"))
        self.Youtube_Download_Button.setText(_translate("TheManager", "Download"))
        self.Close_Button.setText(_translate("TheManager", "Close"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TheManager()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
