import random
import string
from FlaskWebProject4.DAO.GetRandomId import getRandomId

def generate_id():
    letters = string.ascii_lowercase + "0123456789"
    return ''.join(random.choice(letters) for i in range(4))

def check_collison(str,id):
    l = getRandomId(str,id)
    if len(l) == 0:
        print("length", str , id, l)
        return False
    else:
       return True

def get_user_id():
    id = generate_id()
    while check_collison("user",id):
        id = generate_id()
    return id

def get_candidate_id():
    id = generate_id()
    while check_collison("candidate",id):
        id = generate_id()
        print(id)
    return id

def get_task_id():
    id = generate_id()
    while check_collison("task",id):
        id = generate_id()
    return id
