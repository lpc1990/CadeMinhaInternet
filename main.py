import sys
import socket
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel


def check_internet():
    try:
        # Tenta se conectar com o servidor do Google
        socket.create_connection(("www.google.com", 80))
        return 0
    except OSError:
        return 1


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadê minha internet?")
        self.label = QLabel("Olá mundo")
        self.setCentralWidget(self.label)
        self.setGeometry(100, 100, 500, 500)  # Define o tamanho da janela
        self.setFixedSize(500, 500) # Fixa o tamanho da janela
        status_internet = self.check_internet()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = JanelaPrincipal()
    windows.show()
    sys.exit(app.exec_())
