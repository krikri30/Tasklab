# TODO Найдите количество книг, которое можно разместить на дискете
capacity=int(1.44*1024*1024)
page=int(100)
stroka=int(50)
simbols=int(25)
one_book=int((page*stroka*simbols)*4)
itog=int(capacity/one_book)
print("Количество книг, помещающихся на дискету:", itog)
