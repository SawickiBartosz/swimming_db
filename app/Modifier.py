
class Modifier():
    def __init__(self, connection, cursor, checker):
        self.connection = connection
        self.cursor = cursor
        self.checker = checker

    def run(self):
        print('\n\nWhat do you want to modify?')
        print("1. Change swimmer's club")
        print("2. Change swimmer's coach")
        print("3. Change coach's club")
        # TODO modyfikowanie wybranego zawodnika
        print('Anything else to exit')
        choice = input()
        if choice == '1':
            self._mod_swimmers_club()
        elif choice == '2':
            self._mod_swimmers_coach()
        elif choice == '3':
            self._mod_coach_club()
        else:
            return

    
    def _mod_swimmers_club(self):
        print("Which swimmer you want to modify?")
        swimmer_last_name = input("Last name: ")
        swimmer_first_name = input("First name: ")
        new_club = input("New club short name (5 characters): ")

        # check if club exists
        if not self.checker.check_club_exist(club_short_name):
            return

        self.cursor.execute("""
        UPDATE Swimmers 
            SET ClubShortName = ?
            WHERE LastName=? AND FirstName=?;
        """, new_club, swimmer_last_name, swimmer_first_name)
        self.connection.commit()
        print('Modified ' + str(self.cursor.rowcount) + ' row(s)')


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

        self.cursor.execute("""
        UPDATE Swimmers 
            SET CoachID = ?
            WHERE LastName=? AND FirstName=?;
        """, coach_id, swimmer_last_name, swimmer_first_name)
        self.connection.commit()
        print('Modified ' + str(self.cursor.rowcount) + ' row(s)')

    def _mod_coach_club(self):
        print("Which coach you want to modify?")
        coach_last = input("Coach last name: ")
        coach_first = input("Coach first name:  ")
        new_club = input("New club short name (5 characters): ")

        # check if new club exists
        if not self.checker.check_club_exist(new_club):
            return
       
        self.cursor.execute("""
        UPDATE Coaches 
            SET ClubShortName = ?
            WHERE LastName=? AND FirstName=?;
        """, new_club, coach_last, coach_first)
        self.connection.commit()
        print('Modified ' + str(self.cursor.rowcount) + ' row(s)')
