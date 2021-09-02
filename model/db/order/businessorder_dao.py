from basic import MysqlHelper
import config, pymysql

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from businessOrder where businessOrder_id = %s"
sql_all = "select * from businessOrder"
sql_insert = "INSERT INTO businessOrder ( businessOrder_account, businessOrder_password, businessOrder_name, businessOrder_age, businessOrder_gender, businessOrder_defaultAddress, businessOrder_phone, businessOrder_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO businessOrder ( businessOrder_account, businessOrder_password, businessOrder_name, businessOrder_age, businessOrder_gender, businessOrder_defaultAddress, businessOrder_phone, businessOrder_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_delete = "delete from businessOrder where businessOrder_id = %s"
sql_modify_password = "update businessOrder set businessOrder_password = %s where businessOrder_account = %s"

#根据businessOrder_id查找数据
def get_businessOrder_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_businessOrder_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_businessOrder(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_businessOrder(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_businessOrder_id(params=()):
    MysqlHelper.delete(sql_delete, params)

#根据就账号修改密码
def modify_password(params=()):
    MysqlHelper.update(sql_modify_password, params)

def find_all():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM businessOrder"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

def find_complete():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM businessOrder where businessOrder_status = '已完成'"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

def find_incomplete():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM businessOrder where businessOrder_status != '已完成'"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

if __name__ == '__main__':
    print(find_complete())
    print(find_incomplete())
