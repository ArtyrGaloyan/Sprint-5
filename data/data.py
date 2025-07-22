import random


class PersonData:
    user_name = 'Артур Галоян'
    login = 'Артур_Галоян_23_777@gmail.com'
    password = '530087185051377'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"
