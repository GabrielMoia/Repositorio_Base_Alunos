import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)
        
def inserir_aluno(nome, idade, email, curso):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO alunos (nome, idade, email, curso) VALUES (?, ?, ?, ?)', (nome, idade, email, curso))
        conn.commit()
        return cur.lastrowid
    
if __name__ == '__main__':
    #bem vindo ao banco de dados
    print("### BEM VINDO AO BANCO DE DADOS ###")
    nome_aluno = input("Digite o nome do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    email_aluno = input("Digite o email do aluno: ")
    curso_aluno = input("Digite o curso do aluno: ")

    novo_id = inserir_aluno(nome_aluno, idade_aluno, email_aluno, curso_aluno)

    print(f"Aluno inserido com sucesso! ID: {novo_id}")