from datetime import datetime
import csv

choice = ''
while choice != 5:
    def welcome():
        """This is the welcome page and displays options available to user"""
        
        print("""
        WELCOME BARBARA!

        What would you like to do today?

        1. Begin a lesson
        2. Check money made today
        3. Check money made for a specific day
        4. Check total amount of money made
        5. Quit program
    """)

    def write(file,start_time, end_time, hours,money):
        """This is where we write and save to our documment"""
        
        #Headings of columns for various data stored
        field_names = ["Start Date and Time", "End Date and Time",
                        "Time Spent(in hours)",  "Money made(in dollars)"]

        #This creates a new file with the specified filename if file already isn't available
        f = open(file,"a")
        f.close()

        #This opens file to check if the file is empty.
        with open(file, 'r') as f:
            read_file = [row for row in csv.DictReader(f)]
            if len(read_file)==0:
                empty = True
            else:
                empty = False

        #This writes the heading to the file if file is empty before saving 
        #generated data
        with open(file, "a") as data_file:
            file_write = csv.DictWriter(data_file, field_names,lineterminator ='\n')
            if empty:
                file_write.writeheader()
            else:
                pass
            file_write.writerow(
                {"Start Date and Time": start_time,
                "End Date and Time": end_time,
                "Time Spent(in hours)": hours,
                "Money made(in dollars)": money})

    def read(file,date=""):
        """This function accesses stored data and calculates for money made for
            a particular period of time"""

        #This block calculates and returns total amount of money made so far
        if date =="":
            total_money = 0
            with open(file, 'r') as f:
                read_file = csv.DictReader(f)
                for row in read_file:
                    total_money += float(row["Money made(in dollars)"])
                    total_money = round(total_money,5)
            return total_money

        else:
            #This block calculates and returns amount of money made on a particular day
            new_formatted_date = datetime.strptime(date,'%m/%d/%y')
            new_date = new_formatted_date.strftime('%Y-%m-%d')

            today_money = 0
            with open(file, 'r') as f:
                read_file = csv.DictReader(f)
                for row in read_file:
                    if new_date == row["Start Date and Time"][:10]:
                        today_money += float(row["Money made(in dollars)"])
                        today_money = round(today_money,5)
                    else:
                        pass
                return today_money

    def money_made(hours):
        """This function generates the amount of money made"""
        money = round(hours*5, 6)
        return money

    def main():
        """This is our main program. It controls the entire program"""
        welcome()
        choice = int(input("Please select an option: "))

        while choice not in list(range(1,6)):
            print("Invalid option!")
            choice = int(input("Select a valid option: "))

    
        if choice == 1:
            start_time = datetime.now()
            print("Lesson for " + start_time.strftime("%x") +" has began at " + start_time.strftime("%X"))
        
            print("\nLesson is now in progress!\n")
            input("Press <Enter> to end lesson")

            end_time = datetime.now()
            time_difference = end_time - start_time
            hours = round(time_difference.total_seconds()/3600, 5)

            print("Lesson for " + end_time.strftime("%x") + " ended at " + end_time.strftime("%X"))
            print("You spent " + str(hours) + " hours on this lesson")
            money = money_made(hours)
            print("You made $" +str(money)+" for this session")
            write("data.csv",start_time,end_time, hours,money)
            start_time=""


        if choice == 2:
            today = datetime.now()
            formatted_date = today.strftime('%D')
            today_money = read('data.csv',date=formatted_date)
            print("You have made $" + str(today_money) + " today")
        

        if choice == 3:
            try:
                date = input("Enter date (mm/dd/yy): ")
                amount = read('data.csv',date)
            except:
                date = input("\nEnter date in the mm/dd/yy format\nExample: 12/28/20 \t\t:  ")
                amount = read("data.csv",date)

            print("You made $" + str(amount) + " on "+date)

        if choice == 4:
            total_money_made = read('data.csv')
            print("You have made $"+ str(total_money_made)+" so far")

        return choice

    
    try:
        choice = main()
    except FileNotFoundError:
        print("No data exists to perform this operation. Please begin a lesson to generate data")
    
    input("\nPress <Enter> to continue")
print("GOODBYE!!!")
