from src.data_store import initial_object, data_store
import jwt
import re
from unicodedata import name
from xxlimited import new
from json import dump, load
from os import path

from src.error import AccessError, InputError

def check_global_owner(auth_user_id):
    '''
    verifies if the authorised user is a global owner.
    '''
    store = data_store.get()
    for user in store['users']:
        if user['auth_user_id'] == auth_user_id:
            if user['perm_id'] == 1:
                return True
    return False

def owner_or_global_owner(channel, auth_user_id):
    '''
    checks if global owner or channel owner
    '''
    # if channel owner
    for member in channel['owner_members']:
        if member['u_id'] == auth_user_id:
            return True
    # else if seams owner
    store = data_store.get()
    for user in store['users']:
        if user['auth_user_id'] == auth_user_id:
            if user['perm_id'] == 1:
                return True
    # else
    raise AccessError('Error: User does not have global owner or channel owner permissions in this channel')

def member_or_global_owner(channel, auth_user_id):
    '''
    checks if global owner or channel owner
    '''
    # if channel owner
    for member in channel['all_members']:
        if member['u_id'] == auth_user_id:
            return True
    # else if seams owner
    store = data_store.get()
    for user in store['users']:
        if user['auth_user_id'] == auth_user_id:
            if user['perm_id'] == 1:
                return True
    # else
    raise AccessError('Error: User does not have global owner or channel owner permissions in this channel')