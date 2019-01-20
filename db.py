import pymysql
import random

connect = pymysql.connect(host='localhost',
                          user='root',
                          password='Mysqlpass1!',
                          db='mydb')
connect.autocommit(1)

# данные в формате:
# Айди, имя, пол, логин, пароль, дата рождения, регион, email, тип, айди компетенции, айди чемпионата
user_data = []


def log_in(login, password):
    curr = connect.cursor()
    user_data.clear()
    query = "select * from Users where id_number = '%s' and '%s' = password" % (login, password)
    curr.execute(query)
    for i in curr:
        for item in i:
            user_data.append(item)
    if len(user_data) > 0:
        user_data.append(int(get_current_championship().split('.')[0]))
    print(user_data)
    # get_all_competitors_experts(0, 0, 2)



def get_all_competences():  # возвращает массив строк в формате: idКомпетенции. НазваниеКомпетенции.
    curr = connect.cursor()
    query = "select id, name from Competence where id != 999 order by id"
    curr.execute(query)
    data = []
    for i in curr:
        temp = ""
        for item in i:
            temp += str(item) + '. '
        data.append(temp)

    print("all competence = " + str(data))
    return data


def get_all_competitors_experts(id_competence, id_user, id_type):
    # двумерный массив представленный данными:
    # Айди, имя, пол, логин, пароль, дата рождения, регион, email, айди компетенции
    # если компетенция нам не важна, пишем 0, id_user аналогично
    curr = connect.cursor()
    query = "call show_competitors(%s,%s,%s,%s)" % (
        str(get_current_championship().split('.')[0]), str(id_competence), str(id_user), str(id_type))

    curr.execute(query)
    data = []
    for i in curr:
        temp = []
        for item in i:
            temp.append(str(item))
        data.append(temp)

    print("get_all_competitors = " + str(data))
    return data


def get_all_championship():
    # двумерный массив представленный данными:
    # айди, название, регион, число участников, дата проведения

    curr = connect.cursor()
    query = "SELECT * from Championships;"
    curr.execute(query)
    data = []
    for i in curr:
        temp = []
        for item in i:
            temp.append(str(item))
        data.append(temp)

    print("get_all_championships = " + str(data))
    return data


def get_current_championship():  # возвращает строку в формате: idЧемпионата. НазваниеЧемпионата.
    curr = connect.cursor()
    query = "call next_championship()"
    curr.execute(query)
    res = ""
    for i in curr:
        for item in i:
            res += str(item) + '. '
    print("Следующий чемпионат = " + res)
    return res


def change_password(password):
    curr = connect.cursor()
    query = "call change_password(%s,'%s')" % (str(user_data[0]), password)
    curr.execute(query)
    print("change_password = " + query)


def add_expert(data):  # data = [name, gender,region,email,pass,birth,competence]
    curr = connect.cursor()
    login = str(data[5].split('-')[0]) + str(data[6]) + str(random.randint(1, 100)) + str(4)
    query = "call add_expert('%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s)" % (
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], login, 4,
        get_current_championship().split('.')[0])
    print(query)
    curr.execute(query)


def add_competitor(data):  # data = [name, gender,region,email,pass,birth,competence]
    curr = connect.cursor()
    login = str(data[5].split('-')[0]) + str(data[6]) + str(random.randint(1, 100)) + str(2)
    query = "call add_competitor('%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s)" % (
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], login, 2,
        get_current_championship().split('.')[0])
    curr.execute(query)
    query = "call reg_competitor_result('%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s)" % (
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], login, 2,
        get_current_championship().split('.')[0])
    curr.execute(query)


def add_coordinator(data):  # data = [name, gender,region,email,pass,birth]
    curr = connect.cursor()
    login = str(data[5].split('-')[0]) + str(data[6]) + str(random.randint(1, 100)) + str(3)
    query = "call add_competitor('%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s)" % (
        data[0], data[1], data[2], data[3], data[4], data[5], 999, login, 3,
        get_current_championship().split('.')[0])
    curr.execute(query)


def add_volunteer(data):  # data = [name varchar(45), gender varchar(1), region varchar(45), competence int]
    curr = connect.cursor()

    query = "call add_volunteer('%s','%s','%s',%s)" % (data[0], data[1], data[2], data[3])
    print(query)
    curr.execute(query)
    query = "call add_volunteer_to_competence('%s','%s','%s',%s)" % (data[0], data[1], data[2], data[3])
    curr.execute(query)


def add_sponsor(data):  # data = [name varchar(45), gender varchar(1), region varchar(45), competence int]

    curr = connect.cursor()
    query = "call add_sponsor('%s','%s','%s',%s)" % (data[0], data[1], data[2], data[3])
    print(query)
    curr.execute(query)
    query = "call add_sponsor_to_competence('%s','%s','%s',%s)" % (data[0], data[1], data[2], data[3])
    curr.execute(query)


def add_marks(data):  # data = [id_u int, module int, mark int]
    curr = connect.cursor()
    query = "call add_marks(%s,%s,%s,%s,%s)" % (
        data[0], data[1], data[2], get_current_championship().split('.')[0], str(user_data[len(user_data) - 2]))
    print(query)
    curr.execute(query)


def show_marks(data):  # data = id_user если нужны все, тогда id = 0
    # результат для всех учатсников: двумерный массив с полями id_user, module, result
    # для одного module, result
    curr = connect.cursor()
    query = ""
    result = []
    if data == 0:
        query = "call show_all_marks(%s,%s)" % (
            get_current_championship().split('.')[0], str(user_data[len(user_data) - 2]))
    else:
        query = "call show_marks_user(%s,%s,%s)" % (
            data, get_current_championship().split('.')[0], str(user_data[len(user_data) - 2]))
    curr.execute(query)
    for i in curr:
        temp = []
        for j in i:
            temp.append(j)
        result.append(temp)
    return result


def get_competence_info(data):  # data = id_компетенции
    # результат одномерный массив с полями айди, название, описание, план,расписание инфраструктура
    curr = connect.cursor()
    query = "select * from Competence where id = %s" % (data)
    curr.execute(query)
    result = []
    for i in curr:
        for j in i:
            result.append(j)
    print(result)
    return result


def change_vol_competence(data):  # data = [айди волонтера. айди компетенции]
    curr = connect.cursor()
    query = "call change_vol_competence(%s,%s)" % (data[0], data[1])
    curr.execute(query)
    print(query)


def get_all_volunteers():  # возвращает двумерный массив волонтеров в формате:
    #  id волонтера. имя, регион, пол.
    curr = connect.cursor()
    query = 'select * from Volunteer'
    curr.execute(query)
    data = []
    for i in curr:
        temp = []
        for item in i:
            temp.append(item)
        data.append(temp)
    curr = connect.cursor()
    return data


def get_all_sponsors():  # возвращает двумерный массив спонсоров в формате:
    #  id спонсора. имя, регион, пол.
    curr = connect.cursor()
    query = 'select * from Sponsors'
    curr.execute(query)
    data = []
    for i in curr:
        temp = []
        for item in i:
            temp.append(item)
        data.append(temp)
    return data


def get_sponsors(comp):  # принимает номер компетенции в формате строки
    # id спонсора. имя, регион, пол.
    curr = connect.cursor()
    query = 'call get_sponsors(%s)' % comp
    curr.execute(query)
    data = []
    for i in curr:
        temp = []
        for item in i:
            temp.append(item)
        data.append(temp)
    return data


def get_volunteers(comp):
    # принимает номер компетенции в формате строки
    # id волонтера. имя, регион, пол.
    curr = connect.cursor()
    query = 'call get_volunteer(%s)' % comp
    curr.execute(query)
    data = []
    for i in curr:
        temp = []
        for item in i:
            temp.append(item)
        data.append(temp)
    return data
# add_expert(['эксперт', 'Ж', 'Регион', 'почта@почта', 'пароль', '1990-01-01', 2])
# add_competitor(['уч', 'Ж', 'Регион', 'почта@почта', 'пароль', '1990-01-01', 2])
# add_coordinator(['корди', 'Ж', 'Регион', 'почта@почта', 'пароль', '1990-01-01', 2])
# get_all_competitors_experts(0, 0, 2)
# get_competence_info(2)
# add_sponsor(['тест','Ж','Рус','2'])
# add_volunteer(['ТЕСТ','Ж','Россия','2'])
