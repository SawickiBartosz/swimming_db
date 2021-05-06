import os

import pyodbc

from Checker import Checker
from Deleter import Deleter
from Inserter import Inserter
from Modifier import Modifier
from Printer import Printer
from Reporter import Reporter
from settings import password, username


def connect(username, password):
        server = 'localhost' 
        database = 'SwimmingDB'  
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+
            server+';DATABASE='+database+';UID='+username+
            ';PWD='+ password)
        cursor = cnxn.cursor()
        print('Hello ' + username + '! Welcome to SwimBase!')
        return cnxn, cursor

def menu():
    print('\n\nChoose a number:')
    print('1. Insert new data')
    print('2. Delete records')
    print('3. Modify record')
    print('4. Print reports')
    print('5. Print tables')
    print('6. Exit')
    choice = input()
    return choice

def exit():
    cls()
    print('See You!')


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def main(*args, **kwargs):
    cls()
    cnxn, cursor = connect(username, password)
    checker = Checker(cursor)
    inserter = Inserter(cnxn, cursor, checker)
    deleter = Deleter(cnxn, cursor, checker)
    modifier = Modifier(cnxn, cursor, checker)
    reporter = Reporter(cnxn, cursor, checker)
    printer = Printer(cnxn, cursor, checker)

    while True:
        choice = menu()
        if choice == '6':
            break
        elif choice == '1':
            inserter.run()
        elif choice == '2':
            deleter.run()
        elif choice == '3':
            modifier.run()
        elif choice == '4':
            reporter.run()
        elif choice == '5':
            printer.run()
        else:
            cls()
            print('Wrong input! Try again!')
    exit()


if __name__ == '__main__':
    main()
