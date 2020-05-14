import pymysql
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id



#SELECT * FROM Таблица WHERE Колонка = 'Значение
#UPDATE Таблица SET Колонка = 'Значение' WHERE Колонка = 'Значение'
#INSERT INTO Таблица (Колонка1, Колонка2) VALUES ('Значение1', 'Значение2')
#Путь к файлам базы данных
#C:\ProgramData\MySQL\MySQL Server 8.0\Data\notesbot


def insertcash(uid, cash):
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    insertcash = """INSERT INTO cash(userid, cash) VALUES (%i, '%s')"""%(uid, cash)
    #deletecash = """UPDATE notes SET buff='' WHERE buff='cn'"""
    cursor.execute(insertcash)
    #cursor.execute(deletecash)
    conn.commit()
    selectcash = """SELECT cash FROM cash WHERE userid = %i"""%uid
    cursor.execute(selectcash)
    result = cursor.fetchone()
    return(result['cash'])
    cursor.close()
    conn.close()

def insertnote(uid, text):
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    insertnote = """INSERT INTO notes(userid, notes, stat) VALUES (%i, '%s', 1)"""%(uid, text)
    cursor.execute(insertnote)
    conn.commit()
    deletecash = """DELETE FROM cash WHERE ((userid = %i) and (cash != ''))"""%uid
    cursor.execute(deletecash)
    deleteincrement = """ALTER TABLE cash AUTO_INCREMENT = 1"""
    cursor.execute(deleteincrement)
    conn.commit()

    cursor.close()
    conn.close()

def deletecash(uid):
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    deletecash = """DELETE FROM cash WHERE ((userid = %i) and (cash != ''))"""%uid
    cursor.execute(deletecash)
    deleteincrement = """ALTER TABLE cash AUTO_INCREMENT = 1"""
    cursor.execute(deleteincrement)
    conn.commit()

    cursor.close()
    conn.close()

def checkcash(uid):
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    selectcash = """SELECT cash FROM cash WHERE userid = %i"""%uid
    cursor.execute(selectcash)
    result = cursor.fetchone()
    #print(result['cash'])
    try:
        return(result['cash'])
    except TypeError:
        return('wait')
    cursor.close()
    conn.close()

def selectusernote(uid):
    #uid = 127949564
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    notes = []
    titlenotes = []
    selectusernote = """SELECT idnotes, notes, stat FROM notes WHERE ((userid = %i) and (stat = 1))"""%uid
    cursor.execute(selectusernote)
    result = cursor.fetchall()
    for i in result:
        notes.append(str(i['idnotes']) + '. ' + i['notes'])
    for i in notes:
        title = i.split()
        try:
            titlenotes.append(title[0] + ' ' + title[1] + ' ' + title[2] + '...')
        except IndexError:
            titlenotes.append(title[0] + ' ' + title[1])
    return titlenotes
    #print(notes)

def selectuserfullnote(num, uid):
    #num = 1
    #uid = 127949564
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    note = """SELECT idnotes, userid, notes FROM notes WHERE ((idnotes = %i) and (userid = %i) and (stat = 1))"""%(num, uid)
    cursor.execute(note)
    result = cursor.fetchall()
    '''deletecash = """DELETE FROM cash WHERE ((userid = %i) and (cash != ''))"""%uid
    cursor.execute(deletecash)
    deleteincrement = """ALTER TABLE cash AUTO_INCREMENT = 1"""
    cursor.execute(deleteincrement)
    conn.commit()'''

    cursor.close()
    conn.close()
    try:
        return(result[0]['notes'])
    except IndexError:
        return('Такой заметки не существует')

def editnotes(uid, num, ednote):
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    update = """UPDATE notes SET notes = '%s' WHERE ((idnotes = %i) and (userid = %i))"""%(ednote, num, uid)
    cursor.execute(update)
    conn.commit()
    cursor.close()
    conn.close()

def deletenotes(uid, num):
    conn = pymysql.connect(
    host = 'localhost',
    user = 'tgbot',
    password = 'thxleha',
    db = 'notesbot',
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    delete = """UPDATE notes SET stat = 0 WHERE ((idnotes = %i) and (userid = %i))"""%(num, uid)
    cursor.execute(delete)
    conn.commit()
    cursor.close()
    conn.close()