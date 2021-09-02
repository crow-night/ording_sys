from basic import MysqlHelper
import config

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from riders where riders_account = %s"
sql_all = "select * from riders"
sql_insert = "INSERT INTO riders ( riders_account, riders_password, riders_name, riders_age, riders_gender, riders_phone, riders_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO riders ( riders_account, riders_password, riders_name, riders_age, riders_gender, riders_phone, riders_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s )"
sql_delete = "delete from riders where riders_id = %s"
sql_password = "update riders set riders_password = %s where riders_account= %s"
sql_phone = "update riders set riders_phone = %s where riders_aoocunt = %s"
sql_name = "update riders set riders_name = %s where riders_account = %s"
sql_age = "update riders set riders_age = %s where riders_age = %s"
sql_gender = "update riders set riders_gender where riders_gender = %s"

#根据riders_account查找数据
def get_riders_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_riders_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_riders(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_riders(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_riders_id(params=()):
    MysqlHelper.delete(sql_delete, params)

