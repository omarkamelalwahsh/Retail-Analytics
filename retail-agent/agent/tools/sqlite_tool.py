import sqlite3

class SQLiteTool:
    def __init__(self, db_path="data/northwind.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def query(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        return [tuple(row) for row in cur.fetchall()]
