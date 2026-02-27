import psycopg2 

conn = psycopg2.connect(database= "postgres", user = "postgres", password = "admin123", host = "localhost")
print("conexão com banco de dados aberta com sucesso!")
cur=conn.cursor()
cur.execute("""select * from public."AGENDA";""")
registro = cur.fetchone()#fetchone() pega só um registro, fetchall() pega tudo
print(registro) 
conn.commit()
print("seleção realizada com sucesso!")
