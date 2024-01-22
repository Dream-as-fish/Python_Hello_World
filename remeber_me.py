from pathlib import Path
import json


# username = input("What is your username? ")
#
# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)
#
# print(f"We'll remember your username: {username}")

# def greet_user():
#     """问候用户，并指出其姓名"""
#     path = Path('username.json')
#     if path.exists():
#         content = path.read_text()
#         username = json.loads(content)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name?")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you back,{username}")
#
#
# greet_user()


def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = input("What is your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you back, {username}!")


greet_user()
