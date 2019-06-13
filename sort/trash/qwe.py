#окнец строки end
# for i in range(10):
#     print("qwe", end = ' хуй ')

#проверка на строку
# def qwe(srt):
#     try:
#         a = int(srt)
#         return True
#     except:
#         return False


# a = '-123.0'
# print(qwe(a))

#вывод элемнтов массива
listina = [[i*10 for i in range(10)] for _ in range(10)]
mas = [str(i) for i in range(10)]
# for mass in listina:
# :
# print(' '.join(str([str(elem)for elem in mass])for mass in listina))
# print(''.join([[i for i in range(10)] for _ in range(10)]))
# print(listina)

# print(''.join([''.join([str(_) for _ in __] for __ in listina])))

# print(''.join(mas))


# print(' '.join([str(elem) for elem in row]))


print('\r\n'.join(['\t'.join([str(elem) for elem in _]) for _ in listina]))
# print([''.join([str(elem) for elem in _]) for _ in listina])


qwe = ['123456789','1234567890','1234567890']
# print(''.join(qwe))