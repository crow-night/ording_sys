from basic import MysqlHelper
import config, pymysql

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from riderOrder where riderOrder_id = %s"
sql_all = "select * from riderOrder"
sql_insert = "INSERT INTO riderOrder ( riderOrder_id, riderOrder_userName, riderOrder_name, riderOrder_age, riderOrder_gender, riderOrder_defaultAddress, riderOrder_phone, riderOrder_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO riderOrder ( riderOrder_account, riderOrder_password, riderOrder_name, riderOrder_age, riderOrder_gender, riderOrder_defaultAddress, riderOrder_phone, riderOrder_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_delete = "delete from riderOrder where riderOrder_id = %s"
sql_modify_password = "update riderOrder set riderOrder_password = %s where riderOrder_account = %s"

#根据riderOrder_id查找数据
def get_riderOrder_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_riderOrder_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_riderOrder(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_riderOrder(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_riderOrder_id(params=()):
    MysqlHelper.delete(sql_delete, params)

#根据就账号修改密码
def modify_password(params=()):
    MysqlHelper.update(sql_modify_password, params)


def find_all():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM riderOrder"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

def find_complete():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM riderOrder where riderOrder_status = '已完成'"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

def find_incomplete():
    conn = pymysql.connect(host=config.HOST, user='root', password='password', db='orderingsys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM riderOrder where riderOrder_status != '已完成'"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return u

if __name__ == '__main__':
    print(find_incomplete())
    print(find_complete())