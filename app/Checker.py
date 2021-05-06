class Checker():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def check_club_exist(self, new_club):
        self.cursor.execute('SELECT * FROM Clubs WHERE ShortName=?', new_club)
        club = self.cursor.fetchone()
        if club is None:
            print('Such a club does not exist in database, insert it first!\n\n')
            return False
        return True


    def check_coach_exist(self, fname, lname):
        self.cursor.execute(
            'SELECT CoachID FROM Coaches WHERE LastName=? AND FirstName=?',
            lname, fname)
        coach_id = self.cursor.fetchone()
        if coach_id is None:
            print('Such a coach does not exist in database, insert them first!\n\n')
            return False
        return coach_id


    def check_swimmer_exist(self, fname, lname):
        self.cursor.execute('SELECT SwimmerID FROM Swimmers WHERE LastName=? AND FirstName=?', 
        lname, fname)
        swimmer_id = self.cursor.fetchone()
        if swimmer_id is None:
            print('Such a swimmer does not exist in database, insert them first!\n\n')
            return False
        return swimmer_id


    def check_distance_exist(self, distance_name):
        self.cursor.execute('SELECT * FROM Distances WHERE DistanceName=?', distance_name)
        distance = self.cursor.fetchone()
        if distance is None:
            print('Such a distance does not exist in database!\n\n')
            return False
        return True

    def check_city_exist(self, city_name):
        self.cursor.execute('SELECT * FROM Cities WHERE CityName=?', city_name)
        city = self.cursor.fetchone()
        if city is None:
            print('Such a city does not exist in database!\n\n')
            return False
        return True
