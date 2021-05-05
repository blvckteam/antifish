import requests
import urllib.request, urllib.parse, urllib.error
import os
from colorama import Fore, Back, Style
import time

def cls():
    os.system('clear')
def banner():
    print(f"{Fore.RED}    |     '|.   '|' |''||''| '||'{Fore.WHITE} '||''''| '||'  .|'''.|  '||'  '||' ")
    print(f"{Fore.RED}   |||     |'|   |     ||     || {Fore.WHITE}  ||  .    ||   ||..  '   ||    ||  ")
    print(f"{Fore.RED}  |  ||    | '|. |     ||     || {Fore.WHITE}  ||''|    ||    ''|||.   ||''''||  ")
    print(f"{Fore.RED} .''''|.   |   |||     ||     || {Fore.WHITE}  ||       ||  .     '||  ||    ||  ")
    print(f"{Fore.RED}.|.  .||. .|.   '|    .||.   .||.{Fore.WHITE} .||.     .||. |'....|'  .||.  .||. ")
    print(f"{Fore.RED}                                 {Fore.WHITE}             Telegram: {Fore.RED}@blackhat_lab{Fore.WHITE}")
    print('\n')
cls()
banner()

file = open('files.txt', 'r')
print(f'Введите {Fore.RED}ссылку{Fore.WHITE}: ', end='')
a = input('')
if a[:-1] != '/':
    a = (a + '/')
else:
    pass

ok = '0'
for line in file:
    print(line[:-1])
    try:

        urllib.request.urlretrieve(a + line[:-1] + '.log', 'core/' + 'cracked.txt')
        ok = '1'
    except:
        print(Fore.RED + 'Лог ' + str(line) + ' не найден')

    try:
        urllib.request.urlretrieve(a + line[:-1]+ '.lst', 'core/' + 'cracked.txt')
        ok = '1'
    except:
        print(Fore.RED + 'Лист ' + str(line) + ' не найден')
    try:
        urllib.request.urlretrieve(a + line[:-1] + '.db', 'core/' + 'cracked.db')
        ok = '2'
    except:
        print(Fore.RED + 'База данных ' + str(line) + ' не найдена')
        if int(ok) >= 1:
            print(Fore.GREEN + 'Успешно взломали фишинг!!! Файл: ' + line)
            print('')
            print(Fore.MAGENTA + 'Выводим содержание файла...' + Fore.WHITE + '\n\n')
            os.system('cat core/cracked.txt')
            print(Fore.MAGENTA + 'В течении 5 сек можете рассмотреть результат выше и мы продолжим искать')
            time.sleep(5)
            ok = 0
            if ok == '1':

                print(Fore.CYAN + 'Сохранено в core/cracked.txt')
            elif ok == '2':
                print(Fore.CYAN + 'Сохранено в core/cracked.db')
            print('\n')
            print(Fore.BLUE + 'Продолжаем искать... \n')
            time.sleep(2)
            a = '1'
if a == '1':
    cls()
    banner()

    print(Fore.GREEN + 'Выводим содержание файла: \n\n' + Fore.WHITE)
    print(Fore.YELLOW + '----------------------------------------------------------------\n\n')
    print(Fore.WHITE + '')
    os.system('cat core/cracked.txt')
    print(Fore.YELLOW + '\n\n----------------------------------------------------------------')
    q = input(Fore.GREEN + '\nУкраденная информация ^^^')
 
elif a == '2':
    cls()
    banner()
    print(Fore.GREEN + 'База данных сохранена в "core/cracked.db"')
else:
    print(Fore.BLUE + 'Ничего не найдено' + Fore.WHITE)
