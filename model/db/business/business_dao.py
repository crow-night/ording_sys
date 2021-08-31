from basic import MysqlHelper
import config

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from business where business_account = %s"
sql_all = "select * from business"
sql_insert = "INSERT INTO business ( business_account, business_password, business_Name, business_Address, business_phone, business_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO business ( business_account, business_password, business_Name, business_Address, business_phone, business_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s )"
sql_delete = "delete from business where business_account = %s"

#根据business_id查找数据
def get_business_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_business_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_business(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_business(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_business_account(params=()):
    MysqlHelper.delete(sql_delete, params)

