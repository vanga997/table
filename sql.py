import sqlite3

class SqlDB:
    # Список data записаваем в БД  с названием name
    def save(self, data, name):

        conn = sqlite3.connect(name)
        cur = conn.cursor()

        cur.execute("""DROP TABLE IF EXISTS array;""")
        cur.execute("""CREATE TABLE array(
                    id INT PRIMARY KEY,
                    num INT)
                    """)

        conn.commit()
        for i in range(len(data)):
            cur.execute("INSERT INTO array(id, num) VALUES('" + str(i) + "', '" + str(data[i]) + "');")
            conn.commit()

    # Загружает БД из файла находящийся в path
    def load(self, path):

        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM array;")
        return cur
