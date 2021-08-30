import pymysql


# 定义数据库连接类
class MysqlHelper(object):
    # 定义空连接
    conn = None

    # 初始化变量及类
    def __init__(self, host, username, password, db, auth_plugin_map, charset='utf8', port=3306):
        self.host = host  # 数据库地址
        self.username = username  # 数据库用户名
        self.password = password  # 数据库密码
        self.db = db  # 数据库名称
        self.auth_plugin_map = auth_plugin_map
        self.charset = charset  # 数据库字符集
        self.port = port  # 数据库端口

    # 连接数据库
    def connect(self):
        # 初始化数据库连接
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                    db=self.db, charset=self.charset, auth_plugin_map=self.auth_plugin_map)
        # 初始化数据库游标 注意:这里返回的是字典对象,json
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    # 释放数据库
    def close(self):
        # 释放数据游标
        self.cursor.close()
        # 关闭数据库
        self.conn.close()

    #获取数据库返回集中第一条记录
    def get_one(self, sql, params=()):
        #定义空数据集
        result = None
        try:
            if "SELECT" in str(sql).upper():        #检测是否为查询语句
                self.connect()                      #连接数据库
                self.cursor.execute(sql, params)    #执行查询命令
                result = self.cursor.fetchone()     #返回第一条记录
                self.close()                        #释放数据库
        except Exception as e:
            print(e)
        return result



    # 返回全部数据集合
    # def get_all(self, sql, params=()):
    def get_all(self, sql, params=()):
        # 定义数据列表集合
        list_data = ()
        try:
            if "SELECT" in str(sql).upper():  # 检测是否为查询语句
                self.connect()  # 连接数据库
                self.cursor.execute(sql, params)  # 执行查询命令
                list_data = self.cursor.fetchall()  # 返回全部记录
                self.close()  # 释放数据库
        except Exception as e:
            print(e)
        return list_data

    # 执行插入语句
    def insert(self, sql, params=()):
        if "INSERT" in str(sql).upper():  # 检测是否为插入语句
            return self.__edit(sql, params)
        else:
            return None

    # 执行数据库更新
    def update(self, sql, params=()):
        if "UPDATE" in str(sql).upper():  # 检测是否为更新语句
            return self.__edit(sql, params)
        else:
            return None

    # 执行数据删除
    def delete(self, sql, params=()):
        if "DELETE" in str(sql).upper():  # 检测是否为删除语句
            return self.__edit(sql, params)
        else:
            return None

    # 执行其他特殊命令 慎用
    def cmdsql(self, sql, params=()):
        return self.__edit(sql, params)

    # 执行命令函数
    def __edit(self, sql, params):
        # 定义影响行数
        count = 0
        try:
            self.connect()  # 连接数据库
            count = self.cursor.execute(sql, params)  # 执行数据库命令语句
            self.conn.commit()  # 把命令推送到服务器
            self.close()  # 释放数据库
        except Exception as e:
            print(e)
        return count  # 返回受影响的行数


if __name__ == '__main__':
    mysql = MysqlHelper("10.67.0.61", "root", "password", "orderingsys", "mysql_native_password")
    print(mysql.get_all("select * from users"))






