class Database:  # база данных
    def __init__(self):
        self.data = {}  # селф дата в виде пустого словаря

    def add_user(self, username, password):  # будет добавлять юзера и  принимать юзернейм и пассворд
        self.data[username] = password  # будет принимать значение по ключу и сохранять в пароль значение пароля


class User:  # Создаем пользователя
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:  # если пароль будет совпадать с пасворд конфирм, только тогда будем выдавать пароль
            if (len(password) >= 8 and password.isalpha() == False and password.isalnum() == True
                    and password.isdigit() == False and password.islower() == False and password.isupper() == False):
                print('Продолжаем регистрацию')
                self.password = password
            else:
                print(
                    'Ваш пароль должен содержать не менее 8 символов, из них = строчные буквы, хотя бы одну '
                    'заглавную букву, и хотя бы одну цифру')

        # print('Попробуйте снова')


# моржовый оператор :=

if __name__ == "__main__":  # входная точка в нашу программу,
    database = Database()  # базу данных выносим за пределы , т.к. нам не надо создават новую базу данных каждый раз

    while True:  # бесконсный цикл, который будет создавать пользователей
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))  # запрашиваем пользовательский ввод
            if password != password2:  # если пароль не совпадает
                print('Пароли не совпадают, попробуйте еще раз')
                # exit()  # то будем завершать программу , заменили на континью
                continue
            database.add_user(user.username, user.password)  # добавляем пользователя в базу данных, т.е. берем обьект
            # (базу данных) и вызовем метод эдд_юзер, куда мы из юзера передадим юзернейм и пароль
        print(database.data)


