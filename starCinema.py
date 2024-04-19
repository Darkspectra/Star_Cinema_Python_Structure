

class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.entry_hall(self)
    

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [[0] * self._cols for _ in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        for row, col in seat_list:
            if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                print(f"Invalid seat ({row}, {col}).")
                continue
            if self._seats[id][row - 1][col - 1] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self._seats[id][row - 1][col - 1] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        for show in self._show_list:
            print(show)

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        print("Available seats for show", id, "in Hall", self._hall_no)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[id][i][j] == 0:
                    print(f"Seat ({i + 1}, {j + 1})")
        print("===========================")
        print("Seat Matrix for show", id, "in Hall", self._hall_no)
        for row in self._seats[id]:
            print(row)
            
    

        

hall1 = Hall(5, 5, 111)
hall1.entry_show(111, "DUNE Part 2", "9:00 AM")
hall1.entry_show(111, "Sonic 2", "11:00 AM")
hall1.entry_show(111, "Super Mario", "15:00 PM")
# hall1.book_seats(111, [(1, 1), (2, 2), (3, 3)])
# hall1.view_show_list()
# hall1.view_available_seats(111)

# ==============================================================


print("""1. VIEW ALL SHOW TODAY 
2. VIEW AVAILABLE SEATS
3. BOOK TICKET
4. EXIT""")




flag = True

while flag:
    N = int(input("Enter Option: "))
    if (N == 1):
        print("===========================")
        hall1.view_show_list()
        print("===========================")
    
    elif (N == 2):
        hall1.view_available_seats(111)
        print("===========================")
    
    elif (N == 3):
        s_id = int(input("Show ID: "))
        t_id = int(input("Number of Ticket?: "))
        ticket_list = []
    
        for i in range(t_id):
            r = int(input("Enter Seat Row: "))
            c = int(input("Enter Seat Column: "))
            ticket_list.append((r,c))
        hall1.book_seats(s_id, ticket_list)
    
    elif (N==4):
        flag = False
        print("Application has been Terminated")



