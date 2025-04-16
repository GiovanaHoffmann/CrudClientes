import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError, Error

load_dotenv()

class TransactionObject:
    # Configurações do PostgreSQL com valores padrão
    database = os.getenv("DB_NAME", "crud_clients")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    
    conn = None
    cur = None
    connected = False
    
    def connect(self):
        self.conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False

    def execute(self, sql, params=None):
        if not self.connected:
            self.connect()
            
        if params is None:
            self.cur.execute(sql)
        else:
            self.cur.execute(sql, params)
        return True

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        return False

def initDB():
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                cpf TEXT UNIQUE NOT NULL CHECK (LENGTH(cpf) = 11)
            )
        """)
        trans.persist()
    finally:
        trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    try:
        cpf = ''.join(filter(str.isdigit, cpf))  # Remove formatação
        trans.connect()
        trans.execute(
            "INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (%s, %s, %s, %s)",
            (nome, sobrenome, email, cpf)
        )
        trans.persist()
    finally:
        trans.disconnect()

def view():
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("SELECT * FROM clientes ORDER BY nome, sobrenome")
        return trans.fetchall()
    finally:
        trans.disconnect()

def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute(
            """SELECT * FROM clientes 
            WHERE nome ILIKE %s OR sobrenome ILIKE %s 
            OR email ILIKE %s OR cpf LIKE %s
            ORDER BY nome, sobrenome""",
            (f"%{nome}%", f"%{sobrenome}%", f"%{email}%", f"%{cpf}%")
        )
        return trans.fetchall()
    finally:
        trans.disconnect()

def delete(id):
    trans = TransactionObject()
    try:
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id = %s", (id,))
        trans.persist()
    finally:
        trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObject()
    try:
        cpf = ''.join(filter(str.isdigit, cpf))  # Remove formatação
        trans.connect()
        trans.execute(
            """UPDATE clientes 
            SET nome = %s, sobrenome = %s, email = %s, cpf = %s 
            WHERE id = %s""",
            (nome, sobrenome, email, cpf, id)
        )
        trans.persist()
    finally:
        trans.disconnect()

initDB()