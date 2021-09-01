from basic import MysqlHelper
import config
import pymysql

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from dishes where dishes_id = %s"
sql_all = "select * from dishes"
sql_insert = "INSERT INTO dishes ( dishes_account, dishes_password, dishes_name, dishes_age, dishes_gender, dishes_phone, dishes_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO dishes ( dishes_account, dishes_password, dishes_name, dishes_age, dishes_gender, dishes_phone, dishes_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s )"
sql_delete = "delete from dishes where dishes_id = %s"
# sql_password = "update dishes set dishes_password = %s where dishes_account= %s"
# sql_phone = "update dishes set dishes_phone = %s where dishes_aoocunt = %s"
# sql_name = "update dishes set dishes_name = %s where dishes_account = %s"
# sql_age = "update dishes set dishes_age = %s where dishes_age = %s"
# sql_gender = "update dishes set dishes_gender where dishes_gender = %s"

#根据dishes_account查找数据
def get_dishes_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_dishes_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_dishes(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_dishes(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_dishes_id(params=()):
    MysqlHelper.delete(sql_delete, params)

def find_all():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM dishes"
    # sql = "select * from business"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

# if __name__ == '__main__':
#     data = get_dishes_all()
#     print(type(data))
#     print(data)
#     for i in data:
#         print(i["dishes_id"])
#         print(i["dishes_name"])








