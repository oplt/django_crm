import psycopg2

# forming the connection
conn = psycopg2.connect(
                        database="djangocrm", user='django',
                        password='123456', host='127.0.0.1', port='5432'
                    )

# Setting auto commit to True
conn.autocommit = True
# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

sql = '''SELECT * FROM employee;'''

# executing the sql command
cursor.execute(sql)
results = cursor.fetchall()