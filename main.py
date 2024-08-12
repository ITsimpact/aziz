class Ucburce:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def a(self):
        return self.x * self.y * 4 / 2

x = int(input('Enter 1st number: '))
y = int(input('Enter 2nd number: '))
h = Ucburce(x, y)
print(x, y)
# try:
#     file_text = input("Write your own essay")
#     if file_text:
#         with open('example.txt', 'w') as file:
#             content = file.write(file_text)
#             if (content):
#                 print(f"Your file is created file")
#             else:
#                 print("Smth is gona wrong")
#     else:
#         print('write one more time')
#         file = str(input('write your own essay'))
# except FileNotFoundError:
#     print("sorry man your file is not readable")
# except IOError:
#     print("Error: blalal")
# finally:
#     print('This is finally tags')


#1
# try:
#     a = int(input('Write first number: '))
#     b = int(input('Write second number: '))
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("Chislo ne delitsya na nol")


#2
# try:
#     file = True
#     if file:
#         with open('example.txt', 'r') as open:
#             content = open.read(file)
#             print('your file is', content)
#     else:
#         print('file is empty')
# except FileNotFoundError:
#     print('file not found')
#3
# try:
#     a = int(input("Enter int number:"))
#     b = a / 100
#     print("Your answer is", b)
# except ZeroDivisionError:
#     print("you entered schose 0")
# except ValueError:
#     print("you entered string ")
# 4 
# try:
#     file = "hello"
   
#     with open('example.txt', 'w') as open:
#               content = open.write(file)
#               print("your file is", content)

# except FileNotFoundError:
#     print("file not found")

# 5
# try:
#     a = input("Введите число: ")
#     b = int(a)
# except ValueError:
#     print("Это не целое число!")
# else:
#     print(f"Вы ввели число {b}.")
# finally:
#     print("Программа завершена.")