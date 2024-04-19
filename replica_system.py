from starCinema import *


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
        break