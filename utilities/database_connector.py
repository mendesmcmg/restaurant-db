import psycopg2

class DatabaseConnector:
  def __init__(self, dbname):
    self._connection = psycopg2.connect(database=dbname)
    self._cursor = self._connection.cursor()

  def getCursor(self):
    return self._cursor

  def commit(self):
    self._connection.commit()

  def disconnect(self):
    self._connection.close()
    self._cursor.close()