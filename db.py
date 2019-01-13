import pymysql

connect = pymysql.connect(host='localhost',
                          user='root',
                          password='Mysqlpass1!',
                          db='mydb')


def log_in(login, password):
    curr = connect.cursor()
    login = "'" + login + "'"
    password = "'" + password + "'"

    query = "select * from Users where idNumber = " + login + " and password = " + password
    curr.execute(query)
    user_data = []
    for i in curr:
        for item in i:
            user_data.append(item)
    return user_data
