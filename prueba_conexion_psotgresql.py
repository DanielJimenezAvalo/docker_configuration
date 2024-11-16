import psycopg2

connection=psycopg2.connect(user='admin',
                            password='secret',
                            host='db',
                            port=5432,
                            database='postgres_db')

cursor=connection.cursor()

query='''SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public' '''

cursor.execute(query)

table_name=[]
for row in cursor:
    table_name.append(row)
    print(row)

