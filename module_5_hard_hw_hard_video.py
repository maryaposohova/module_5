# class User:
#     def __init__(self, nickname, password, age: int):  # создаем условия пользователю
#         self.nickname = nickname
#         self.password_hash = self.hash_password(password)
#         self.password = password
#         if age >= 18:
#             self.age = age
#         else:
#             print('Вам еще нет 18 лет')
#         print()
#
#     def hash_password(self, password):
#         return password
#
#     def __hash__(self):     #
#         return self.password
#
#     def __str__(self):
#         return
#
# class Video:
#     def __init__(self, title, duration, time_now, adult_mode):
#         self.title = title   #  заголовок, строка
#         self.duration = duration   #  продолжительность, секунды
#         self.time_now = time_now    #  секунда остановки (изначально 0)
#         self.adult_mode = adult_mode    # ограничение по возрасту, bool (False по умолчанию)
#         print('Вам нет 18 лет, пожалуйста покиньте страницу')
#
#
#
#
#
#
# class UrTube:
#     pass
#
#
# u1 = User('M', 11, 18)
# print(u1.nickname)
# print(u1.password_hash, id(u1.password_hash))
# print(u1.password, id(u1.password))
# print(u1.age)
# u2 = Video('Video', 1000, 0, 17)
# print(u2.title)
# print(u2.duration)
# print(u2.time_now)
# print(u2.adult_mode)


