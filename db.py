#Arquivo Auxiliar para 'main.py', que realiza a conexão com um banco de dados realizado pelo 'railway', uma solução que hospeda bancos na nuvem gratuitamente.

import psycopg2

from urllib.parse import urlparse

# URL de conexão do banco (Railway)
DATABASE_URL = "postgresql://postgres:LsViiuogBzkUISNbtKTpOHWNrYmNefnV@roundhouse.proxy.rlwy.net:36019/railway"

# Extrair as informações de conexão da URL(database, usuário, password,etc)
url = urlparse(DATABASE_URL)

# Credenciais do banco de dados
DATABASE = url.path[1:]
USER = url.username
PASSWORD = url.password
HOST = url.hostname
PORT = url.port

def conexao_postgresql():
    try:
        # Conexão ao banco de dados PostgreSQL
        conexao = psycopg2.connect(
            database= DATABASE,
            user= USER,
            password= PASSWORD,
            host= HOST,
            port= PORT
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT version();")#buscando a versão do PostgreSQL
        db_versao = cursor.fetchone() # atribui o resultado a variável db_versao
        cursor.close()
        conexao.close()
        return (f"Conectado ao PostgreSQL!")
    except Exception as e:
        return f"Erro ao conectar ao PostgreSQL: {e}"

def cadastrar_aluno(nome, idade, curso):
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = connection.cursor()
        # Inserir dados do aluno
        inserir_sql = """INSERT INTO alunos1 (nome, idade, curso) VALUES (%s, %s, %s)"""
        gravar_insert = (nome, idade, curso)
        cursor.execute(inserir_sql, gravar_insert)
        connection.commit() #garantir que todas as alterações sejam refletidas permanentemente no banco.
        cursor.close()
        connection.close()
        return "Aluno cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar aluno: {e}"
