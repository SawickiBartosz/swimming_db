from Worker import Worker

class Reporter(Worker):
    def run(self):
        print('\n\nWhat kind of report you want to generate?')
        print('1. Personal best times of a swimmer')
        print('2. Ranking of a distance')
        print('Anything else to exit')
        choice = input()
        if choice == '1':
            self._report_pb()
        elif choice == '2':
            self._report_ranking()
        else:
            return

    def _report_pb(self):
        print('\nWhose personal bests you want to show?')
        last_name = input('Last name: ')
        first_name = input('First name: ')

        swimmer_id = self.checker.check_swimmer_exist(first_name, last_name)
        if not swimmer_id:
            return
        self.cursor.execute("""--sql
            SELECT  d.DistanceName, 
                    MIN(SwimTime) AS PersonalBest, 
                    StartDate 
            FROM Starts s 
            JOIN Distances d on s.DistanceName=d.DistanceName
            JOIN Swimmers sw on s.SwimmerID=sw.SwimmerID
            WHERE sw.FirstName = ? AND sw.LastName = ?
            GROUP BY d.DistanceName, 
                    StartDate;""", 
                first_name, last_name)
        self._pretty_print()

    def _report_ranking(self):
        print('\nWhich distance you want to show?')
        distance_name = input('Distance : ')

        if not self.checker.check_distance_exist(distance_name):
            return

        self.cursor.execute("""--sql
            SELECT  sw.FirstName AS FirstName,
                    sw.LastName AS LastName, 
                    MIN(SwimTime) AS BestTime,
                    CONCAT(c.FirstName, ' ' ,c.LastName) AS CoachName,
                    cl.ClubName AS ClubName
            FROM Starts s 
            JOIN Swimmers sw on s.SwimmerID=sw.SwimmerID
            JOIN Coaches c on sw.CoachID=c.CoachID
            JOIN Clubs cl on cl.ShortName=sw.ClubShortName
            WHERE DistanceName = ?
            GROUP BY 
                sw.SwimmerID, 
                sw.FirstName, 
                sw.LastName, 
                cl.ClubName, 
                c.FirstName, 
                c.LastName
            ORDER BY BestTime ASC;""",
            distance_name)
        self._pretty_print()
