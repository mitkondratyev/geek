def info(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone, sep=', ')

def info2(**kwargs):
    print(', '.join(list(kwargs.values())))

info(name='Dima', surname="K", year="1990", city="K", email="test@gmail.com", phone="+799999999")
info2(name='Dima', surname="K", year="1990", city="K", email="test@gmail.com", phone="+799999999")