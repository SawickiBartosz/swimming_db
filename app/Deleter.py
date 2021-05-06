from Worker import Worker


class Deleter(Worker):

    def run(self):
        print('\n\nWhat do you want to delete?')
        print('1. All swimmers that have 0 starts')
        print('2. All starts older than one year')
        print('3. Coaches who are coaches to 0 swimmers')
        print('4. Selected swimmer')
        print('Anything else to exit')
        choice = input()
        if choice == '1':
            self._delete_swimmers()
        elif choice == '2':
            self._delete_starts()
        elif choice == '3':
            self._delete_coaches()
        elif choice == '4':
            self._delete_selected_swimmer()
        else:
            return
        
    def _delete_swimmers(self):
        self.cursor.execute("""
        DELETE FROM Swimmers WHERE SwimmerID NOT IN (SELECT DISTINCT SwimmerID FROM Starts);
        """)
        self.connection.commit()
        print('Deleted ' + str(self.cursor.rowcount) + ' row(s)')

    def _delete_starts(self):
        import datetime
        today = datetime.date.today()
        one_year_ago = today.replace(year=today.year-1)
        self.cursor.execute("""
        DELETE FROM Starts WHERE StartDate < ?
        """, one_year_ago.strftime('%Y-%m-%d'))
        self.connection.commit()
        print('Deleted ' + str(self.cursor.rowcount) + ' row(s)')

    def _delete_coaches(self):
        self.cursor.execute("""
            DELETE FROM Coaches WHERE CoachID NOT IN (SELECT DISTINCT CoachID FROM Swimmers);
            """)
        self.connection.commit()
        print('Deleted ' + str(self.cursor.rowcount) + ' row(s)')


    def _delete_selected_swimmer(self):
        self.cursor.execute("""
        --sql
        SELECT SwimmerID, LastName, FirstName FROM Swimmers;""")
        print('')
        self._pretty_print()
        swimmer_id = input('Type id of a swimmer to delete: ')
        try:
            self.cursor.execute("""
                DELETE FROM Swimmers WHERE SwimmerID=?;
                """, swimmer_id)
            self.connection.commit()
            print('Deleted ' + str(self.cursor.rowcount) + ' row(s)')
        except Exception as e:
            print(str(e) + '\n')
            print('An error occured. Please try again and check your data\n\n')


