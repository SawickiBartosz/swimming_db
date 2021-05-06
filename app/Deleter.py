
class Deleter():
    
    def __init__(self, connection, cursor, checker):
        self.connection = connection
        self.cursor = cursor
        self.checker = checker

    def run(self):
        print('\n\nWhat do you want to delete?')
        print('1. All swimmers that have 0 starts')
        print('2. All starts older than one year')
        print('3. Coaches who are coaches to 0 swimmers')
        # TODO usuwanie wybranego zawodnika
        print('Anything else to exit')
        choice = input()
        if choice == '1':
            self._delete_swimmers()
        elif choice == '2':
            self._delete_starts()
        elif choice == '3':
            self._delete_coaches()
        else:
            return
        
    def _delete_swimmers(self):
        self.cursor.execute("""
        DELETE FROM Swimmers WHERE SwimmerID NOT IN (SELECT DISTINCT SwimmerID FROM Starts);
        """)
        self.connection.commit()
        print('Deleted ' + str(self.cursor.rowcount) + ' rows')

    def _delete_starts(self):
        import datetime
        today = datetime.date.today()
        one_year_ago = today.replace(year=today.year-1)
        self.cursor.execute("""
        DELETE FROM Starts WHERE StartDate < ?
        """, one_year_ago.strftime('%Y-%m-%d'))
        self.connection.commit()
        print('Deleted ' + str(self.cursor.rowcount) + ' rows')

    def _delete_coaches(self):
        self.cursor.execute("""
            DELETE FROM Coaches WHERE CoachID NOT IN (SELECT DISTINCT CoachID FROM Swimmers);
            """)
        self.connection.commit()
        print('Deleted ' + str(self.cursor.rowcount) + ' rows')
