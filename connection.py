from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://prod:Psytrixx2121#@localhost:3306/cinema")
conn = engine.connect()
response = conn.execute('SELECT * FROM filmes;')

for row in response:
    print(row)
    