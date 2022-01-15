# #
# # print("test" or 0)
# # print([] and "test")
# # nice = 0
# # personality = ("wredny", "miły")[nice]
# # print("Kot jest", personality)  # Wyjście: Kot jest miły
# # string = 'Python'
# # for litera in string:
# #    print('litera:', litera)
# # litera = string[0]
# # print('litera:', litera)
# # litera = string[1]
# # print('litera:', litera)
# # litera = string[2]
# # print('litera:', litera)
# # litera = string[3]
# # print('litera:', litera)
# # litera = string[4]
# # print('litera:', litera)
# # litera = string[5]
# # print('litera:', litera)
# # warzywa = ['marchew', 'kalafior', 'kapusta']
# # i = 1
# # for warzywo in warzywa:
# #     print('warzywo:', i,warzywo)
# #     i +=1
# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "Aneta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
# lista.sort()
# i=()
# for t in lista:
#     if t[-1]=="a":
#         i=i+1
# print(i)
# liczby = list()
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby) # [2, 4, 6, 8, 10]

# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)
# x = int(input("podaj pierwszą liczbę:"))
# y = int(input("Padaj drugą liczbę"))
#
# if x > y:
#     print("x jest większe od y")
#     n = y
# else:
#     print("x jest mniejsze od y")
#     n = x
# print(n)
#
# for z in range(n, 0, -1):
#     if x % z == 0 and y % z ==0:
#         print(x, "i", y, "dzieli się przez" ,z)
#         break
name = input("Proszę wpisać swoje imię.")
# Wpisz swoją odpowiedź tutaj.

if len(name) > 0:
    print(name)
else:
    pass