# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:28:54 2019

@author: KALI CORP
"""
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #compares strings
        return user
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

