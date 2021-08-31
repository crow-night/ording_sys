from basic import MysqlHelper
import config

MysqlHelper = MysqlHelper(config.HOST, config.USER, config.PWSSED, config.DATABASE, config.AUTH_PLUGIN_MAP)
sql_one = "select * from users where users_account = %s"
sql_all = "select * from users"
sql_insert = "INSERT INTO users ( users_account, users_password, users_name, users_age, users_gender, users_defaultAddress, users_phone, users_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_update = "INSERT INTO users ( users_account, users_password, users_name, users_age, users_gender, users_defaultAddress, users_phone, users_headPortrait ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
sql_delete = "delete from users where users_id = %s"
sql_modify_password = "update users set users_password = %s where users_account = %s"

#根据users_id查找数据
def get_users_one(params=()):
    result = MysqlHelper.get_one(sql_one, params)
    return result

#查找全部数据
def get_users_all():
    result = MysqlHelper.get_all(sql_all)
    return result

#插入数据
def insert_users(params=()):
    MysqlHelper.insert(sql_insert, params)

#更新数据
def update_users(params=()):
    MysqlHelper.update(sql_update, params)

#删除数据
def delete_users_id(params=()):
    MysqlHelper.delete(sql_delete, params)

#根据就账号修改密码
def modify_password(params=()):
    MysqlHelper.update(sql_modify_password, params)

# if __name__ == '__main__':
#     modify_password(("7", "5"))
#     print(get_users_one("5"))