#Código que se utiliza da API do Instituto Brasileiro de Geografia e estatística, para consultar o endereço, usando como base o CEP fornecido pelo usuário. Botão de 'salvar' para inserir no banco existente, mas ainda não funcional.

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import requests

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta CEP!")
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('s.png'))
        self.interface()
        self.show()

    def interface(self):
        principal = QWidget(self)
        self.setCentralWidget(principal)

        layout_principal = QGridLayout()

    
        self.setStyleSheet("""
            QLabel {
                font-size: 12px;
            }
            QLineEdit {
                padding: 5px;
                font-size: 12px;
            }
            QPushButton {
                background-color: #5cb85c;
                color: black;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: green;
                color: white;
            }
        """)
        

        self.cep_texto = QLabel('Digite o CEP:')
        self.cep_input = QLineEdit()
        self.cep_input.setInputMask('00000-000')
        self.cep_input.editingFinished.connect(self.consulta_cep)

    
        self.logradouro_texto = QLabel('Rua:')
        self.logradouro_input = QLineEdit()

       
        self.numerocasa = QLabel('Número:')
        self.casa_input = QLineEdit()

     
        self.bairro_texto = QLabel('Bairro:')
        self.bairro_input = QLineEdit()

       
        self.cidade_texto = QLabel('Cidade:')
        self.cidade_input = QLineEdit()

        
        self.estado_texto = QLabel('Estado:')
        self.estado_input = QLineEdit()

       
        self.botaosalvar = QPushButton('Salvar')

        layout_principal.addWidget(self.cep_texto, 1, 0)
        layout_principal.addWidget(self.cep_input, 1, 1, 1, 2)

        layout_principal.addWidget(self.logradouro_texto, 2, 0)
        layout_principal.addWidget(self.logradouro_input, 2, 1, 1, 2)

        layout_principal.addWidget(self.numerocasa, 3, 0)
        layout_principal.addWidget(self.casa_input, 3, 1, 1, 2)

        layout_principal.addWidget(self.bairro_texto, 4, 0)
        layout_principal.addWidget(self.bairro_input, 4, 1, 1, 2)

        layout_principal.addWidget(self.cidade_texto, 5, 0)
        layout_principal.addWidget(self.cidade_input, 5, 1, 1, 2)

        layout_principal.addWidget(self.estado_texto, 6, 0)
        layout_principal.addWidget(self.estado_input, 6, 1, 1, 2)

        layout_principal.addWidget(self.botaosalvar, 7, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)

        principal.setLayout(layout_principal)

    def consulta_cep(self):
        cep = self.cep_input.text().strip().replace('-', '')

        if len(cep) != 8 or not cep.isdigit():
            QMessageBox.warning(self, 'Atenção', 'Por favor insira um CEP válido.')
            return

        try:
            resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            resposta.raise_for_status()
            dados = resposta.json()

            if 'erro' in dados:
                QMessageBox.warning(self, 'Atenção', 'CEP não encontrado.')
            else:
                self.logradouro_input.setText(dados.get('logradouro', ''))
                self.bairro_input.setText(dados.get('bairro', ''))
                self.cidade_input.setText(dados.get('localidade', ''))
                self.estado_input.setText(dados.get('uf', ''))

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Erro', 'Houve um erro ao procurar o CEP.')

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
