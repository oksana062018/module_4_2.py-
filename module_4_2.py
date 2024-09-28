def test_function():
    def inner_function():
        print()
    d = ("Я в области видимости функции test_function")
    print(d)

a = ("Я в области видимости функции test_function")
print(a)
