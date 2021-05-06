class Worker():
    def __init__(self, connection, cursor, checker):
        self.connection = connection
        self.cursor = cursor
        self.checker = checker

    def _pretty_print(self):
        n_col = len(self.cursor.description)
        max_length_column = []
        report = self.cursor.fetchall()
        report.insert(0, [x[0] for x in self.cursor.description])
        for i in range(n_col):
            max_length_column.append(max(len(str(e[i]))+2 for e in report))    

        for e in report:
            for i in range(n_col):
                print(str(e[i]).ljust(max_length_column[i]), end='')
            print()
        print('\n\n---------------------')
