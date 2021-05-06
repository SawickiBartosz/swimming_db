from Worker import Worker

class Inserter(Worker):

    def run(self):
        print('\n\nWhere to insert a new row?')
        print('1. Swimmers')
        print('2. Starts')
        print('3. Coaches')
        print('4. Clubs')
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
        else:
            return

    def _insert_swimmers(self):
        cursor = self.cursor
        print('\n Type in information')
        last_name = input('Last name: ')
        first_name = input('First name: ')
        sex = input('Sex (0=Not Known 1=Male 2=Female ): ')
        club_short_name = input('Club short name: ')
        coach_last_name = input('Coach last name: ')
        coach_first_name = input('Coach first name: ')

        # check if coach exists
        coach_id = self.checker.check_coach_exist(coach_first_name, coach_last_name)
        if not coach_id:
            return

        # check if club exists
        if not self.checker.check_club_exist(club_short_name):
            return
        
        # insert a row
        cursor.execute("""
            INSERT INTO Swimmers 
                (LastName, FirstName, Sex, ClubShortName, CoachID)
            VALUES 
                (?, ?, ?, ?, ?)""", 
                last_name, first_name, sex, club_short_name, coach_id[0])
        self.connection.commit()
        print("INSERTED")


    def _insert_starts(self):
        cursor = self.cursor
        print('\n Type in information')
        last_name = input('Swimmer last name: ')
        first_name = input('Swimmer first name: ')
        start_date = input('Date (YYYY-MM-DD): ')
        swim_time = input('Swim time (hh:mm[:ss][.fractional seconds])')
        distance_name = input('Distance name ([distance in m] [style])')

        # check if swimmer exists
        swimmer_id = self.checker.check_coach_exist(first_name, last_name)
        if not swimmer_id:
            return

        # check if distance exists
        if not self.checker.check_distance_exist(distance_name):
           return

        # insert a row
        cursor.execute("""
            INSERT INTO Starts 
                (SwimmerID, StartDate, SwimTime, DistanceName)
            VALUES 
                (?, ?, ?, ?)""", swimmer_id[0], start_date, swim_time, distance_name)
        self.connection.commit()
        print("INSERTED")


    def _insert_coaches(self):
        cursor = self.cursor
        print('\n Type in information')
        last_name = input('Coach last name: ')
        first_name = input('Coach first name: ')
        club_short_name = input('Club short name: ')

        # check if club exists
        if not self.checker.check_club_exist(club_short_name):
            return
    
        # insert a row
        cursor.execute("""
            INSERT INTO Coaches 
                (LastName, FirstName, ClubShortName)
            VALUES 
                (?, ?, ?)""", last_name, first_name, club_short_name)
        self.connection.commit()
        print("INSERTED")

    def _insert_clubs(self):
        cursor = self.cursor
        print('\n Type in information')
        short_name = input('Unique club short name (5 characters): ')
        club_name = input('Club full name: ')
        city_name = input('City: ')

        # check if city exists
        if not self.checker.check_city_exist(city_name):
            return
    
        # insert a row
        cursor.execute("""
            INSERT INTO Cities 
                (ShortName, ClubName, CityName)
            VALUES 
                (?, ?, ?)""", short_name, club_name, city_name)
        self.connection.commit()
        print("INSERTED")
