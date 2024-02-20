#!/usr/bin/env python3


# """
# Main file
# """
# from user import User

# print(User.__tablename__)

# for column in User.__table__.columns:
#     print("{}: {}".format(column, column.type))

# =================== task 1 ====================

# """
# Main file
# """

# from db import DB
# from user import User

# my_db = DB()

# user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
# print(user_1.id)

# user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
# print(user_2.id)


# =================== task 2 ====================

# """
# Main file
# """
# from db import DB
# from user import User

# from sqlalchemy.exc import InvalidRequestError
# from sqlalchemy.orm.exc import NoResultFound


# my_db = DB()

# user = my_db.add_user("test@test.com", "PwdHashed")
# print(user.id)

# find_user = my_db.find_user_by(email="test@test.com")
# print(find_user.id)

# try:
#     find_user = my_db.find_user_by(email="test2@test.com")
#     print(find_user.id)
# except NoResultFound:
#     print("Not found")

# try:
#     find_user = my_db.find_user_by(no_email="test@test.com")
#     print(find_user.id)
# except InvalidRequestError:
#     print("Invalid")        


# =================== task 3 ====================

# """
# Main file
# """
# from db import DB
# from user import User

# from sqlalchemy.exc import InvalidRequestError
# from sqlalchemy.orm.exc import NoResultFound


# my_db = DB()

# email = 'test@test.com'
# hashed_password = "hashedPwd"

# user = my_db.add_user(email, hashed_password)
# print(user.id)

# try:
#     my_db.update_user(user.id, hashed_password='NewPwd')
#     print("Password updated")
# except ValueError:
#     print("Error")


# =================== task 4 ====================
# ================ _hash_password  =======================

# """
# Main file
# """
# from auth import _hash_password

# print(_hash_password("Hello Holberton"))


# =================== task 5 ====================
# ================ register_user  =======================

"""
Main file
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err)) 
