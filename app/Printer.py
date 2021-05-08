from Worker import Worker


class Printer(Worker):
    # def run(self):
    #     print('Select table to print')
    #     print("1. Swimmers")
    #     print("2. Starts")
    #     print("3. Coaches")
    #     print("4. Clubs")
    #     print("5. Cities")
    #     print("6. Distances")
    #     print('Anything else to exit')

    #     choice = input()
    #     if choice == '1':
    #         self._print_table('Swimmers')
    #     elif choice == '2':
    #         self._print_table('Starts')
    #     elif choice == '3':
    #         self._print_table('Coaches')
    #     elif choice == '4':
    #         self._print_table('Clubs')
    #     elif choice == '5':
    #         self._print_table('Cities')
    #     elif choice == '6':
    #         self._print_table('Distances')
    #     else:
    #         return

    def _print_menu(self):
        print('Select table to print')
        print("1. Swimmers")
        print("2. Starts")
        print("3. Coaches")
        print("4. Clubs")
        print("5. Cities")
        print("6. Distances")
        print('Anything else to exit')

        choice = input()
        return choice

    def _utilize_choice(self, choice):
        if choice == '1':
            self._print_table('Swimmers')
        elif choice == '2':
            self._print_table('Starts')
        elif choice == '3':
            self._print_table('Coaches')
        elif choice == '4':
            self._print_table('Clubs')
        elif choice == '5':
            self._print_table('Cities')
        elif choice == '6':
            self._print_table('Distances')
        else:
            return

    def _print_table(self, table_name):
        self.cursor.execute("SELECT * from " + table_name) 
        # SQL injection safe, only coded values are substituted
        self._pretty_print()