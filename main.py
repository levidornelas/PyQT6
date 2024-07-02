import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon 
from PyQt6.QtCore import Qt
import requests
from database import conexao_postgresql, cadastrar_aluno

class JanelaPrincipal(QMainWindow): #classe principal que vai conter elementos  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexão com o banco!")
        self.setFixedSize(450,150)
        self.setWindowIcon(QIcon('')) #apontando para imagem que está no mesmo diretório
        self.interface()
        self.show()# faz a tela ser exibida

    def interface(self):
    # Layout principal
        main_layout = QVBoxLayout()

        # Layout do formulário
        form_layout = QFormLayout()

        # Campos do formulário
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.course_input = QLineEdit()

        form_layout.addRow("Nome:", self.name_input)
        form_layout.addRow("Idade:", self.age_input)
        form_layout.addRow("Curso:", self.course_input)

        main_layout.addLayout(form_layout)

        # Botão para cadastrar aluno
        self.submit_button = QPushButton("Cadastrar Aluno")
        self.submit_button.clicked.connect(self.registrar_aluno)
        main_layout.addWidget(self.submit_button)

        # Label para mostrar o status
        self.status_label = QLabel("")
        main_layout.addWidget(self.status_label)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)




    def conectar_banco(self):  
        conection = conexao_postgresql()
        self.status.setText(conection)
        self.adjustSize()

    def registrar_aluno(self):
    # Obter dados do formulário
        name = self.name_input.text()
        age = self.age_input.text()
        course = self.course_input.text()

        # Chamar a função para inserir dados no banco de dados
        status = cadastrar_aluno(name, age, course)
        self.status_label.setText(status)

        self.name_input.clear()
        self.age_input.clear()
        self.course_input.clear()


qt = QApplication(sys.argv) #variavel qt instanciando a classe QApplication: permite usar recursos do SO
app = JanelaPrincipal() #instaciando a classe
sys.exit(qt.exec()) #encerra totalmente a aplicação assim que fechada
