from users import users_dao
from business import business_dao
from riders import riders_dao

def login():
    dic_user, dic_bisiness, dic_rider = {}, {}, {}
    list_user = users_dao.get_users_all()
    list_bisiness = business_dao.get_business_all()
    list_rider = riders_dao.get_riders_all()
    num_user = len(list_user)
    num_business = len(list_bisiness)
    num_rider = len(list_rider)

    for i in range(num_user):
        key = list_user[i].get("users_account")
        value = list_user[i].get("users_password")
        dic_user.setdefault(key, value)

    for i in range(num_business):
        key = list_bisiness[i].get("business_account")
        value = list_bisiness[i].get("business_password")
        dic_bisiness.setdefault(key, value)

    for i in range(num_rider):
        key = list_rider[i].get("riders_account")
        value = list_rider[i].get("riders_account")
        dic_rider.setdefault(key, value)

    return dic_user, dic_bisiness, dic_rider

def register(params=()):
    if len(params) == 8:
        users_dao.insert_users(params)
    elif len(params) == 6:
        business_dao.insert_business(params)
    else:
        riders_dao.insert_riders(params)

