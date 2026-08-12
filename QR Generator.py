import os
import sys
import qrcode
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class QRGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.qr_label = QLabel("Enter the url: ", self)
        self.qr_button = QPushButton("Generate", self)
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("https://.com")
        self.initUI()
        self.qr_image = QLabel()
        self.qr_image.setAlignment(Qt.AlignCenter)

    def initUI(self):
        self.setWindowTitle("QR Generator")
        self.resize(400, 400)

        vbox = QVBoxLayout()

        vbox.addWidget(self.qr_label)
        vbox.addWidget(self.url_input)
        vbox.addWidget(self.qr_button)

        self.setLayout(vbox)

        self.setObjectName("Generator")

        self.setStyleSheet("""
        QLabel, QLineEdit {
        font-size: 40px;
        font-weight: bold;
        font-family: Times New Roman;
        }
        QPushButton {
        font-size: 40px;
        background-color: hsl(175, 0%, 60%);
        }
        QPushButton:hover {
        background-color: hsl(175, 0%, 80%);
        }
        """)
        self.qr_button.clicked.connect(self.generate)

    def generate(self):
        url = self.url_input.text().strip()
        if not url:
            self.qr_image.setText("Please enter a url")
            return f"{url}"
        img = qrcode.make(url)

        file_path =os.path.join(os.getcwd(), "qrcode.png")
        img.save(file_path)
        pixmap = QPixmap(file_path)
        self.qr_image.setPixmap(
            pixmap.scaled(
                300, 300, Qt.KeepAspectRatioMode, Qt.SmoothTransformation))
print("QR Code Generated")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QR = QRGenerator()
    QR.show()
    sys.exit(app.exec_())