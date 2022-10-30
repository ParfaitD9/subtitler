import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt6.QtGui import QIcon
from assets.py.subtitler import Ui_MainWindow


class SubtitlerView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen_multiple_files.triggered.connect(
            lambda: self.openFileDialog(True)
        )

        self.ui.actionOpen_a_file.triggered.connect(lambda: self.openFileDialog(False))
        self.ui.actionUpdate_subtitle.triggered.connect(self.updateFileDialog)

        self.ui.tableWidget.setHorizontalHeaderLabels(["Name", "Location", "Size"])

        self.setWindowIcon(QIcon("assets/logo.svg"))

    def openFileDialog(self, multiples=True) -> list[Path]:
        if multiples:
            fname = QFileDialog.getOpenFileNames(
                self,
                "Open file",
                "/home/parfaitd/Videos/Rust/Holochain",
                "Videos (*.mp4)",
            )

        else:
            fname = QFileDialog.getOpenFileName(
                self,
                "Open file",
                "/home/parfaitd/Videos/Rust/Holochain",
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
            self.ui.label_ann_file.setText(
                "Des sous-titres seront générés pour les fichiers suivant : "
                if multiples
                else "Des sous-titres seront générés pour le fichier suivant : "
            )

            return files
        return []

    def updateFileDialog(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "/home/parfaitd/Videos/Rust/Holochain",
            "Sous-titres (*.srt)",
        )

        if fname[0]:
            file = Path(fname[0])
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
        for i, path in enumerate(files):
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            data = (
                path.name,
                path.parent.__str__(),
                "%.2f Mo" % (path.stat().st_size / 1024**2),
            )
            for j, item in enumerate(data):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(item))

    def saveFileDialog(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SubtitlerView()
    w.show()
    sys.exit(app.exec())
