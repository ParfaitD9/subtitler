import os
import sys
import time
import platform

from pathlib import Path
from typing import Any, Callable

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QTableWidgetItem,
)

from PyQt6.QtCore import pyqtSignal, QThread, QObject
from PyQt6.QtGui import QIcon, QCloseEvent

from assets.py.subtitler import Ui_MainWindow
from controller import File
from models import State


class SubtitlerView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen_multiple_files.triggered.connect(
            lambda: self.openFileDialog(True)
        )

        self._thread = QThread(self)
        self.worker = Worker(app=self)
        self.worker.moveToThread(self._thread)
        self.worker.done.connect(self.load_content_to_box)

        self.__state = State.from_cfg(Path("assets/user.cfg"))
        self.ui.actionOpen_a_file.triggered.connect(lambda: self.openFileDialog(False))
        self.ui.actionUpdate_subtitle.triggered.connect(self.updateFileDialog)
        self.ui.actionLatest_state.triggered.connect(self.reload_state)
        self.ui.button_new.clicked.connect(self.worker.process)
        self.ui.button_new.clicked.connect(self.disable_new_btn)
        self.ui.button_save.clicked.connect(self.saveFileDialog)

        self.ui.tableWidget.setHorizontalHeaderLabels(["Name", "Location", "Size"])
        print("State is", self.state)

        self.setWindowIcon(QIcon("assets/icon.svg"))
        self._thread.start()

    @property
    def state(self):
        self.__state.update(**self.get_current_state())
        return self.__state

    @state.setter
    def state(self, value: State):
        file = value.kwargs.get("filepath")
        files = (
            [
                Path(file),
            ]
            if file is not None
            else []
        )
        is_audio = value.kwargs.get("is_audio", False)
        editing = value.kwargs.get("editing", False)
        lang = value.kwargs.get("lang", "en-US")
        lang = {
            "en-US": "English (USA)",
            "fr-FR": "Français (France)",
            "en-UK": "English (UK)",
            "fr-BE": "Français (Belgique)",
        }.get(lang)

        self.show_files(files)
        self.ui.radio_audio.setChecked(is_audio)
        if editing and files:
            with open(files[0], "r") as f:
                self.ui.text_content.setText(f.read())
        self.__state = value

    def openFileDialog(self, multiples=True) -> list[Path]:
        default_dir = (
            "/home/%s" % os.getenv("USER")
            if platform.system() == "Linux"
            else "C:\\Users"
        )
        current_dir = self.state.kwargs.get("current_dir")
        print("State is", self.__state)
        if multiples:
            fname = QFileDialog.getOpenFileNames(
                self,
                "Open file",
                current_dir if current_dir else default_dir,
                "Videos (*.mp4)",
            )

        else:
            fname = QFileDialog.getOpenFileName(
                self,
                "Open file",
                current_dir if current_dir else default_dir,
                "Videos (*.mp4)",
            )

        if fname[0]:
            files = (
                [Path(p) for p in fname[0]]
                if multiples
                else [
                    Path(fname[0]),  # type: ignore
                ]
            )
            self.show_files(files)
            self.ui.text_content.clear()
            self.ui.label_ann_file.setText(
                "Subtitles will be extracted from files below"
            )

            return files
        return []

    def update_state(self):
        self.state.save()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self._thread.exit()
        self.update_state()
        return super().closeEvent(a0)

    def updateFileDialog(self):
        default_dir = (
            "/home/%s" % os.getenv("USER")
            if platform.system() == "Linux"
            else "C:\\Users"
        )
        current_dir = self.state.kwargs.get("current_dir")
        fname = QFileDialog.getOpenFileName(
            self,
            "Update file",
            current_dir if current_dir else default_dir,
            "Sous-titres (*.srt)",
        )

        if fname[0]:
            file = Path(fname[0])
            self.ui.label_ann_file.setText(
                f"File {file.name} have been opened for editing"
            )
            self.show_files(
                [
                    file,
                ]
            )

            with open(file) as f:
                data = f.read()
                self.ui.text_content.setText(data)

    def load_languages(self):
        langs = [
            ("English (USA)", "en-US"),
            ("English (UK)", "en-US"),
            ("Français (France)", "fr-FR"),
            ("Français (Belgique)", "fr-BE"),
        ]
        for lang, code in langs:
            # self.ui.combo_lang.addItem()
            pass

    def show_files(self, files: list[Path]):
        for _ in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(0)

        for i, path in enumerate(files):
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            data = (
                path.name,
                path.parent.__str__(),
                "%.2f Mo" % (path.stat().st_size / 1024**2),
            )
            for j, item in enumerate(data):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(item))

    def get_current_state(self) -> dict[str, Any]:
        cur_fil = self.ui.tableWidget.item(0, 0)
        cur_dir = self.ui.tableWidget.item(0, 1)

        lang = {
            "English (USA)": "en-US",
            "English (UK)": "en-UK",
            "Français (France)": "fr-FR",
            "English (Belgique)": "fr-BE",
        }.get(self.ui.combo_lang.currentText())
        is_audio = False
        if self.ui.radio_audio.isChecked():
            is_audio = True
        editing = bool(self.ui.text_content.toPlainText().strip())

        state = {
            "filepath": os.path.join(cur_dir.text(), cur_fil.text())
            if cur_dir and cur_fil
            else None,
            "current_dir": cur_dir.text() if cur_dir else None,
            "lang": lang,
            "is_audio": is_audio,
            "editing": editing,
        }

        return state

    def reload_state(self):
        self.state = State.from_cfg()
        print("State updated")

    def load_content_to_box(self, content: list[str]):
        txt, name = content
        self.ui.text_content.setText(txt)
        self.ui.label_ann_content.setText(f"Subtitles extrated from {name} are below :")
        self.ui.button_new.setDisabled(False)

    def saveFileDialog(self):
        state = self.get_current_state()
        path = Path(state["filepath"])

        save_name, _ = QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFilename()",
            path.with_suffix(".srt").__str__(),
            "Subtitles (*.srt)",
        )
        if save_name:
            with open(save_name, "w") as f:
                f.write(self.ui.text_content.toPlainText())

    def disable_new_btn(self):
        self.ui.button_new.setDisabled(True)


class Worker(QObject):
    done = pyqtSignal(list)

    def __init__(self, parent=None, app: SubtitlerView = None) -> None:  # type: ignore
        super().__init__(parent)
        self._parent = app

    def process(self):
        print("Extraction started ...")

        data = self._parent.get_current_state()  # type: ignore
        print("State is", data)
        self._parent.ui.label_progress.setText("Extrating ...")
        self._parent.ui.progressBar.setValue(52)
        file = File(**data)
        content = file.generate_srt(save=False)
        time.sleep(5)
        self.done.emit([content, file.path.name])
        self._parent.ui.label_progress.setText("Extraction finished !")
        self._parent.ui.progressBar.setValue(100)
        print("Extraction finished !")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SubtitlerView()
    w.show()
    sys.exit(app.exec())
