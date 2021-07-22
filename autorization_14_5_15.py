USERS = ['admin', 'guest', 'director', 'root', 'superstar', 'gena', 'anna']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """).lower()

auth = yesno == "y"

if auth:
    username = input('Введите Ваш username: ').lower()


def is_auth(func):
    def wrapper():
        if auth:
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper


def has_access(func):
    def wrapper():
        if username in USERS:
            print(f'Авторизован как {username}')
            func()
        else:
            print(f'Доступ пользователю {username}, запрещен')
    return wrapper


@is_auth
@has_access
def from_db():
    print(f'\n Статус {username}: \n   - черт')


from_db()
