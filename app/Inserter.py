from Worker import Worker

class Inserter(Worker):

    def run(self):
        print('\n\nWhere to insert a new row?')
        print('1. Swimmers')
        print('2. Starts')
        print('3. Coaches')
        print('4. Clubs')
        print('5. Cities')

        print('Anything else to exit')
        choice = input()
        if choice == '1':
            self._insert_swimmers()
        elif choice == '2':
            self._insert_starts()
        elif choice == '3':
            self._insert_coaches()
        elif choice == '4':
            self._insert_clubs()
        elif choice == '5':
            self._insert_cities()
        else:
            return

    def _print_menu(self):
        print('\n\nWhere to insert a new row?')
        print('1. Swimmers')
        print('2. Starts')
        print('3. Coaches')
        print('4. Clubs')
        print('5. Cities')
        print('Anything else to exit')
        choice = input()
        return choice

    def _utilize_choice(self, choice):
        if choice == '1':
            self._insert_swimmers()
        elif choice == '2':
            self._insert_starts()
        elif choice == '3':
            self._insert_coaches()
        elif choice == '4':
            self._insert_clubs()
        elif choice == '5':
            self._insert_cities()
        else:
            return
        

    def _insert_swimmers(self):
        cursor = self.cursor
        print('\nType in information')
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
            # insert a row
            cursor.execute("""
                INSERT INTO Swimmers 
                    (LastName, FirstName, Sex, ClubShortName, CoachID)
                VALUES 
                    (?, ?, ?, ?, ?)""", 
                    last_name, first_name, sex, club_short_name, coach_id[0])
            self.connection.commit()
            print("INSERTED")
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')



    def _insert_starts(self):
        cursor = self.cursor
        print('\nType in information')
        last_name = input('Swimmer last name: ')
        first_name = input('Swimmer first name: ')

        # check if swimmer exists
        swimmer_id = self.checker.check_swimmer_exist(first_name, last_name)
        if not swimmer_id:
            return

        distance_name = input('Distance name ([distance in m] [style])')

        # check if distance exists
        if not self.checker.check_distance_exist(distance_name):
           return

        start_date = input('Start date (YYYY-MM-DD): ')
        swim_time = input('Swim time (hh:mm[:ss][.fractional seconds])')
        
        try:
            # insert a row
            cursor.execute("""
                INSERT INTO Starts 
                    (SwimmerID, StartDate, SwimTime, DistanceName)
                VALUES 
                    (?, ?, ?, ?)""", swimmer_id[0], start_date, swim_time, distance_name)
            self.connection.commit()
            print("INSERTED")
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')

    def _insert_coaches(self):
        cursor = self.cursor
        print('\nType in information')
        last_name = input('Coach last name: ')
        first_name = input('Coach first name: ')
        club_short_name = input('Club short name: ')

        # check if club exists
        if not self.checker.check_club_exist(club_short_name):
            return
        try:
            # insert a row
            cursor.execute("""
                INSERT INTO Coaches 
                    (LastName, FirstName, ClubShortName)
                VALUES 
                    (?, ?, ?)""", last_name, first_name, club_short_name)
            self.connection.commit()
            print("INSERTED")
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')



    def _insert_clubs(self):
        cursor = self.cursor
        print('\nType in information')
        short_name = input('Unique club short name (5 characters): ')
        club_name = input('Club full name: ')
        city_name = input('City: ')

        # check if city exists
        if not self.checker.check_city_exist(city_name):
            return
        try:
            # insert a row
            cursor.execute("""
                INSERT INTO Clubs 
                    (ShortName, ClubName, CityName)
                VALUES 
                    (?, ?, ?)""", short_name, club_name, city_name)
            self.connection.commit()
            print("INSERTED")
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')



    def _insert_cities(self):
        cursor = self.cursor
        print('\nType in information')
        city_name = input('City: ')

        try:
            # insert a row
            cursor.execute("""
                INSERT INTO Cities 
                    (CityName)
                VALUES 
                    (?)""", city_name)
            self.connection.commit()
            print("INSERTED")
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')
