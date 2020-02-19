# TODO:
# 1 - create a connection
# 2 - create a cursor object
# 3 - create the query
# 4 - execute the query
# 5 - commit the connection (conn.commit())
# 6 - cursor.fetchall() which returns all the records

import psycopg2
import pandas as pd

# Establishes connection with the host/dbase
conn = psycopg2.connect(dbname='ejfhwlkg',
                        user='ejfhwlkg',
                        password='6VxghFQnfeb1WjzVG-mMIv5knSUG8If7',
                        host='rajje.db.elephantsql.com')
cursor = conn.cursor()
# query = 'SELECT * from test_table;'
# cursor.execute(query)
# print(cursor.fetchall())
df = pd.read_csv('titanic.csv')

print(df.shape)
# print(df.columns)

query = '''
        CREATE TABLE Titanic (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(100),
        Sex VARCHAR(10),
        Age INT,
        Siblings INT,
        Parents INT,
        Fare REAL
        );
        '''

# Execute creates the table...  In this case we are executing the string variable 'query'
cursor.execute(query)

def get_insert_statement(row):
    base = 'INSERT INTO Titanic (Survived, Pclass, Name, Sex, Age, Siblings, Parents, Fare) VALUES '
    row[2] = row[2].replace("'", "")
    return base + str(tuple(row)) + ";"

for row in df.values:
    query = get_insert_statement(row)
    print(query)
    cursor.execute(query)

#Save/commit the changes
conn.commit()


query = 'SELECT COUNT(*) FROM Titanic'
cursor.execute(query)

# Fetchall returns all of the records.
print(cursor.fetchall())