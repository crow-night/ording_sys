from basic import MysqlHelper
import config
import pymysql

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from userOrder where userOrder_account = %s"
sql_all = "select * from userOrder"
sql_insert = "INSERT INTO userOrder ( userOrder_account, userOrder_password, userOrder_name, userOrder_age, userOrder_gender, userOrder_defaultAddress, userOrder_phone, userOrder_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO userOrder ( userOrder_account, userOrder_password, userOrder_name, userOrder_age, userOrder_gender, userOrder_defaultAddress, userOrder_phone, userOrder_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_delete = "delete from userOrder where userOrder_id = %s"
sql_modify_password = "update userOrder set userOrder_password = %s where userOrder_account = %s"

#根据userOrder_id查找数据
def get_userOrder_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_userOrder_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_userOrder(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_userOrder(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_userOrder_id(params=()):
    MysqlHelper.delete(sql_delete, params)

#根据就账号修改密码
def modify_password(params=()):
    MysqlHelper.update(sql_modify_password, params)

def find_all():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM usersOrder"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

def find_complete():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM usersOrder where usersOrder_status = '已完成'"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

def find_incomplete():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM usersOrder where usersOrder_status != '已完成'"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

if __name__ == '__main__':
    # print(find_incomplete())
    print(find_complete())
