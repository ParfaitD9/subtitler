# Form implementation generated from reading ui file 'assets/ui/subtitler.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_ann_file = QtWidgets.QLabel(self.centralwidget)
        self.label_ann_file.setObjectName("label_ann_file")
        self.verticalLayout.addWidget(self.label_ann_file)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_options_traitement = QtWidgets.QLabel(self.frame)
        self.label_options_traitement.setObjectName("label_options_traitement")
        self.verticalLayout_9.addWidget(self.label_options_traitement)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_select_langue = QtWidgets.QLabel(self.frame)
        self.label_select_langue.setObjectName("label_select_langue")
        self.verticalLayout_3.addWidget(self.label_select_langue)
        self.combo_lang = QtWidgets.QComboBox(self.frame)
        self.combo_lang.setObjectName("combo_lang")
        self.combo_lang.addItem("")
        self.combo_lang.addItem("")
        self.combo_lang.addItem("")
        self.combo_lang.addItem("")
        self.verticalLayout_3.addWidget(self.combo_lang)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_format = QtWidgets.QLabel(self.frame)
        self.label_format.setObjectName("label_format")
        self.verticalLayout_8.addWidget(self.label_format)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radio_audio = QtWidgets.QRadioButton(self.frame)
        self.radio_audio.setObjectName("radio_audio")
        self.verticalLayout_4.addWidget(self.radio_audio)
        self.radio_video = QtWidgets.QRadioButton(self.frame)
        self.radio_video.setChecked(True)
        self.radio_video.setObjectName("radio_video")
        self.verticalLayout_4.addWidget(self.radio_video)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_ann_content = QtWidgets.QLabel(self.frame_2)
        self.label_ann_content.setObjectName("label_ann_content")
        self.verticalLayout_5.addWidget(self.label_ann_content)
        self.text_content = QtWidgets.QTextEdit(self.frame_2)
        self.text_content.setObjectName("text_content")
        self.verticalLayout_5.addWidget(self.text_content)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_progress = QtWidgets.QLabel(self.frame_3)
        self.label_progress.setObjectName("label_progress")
        self.verticalLayout_2.addWidget(self.label_progress)
        self.progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_11.addWidget(self.frame_3)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_new = QtWidgets.QPushButton(self.centralwidget)
        self.button_new.setObjectName("button_new")
        self.horizontalLayout.addWidget(self.button_new)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_13.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_a_file = QtGui.QAction(MainWindow)
        self.actionOpen_a_file.setObjectName("actionOpen_a_file")
        self.actionOpen_multiple_files = QtGui.QAction(MainWindow)
        self.actionOpen_multiple_files.setObjectName("actionOpen_multiple_files")
        self.actionUpdate_subtitle = QtGui.QAction(MainWindow)
        self.actionUpdate_subtitle.setObjectName("actionUpdate_subtitle")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLatest_state = QtGui.QAction(MainWindow)
        self.actionLatest_state.setObjectName("actionLatest_state")
        self.menuFile.addAction(self.actionOpen_a_file)
        self.menuFile.addAction(self.actionOpen_multiple_files)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionUpdate_subtitle)
        self.menuEdit.addAction(self.actionLatest_state)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Subtitler"))
        self.label_ann_file.setText(_translate("MainWindow", "Select a file to extract the subtitles"))
        self.label_options_traitement.setText(_translate("MainWindow", "Treatment options"))
        self.label_select_langue.setText(_translate("MainWindow", "Language"))
        self.combo_lang.setItemText(0, _translate("MainWindow", "English (USA)"))
        self.combo_lang.setItemText(1, _translate("MainWindow", "English (UK)"))
        self.combo_lang.setItemText(2, _translate("MainWindow", "Français (France)"))
        self.combo_lang.setItemText(3, _translate("MainWindow", "Français (Belgique)"))
        self.label_format.setText(_translate("MainWindow", "Format"))
        self.radio_audio.setText(_translate("MainWindow", "Audio"))
        self.radio_video.setText(_translate("MainWindow", "Video"))
        self.label_ann_content.setText(_translate("MainWindow", "When the extraction is complete, you will see subtitles here"))
        self.label_progress.setText(_translate("MainWindow", "Extraction progress will be displayed here"))
        self.button_new.setText(_translate("MainWindow", "Generate subtitles"))
        self.button_save.setText(_translate("MainWindow", "Save these subtitles"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_a_file.setText(_translate("MainWindow", "Open a file"))
        self.actionOpen_a_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_multiple_files.setText(_translate("MainWindow", "Open multiple files"))
        self.actionOpen_multiple_files.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionUpdate_subtitle.setText(_translate("MainWindow", "Update subtitle"))
        self.actionUpdate_subtitle.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLatest_state.setText(_translate("MainWindow", "Latest state"))
        self.actionLatest_state.setShortcut(_translate("MainWindow", "Ctrl+R"))
