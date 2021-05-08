from Worker import Worker


class Modifier(Worker):
    
    # def run(self):
    #     print('\n\nWhat do you want to modify?')
    #     print("1. Change swimmer's club")
    #     print("2. Change swimmer's coach")
    #     print("3. Change coach's club")
    #     print("4. Modify all of swimmer's data")
    #     print('Anything else to exit')
    #     choice = input()
    #     if choice == '1':
    #         self._mod_swimmers_club()
    #     elif choice == '2':
    #         self._mod_swimmers_coach()
    #     elif choice == '3':
    #         self._mod_coach_club()
    #     elif choice == '4':
    #         self._mod_all_swimmer()
    #     else:
    #         return


    def _print_menu(self):
        print('\n\nWhat do you want to modify?')
        print("1. Change swimmer's club")
        print("2. Change swimmer's coach")
        print("3. Change coach's club")
        print("4. Modify all of swimmer's data")
        print('Anything else to exit')
        choice = input()
        return choice

    def _utilize_choice(self, choice):
        if choice == '1':
            self._mod_swimmers_club()
        elif choice == '2':
            self._mod_swimmers_coach()
        elif choice == '3':
            self._mod_coach_club()
        elif choice == '4':
            self._mod_all_swimmer()
        else:
            return
    
    def _mod_swimmers_club(self):
        print("Which swimmer you want to modify?")
        swimmer_last_name = input("Last name: ")
        swimmer_first_name = input("First name: ")
        new_club = input("New club short name (5 characters): ")

        # check if club exists
        if not self.checker.check_club_exist(new_club):
            return
        try:
            self.cursor.execute("""
            UPDATE Swimmers 
                SET ClubShortName = ?
                WHERE LastName=? AND FirstName=?;
            """, new_club, swimmer_last_name, swimmer_first_name)
            self.connection.commit()
            print('Modified ' + str(self.cursor.rowcount) + ' row(s)')
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')



    def _mod_swimmers_coach(self):
        print("Which swimmer you want to modify?")
        swimmer_last_name = input("Last name: ")
        swimmer_first_name = input("First name: ")
        new_coach_last = input("New coach last name: ")
        new_coach_first = input("New coach first name:  ")

        # check if coach exists
        coach_id = self.checker.check_coach_exist(coach_first_name, coach_last_name)
        if not coach_id:
            return
        try:
            self.cursor.execute("""
            UPDATE Swimmers 
                SET CoachID = ?
                WHERE LastName=? AND FirstName=?;
            """, coach_id, swimmer_last_name, swimmer_first_name)
            self.connection.commit()
            print('Modified ' + str(self.cursor.rowcount) + ' row(s)')
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')


    def _mod_coach_club(self):
        print("Which coach you want to modify?")
        coach_last = input("Coach last name: ")
        coach_first = input("Coach first name:  ")
        new_club = input("New club short name (5 characters): ")

        # check if new club exists
        if not self.checker.check_club_exist(new_club):
            return
       
        try:
            self.cursor.execute("""
            UPDATE Coaches 
                SET ClubShortName = ?
                WHERE LastName=? AND FirstName=?;
            """, new_club, coach_last, coach_first)
            self.connection.commit()
            print('Modified ' + str(self.cursor.rowcount) + ' row(s)')
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')


    def _mod_all_swimmer(self):
        self.cursor.execute("""
        --sql
        SELECT s.*, c.LastName AS CoachLastName, c.FirstName AS CoachFirstName
        FROM Swimmers s JOIN Coaches c on c.CoachID = s.CoachID;""")
        print('')
        self._pretty_print()
        swimmer_id = input('Type id of a swimmer to modify: ')
        print('Type in updated information')

        last_name = input('Last name: ')
        first_name = input('First name: ')
        sex = input('Sex (0=Not Known 1=Male 2=Female ): ')
        club_short_name = input('Club short name: ')

        # check if club exists
        if not self.checker.check_club_exist(club_short_name):
            return

        coach_last_name = input('Coach last name: ')
        coach_first_name = input('Coach first name: ')

        # check if coach exists
        coach_id = self.checker.check_coach_exist(coach_first_name, coach_last_name)
        if not coach_id:
            return

        try:
            self.cursor.execute("""
                UPDATE Swimmers 
                    SET LastName=?, FirstName=?, Sex=?, ClubShortName=?, CoachID=?
                WHERE SwimmerID = ?;""", 
                    last_name, first_name, sex, club_short_name, coach_id[0], swimmer_id)
            self.connection.commit()
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')
