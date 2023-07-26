import requests

with open('accesss.txt','r') as file:
        access_token = file.read().strip()
with open('refresh.txt','r') as file:
        refresh_token = file.read().strip()

def get_refresh_token():
        global access_token, refresh_token
        username = input("What is your username ?")
        password = input("what is your password ?")
        auth_resp = requests.post("http://127.0.0.1:8000/api/token/", json={"username":username, "password":password})
        if auth_resp.status_code == 200:
                access_token = auth_resp.json()['access']
                with open('accesss.txt', 'w') as file:
                        file.write(access_token)
                refresh_token = auth_resp.json()['refresh']
                with open('refresh.txt', 'w') as file:
                        file.write(refresh_token)
                return True
        else:
                return False


def get_access_token():
        global access_token, refresh_token
        resp = requests.post("http://127.0.0.1:8000/api/token/refresh/", json={"refresh": f"{refresh_token}"})
        if resp.status_code == 200:
                access_token = resp.json()['access']
                with open('accesss.txt', 'w') as file:
                        file.write(access_token)
                return True
        else:
                return False

def create_book():
        global access_token
        headers = { "Authorization": f"Bearer {access_token}" }
        resp = requests.post("http://127.0.0.1:8000/api/books/", headers=headers,
                             json={"title": "The Alchemist", "author": "Paulo Coelho"})
        if resp.status_code == 201:
                print(resp.json())
                return True
        else:
                return False


if not create_book() :
        print('access_token failed')
        if not (get_access_token() and create_book()):
                print('refresh token failed')
                if not (get_refresh_token() and create_book()):
                        print('login failed')





