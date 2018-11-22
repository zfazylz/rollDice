import MySQLdb


class UserAuth:

    def __init__(self, login, password):
        self.userID = None
        self.db = None
        self.cursor = None
        self.balance = None
        connect()
        if login(login, password):
            print("ok")
        else:
            print("err")

    def connect(self):
        # Open database connection

        self.db = MySQLdb.connect("sql7.freemysqlhosting.net", "sql7266600", "CMqGsk3z3S", "sql7266600")

    def login(self, name, password):
        self.cursor = db.cursor()
        auth = cursor.execute(
            "SELECT userID, balance from users where name='" + name + "' and password='" + password + "''")
        data = cursor.fetchone()
        self.userID = data[0]
        self.balance = data[1]
        if auth == 1:
            return True
        return False

    def disconnect(self):
        self.db.close()
