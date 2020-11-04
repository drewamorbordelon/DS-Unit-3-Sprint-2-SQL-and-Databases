import csv, sqlite3

conn = sqlite3.connect("buddymove.db")
curs - conn.cursor()

curs.execute(
    'CREATE TABLE bd(User Id, Sports, Religious, NatureTheatre, Shopping, Picnic);'
)

f =open('module1-introduction-to-sql/assign/buddymove_holiday.csv')
rows = csv.reader()
curs.executemany('INSERT INTO db VALUES(?, ?, ?, ?, ?, ?, ?', rows)

curs.execute("SELECT * FROM db")
print(curs.fetchall())

conn.commit()
conn.close()

print(rows)