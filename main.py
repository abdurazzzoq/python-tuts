# cars = ('bmw', 'atang', 'mini', 'chevrolet', 'dodge')

# cars_2 = []
# # print(cars)
# for i in cars:
#     cars_2.insert(0, i)
# print(cars_2)

# friends = []

# for friend in range(5): #since we do not provide a list above we use range() method
#     friends.append(input(f'enter your {friend+1} name: '))
# print(friends)


# names = ['Maryam', 'Sevda', 'Abdurrozzaq', 'Dilshod', 'Xushnud', 'Naima']
# for name in names:
#     if name.__contains__('Maryam'):
#         print(name.upper())
#     else:
#         print(name.title())
# # for i in names:
#     print('Hello', i)

# print(f'the code repeated {len(names)} times')

# num = list(range(10, 101))
# for i in num:
#     print(i**3)

# users_num = input('how many you talked to today?>>>')
# users = []
# for i in range(int(users_num)):
#     users.append(input(f'to day you talked with {i+1}'))
# print(users)


# login = input('Please enter your login:  ')
# if len(login) <= 5:
#     print('Login must be more than five characters')
# else:
#     print('Hello World!')


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for i in cars:
#     if i != 'gm':
#         print(i.title())
#     else:
#         print(i.upper())


# is_admin = input('please, enter your name:  ')

# if is_admin.lower().__contains__('admin'):
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {is_admin}!")


# num = int(input('please enter the number:  '))

# # if num > 0:
#     print(int(num**(0.5)))  # this is finding the root of the entered number
# else:
#     print('please enter positive number')


# num1 = input('enter the first number: ')
# num2 = input('enter the second number: ')
# if num1 > num2:
#     print(f'{num1} is bigger than {num2}')
# elif num1 < num2:
#     print(f'{num1} is less than {num2}')
# else:
#     print('they are equal')


# mahsulotlar = ['apple', 'pineapple', 'melon', 'watermelon', 'peachh']
# savat = []


# for i in range(5):
#     savat.append(input(f'the {i+1} element: '))
# bor_mahsulotlar = []
# mavjud_emas = []

# for product in savat:
#     if product in mahsulotlar:
#         bor_mahsulotlar.append(product)
#     else:
#         mavjud_emas.append(product)

# if mavjud_emas:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q:")
#     for i in mavjud_emas:
#         print(i)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# print(f'bor mahsulotlar {bor_mahsulotlar}')
# print(f'yoq mahsulotlar {mavjud_emas}')


# users = ['Maryam', 'Abdulvahhab', 'Abdurrozzaq', 'Muhammad', 'Naima']
# is_user = input('plese enter the login:  ')
# if is_user in users:
#     print('this username is already exist')
# else:
#     print(f'welcome {is_user}')


# products = ['apple', 'towel', 'brush', 't-shirt', 'shirt', 'dates', ]
# products.sort()
# print(products)
# cart = []

# available = []
# missing = []


# for item in range(5):
#     cart.append(input(f'please enter the {item+1} product: '))

# for i in cart:
#     if i in products:
#         available.append(i)
#     else:
#         missing.append(i)

# if missing:
#     not_available = print('these products are not available: ')
#     for i in missing:
#         print(i)
# else:
#     print('all products are in our store')

# terms = {
#     'int': 'whole number',
#     'str': 'string',
#     'float': 'decimal number',
#     'if': 'if condition',
#     'elif': 'else and if'
# }
# print(sorted(terms))

# countries = {
#     'Uzbekistan': 'Tashkent',
#     'USA': 'Washington',
#     'UK': 'London',
#     'UAE': 'Abu-Dabi',
#     'Saudi-Arabia': 'Ar-riyad'
# }
# quest = input('enter the country:  ')

# if quest in countries:
#     print(countries[quest])
# else:
#     print('we could not defined the country')


# menu = {
#     'plow': 10,
#     'kebab': 20,
#     'lagman': 15,
#     'sushi': 25,
#     'pizza': 12,
#     'burger': 15,
#     'mandi': 30,
#     'fendi': 32
# }

# orders = []
# for i in range(3):
#     orders.append(input(f'please order {i+1} meal:  '))
# for order in orders:
#     if order in menu:
#         print(menu[order])
#     else:
#         print('we do not have this')

# person = {
#     'Abdulvahhab': ['john wick', 'hitman'],
#     'Maryam': ['shaytanat', 'deadpool'],
#     'Naima': ['spiderman', 'batman'],
#     'Muhammad': ['naruto', 'tokyo revengers']
# }
# for key, value in person.items():
#     print(f"{key}'s favourite movie is:")
#     for movie in value:
#         print(movie)


# countries = {
#     'Uzbekistan': {
#         'capital': 'Tashkent',
#         'location': 'central asia'
#     },
#     'UAE': {
#         'capital': 'Abu-Dabi',
#         'location': 'asia',
#     },
#     'Poland': {
#         'capital': 'Warsaw',
#         'location': 'Europe'
#     }
# }

# quest = input('please enter the country:  ')
# result = countries.get(quest)
# if quest in countries:
#     print(result)
# else:
#     print('Hello World!')

# print('please, enter your age:  ')
# quest = 'if you want to quit the application please enter "exit" or "quit" or "clear":  '

# while True:
#     result = input(quest)
#     if result == 'exit' or result == 'quit' or result == 'clear':
#         break
#     age = int(result)
#     if age < 7:
#         price = 2000
#     elif 7 <= age < 18:
#         price = 3000
#     elif 18 <= age < 65:
#         price = 10000
#     else:
#         print('free')
#     print(price)
# print('the app is over')

products = ['kebab', 'welnut', 'orbit']

# quest = 'please select your product:  '
# order = ''


# def prod():
#     while True:
#         order = input(quest)
#         if order == 'clear' or order == 'cls' or order == 'no':
#             break
#         else:
#             products.append(order)
#     return products


# print(prod())



# print(products)
