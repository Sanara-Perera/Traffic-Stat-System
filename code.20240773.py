#Author: Sanara Perera
#Date: 2024-11-30
#Srudent ID: 2120118



# Task A: Input Validation
def Validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    -Correct data type (Integer Values)
    -Correct range for day (1-31),month (1-12),year (2000-2024)
    Returns the validated date in a string format of 'DD/MM/YYYY'
    """
    #Initiates an infinite loop where the program will keep on asking for an input from the user until a proper input is offered.


    #Prompt for year
    while True:    #Initiates an infinite loop where the program will keep on asking for an input from the user until a proper input is offered.
        try:
            year=int(input("Please enter the year of the survey in the format YYYY: "))  #prompts the user to enter the year in a four digit manner.
            if not year:
                print("Empty input: Please Enter again") #if enter 0 display this message as an empty input
                continue

            year=int(year)
            if 2000<=year<=2024:  #check if the user input is within the given range
                if (year%4==0 and year%100!=0 or year%400==0):   #check if the year is a leap year(divisible by 4 but not by 100 unless divisible ny 400)
                    Leap_year_checking=True  
                    break       #Exit the loop when the year is valid.
                else:
                    Leap_year_checking=False
                    break
            else:
                print("Out of range - Values must be in range 2000 and 2024")  #Error message for invalid range 
                continue
        except ValueError:    #Handle non-integer input
            print("Integer required.Please enter a valid numeric value")   #Error message for invalid input

    #Prompt for month
    while True:
        try:
            month=int(input("Please enter the month of the survey in the format MM: "))  #prompts the user to enter the month in a two digit manner.
            if not month:
                print("Empty input: Please Enter again")   #if enter 0 display this message as an empty input
                continue

            month=int(month)
            if 1<=month<=12:   #check if the user input is within the given range
                break
            else:
                print("Out of range - Values must be in the range on 1 and 12.") #Error message for invalid range
                continue
        except ValueError:   #Handle non-integer input
            print("Integer required. Please enter a valid numeric value")  #Error message for invalid input

    #Prompt for day
    while True:    
        try:
            day = int(input("please enter the day of the survey in the format DD: "))  #prompts the user to enter the day in a two digit manner.
            if not day:
                print("Empty input. Please Enter again")  #if enter 0 display this message as an empty input.
                continue
            month_end_in_31 = [1,3,5,7,8,10,12]   #define months with 30 and 31 days for validation purposes.
            month_end_in_30 = [4,6,9,11]

            #validate day based on the month and leap year status.
            day = int(day)
            if month in month_end_in_31:  #for months with 31 days.
                if 1<=day<=31:
                    break   #Exit the loop when the day in valid.
                else:
                    print("Out of range - Values must be in range 1 and 31")   #Error message for invalid range
                    continue
            elif month in month_end_in_30:   #for months with 30 days.
                if 1<=day<=30:
                    break    #Exit the loop when the day in valid.
                else:
                    print("Out of range - Values must be in range 1 and 30")  #Error message for invalid range
            else:
                if (Leap_year_checking == True):
                    if 1<=day<=29:   #for february validate based on leap year status.
                        break    #Exit the loop for valid leap year day.
                    else:
                        print("Out of range - Values must be in range 1 and 29")  #Error message for invalid range
                else:
                    if 1<=day<=28:
                        break     #Exit the loop for valid non leap year day.
                    else:
                        print("Out of range - Values must be in range 1 and 28")  #Error message for invalid range
            
        except ValueError:   #Accepts non-numeric inputs and informs the user by displaying this message without terminating the programm.
            print("Integer required.Please enter a valid numeric value") #If the input is a non-numeric value display this message and restart the loop.

    day = str(day).zfill(2)   #Format the day and month with leading zeros if necessary
    month = str(month).zfill(2)
    year = str(year)  #Convert the year into string for file path construction.         
    file_pathway = f"traffic_data{day}{month}{year}.csv"
    return file_pathway


def Validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    -Accepts input "Y" or "N". (case-insensitive)
    -Re-prompts the user until valid input is provided.
    Returns True if the user enters "Y", otherwise returns False.
    """
    #Initiates an infinite loop where the program will keep on asking for an input from the user until a proper input is offered.
    while True:
        user_input = input("Do you want to load another data set for a different date? Y/N: ").upper()#input = prompts the user with the given message.
                                                                                                              #.strip()=removes any leading/ending spaces that might be entered unintentionally.
                                                                                                              #.upper()=converts the input to uppercase so that the inputs are case-insensitive.

        if user_input == "Y": #if the input is "Y", user wants to continue.
            return True

        elif user_input == "N": #if the input us "N", user wants to exit.
            return False

        else:
            print('Invalid input. Please enter "Y" or "N".') #if the input is invalid, display this message and restart the loop.
        




# Task B: Processed Outcomes
def process_csv_data(file_pathway):
    """
    Processes the CSV data for the selected date and extracts:
    - Total Vehicles
    - Total Trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    Returns a dictionary with all the calculates outcomes.
    """
    # Dictionary to store various calculated outcomes.
    outcomes = {       
       "file_pathway": file_pathway,
       "total_vehicles":0,   #count of all vehicles
       "total_trucks":0,    #count of all trucks 
       "electric_vehicles":0,  #count of all electric vehicles
       "two_wheeled_vehicles":0,  #count of two-wheeled vehicles(scooters, bicycles )
       "total_bikes":0,  #count of bicycles
       "buses_through_elm_to_N":0,  #count of buses traveling north through Elm avenue
       "no_turning_vehicles":0,  #count of vehicles not turning at any junction
       "over_speed_limit":0,   #count of vehicles exceeding the speed limit
       "vehicles_ElmAvenue_RabbitRoad":0, #count of vehicles passing through Elm Avenue/Rabbit Road
       "vehicles_HanleyHighway_Westway":0, #count of vehicles passing through Hanley Highway/Westway
       "scooter_through_elm":0,  #count of scooters passing through Elm Avenue
       "vehicles_in_peak_Hanley":0, #count of vehicles in the peak hour at Hanley Highway
       "hourly_traffic_hanley":{}, #hourly breakdown of traffic at Hanley Highwa
       "rain_hours":0,  #count of hours with rain.
       "trucks_percentage":0,  #percentage of trucks out of total vehicles
       "scooter_percentage":0,  #percentage of scooters at Elm Avenue/Rabbit Road
       "average_bicycles_per_hour":0,  #Average number of bicycles recorded per hour
       "max_traffic":0, #maximum traffic in any hour
       "peak_time_hanley_string": 0  #String describing the peak traffic times
    }
    
    hourly_vehicles={}   #Dictionary to store hourly vehicle counts
    peak_times =[]   #List to store peak traffic times
    peakhour_vehicles = 0  #Initialize peak hour vehicle count
    
   

    try:
        with open(file_pathway ,'r') as file:  #open the csv file
            next(file)   #skip the header row 
            lines = file.readlines() #read all lines in the file 

            #Process each line in the CSV file
            for line in lines:
                columns=line.strip().split(",")    #split line into columns by comma[reference: https://www.w3schools.com/python/ref_string_split.asp]
                outcomes["total_vehicles"] += 1    #count total vehicles    
                
                #count total trucks
                if columns[8] == "Truck":
                    outcomes["total_trucks"] += 1

                #count electric vehicles
                if columns[9] == "True":
                    outcomes["electric_vehicles"] += 1

                #count two-wheeled vehicles
                if columns[8].strip() == "Scooter" or columns[8].strip() == "Bicycle" or columns[8].strip() == "Motorcycle":  #[reference- https://www.w3schools.com/python/ref_string_split.asp]
                    outcomes["two_wheeled_vehicles"] += 1

                #count buses heading north through Elm Avenue
                if columns[8] == "Buss" and columns[4] == "N" and columns[0] == "Elm Avenue/Rabbit Road":
                    outcomes["buses_through_elm_to_N"] += 1
                    
                #count vehicles not turning
                if columns[3] == columns[4]:
                    outcomes["no_turning_vehicles"] += 1

                #calculate trucks percentage
                outcomes["trucks_percentage"] = round((outcomes["total_trucks"]/outcomes["total_vehicles"])*100)

                #count bicycles and average number of bicycles per hour
                if columns[8] == "Bicycle":
                    outcomes["total_bikes"] += 1
                    outcomes["average_bicycles_per_hour"] =round(outcomes["total_bikes"]/24)

                #count vehicles over the speed limit
                if int(columns[7])>int(columns[6]):
                    outcomes["over_speed_limit"]+=1

                #total vehicles recorded through Elm Avenue/Rabbit Road junction
                if columns[0] == "Elm Avenue/Rabbit Road":
                    outcomes["vehicles_ElmAvenue_RabbitRoad"] += 1

                #total vehicles recorded through Hanley Highway/Westway junction
                if columns[0] == "Hanley Highway/Westway":
                    outcomes["vehicles_HanleyHighway_Westway"] += 1

                #percentage of scooters through Elm Avenue
                if columns[8] == "Scooter" and columns[0] == "Elm Avenue/Rabbit Road":
                    outcomes["scooter_through_elm"] += 1
                    outcomes["scooter_percentage"] = round((outcomes["scooter_through_elm"]/outcomes["vehicles_ElmAvenue_RabbitRoad"])*100)

                #number of vehicles recorded in the peak hour on Hanley Highway/Westway
                for row in file:
                    if columns[0]=="Hanley Highway/Westway":
                        hour=row[2][:2]
                        if hour in hourly_vehicles:
                            hourly_vehicles[hour]+=1   #adds one to that specific key
                        else: #if the certain key in not in the dict.
                            hourly_vehicles[hour]=1    #assigns one to that key

                        if hourly_vehicles:
                            for hour in hourly_vehicles:
                                max_count=max(max_count, hourly_vehicles[hour])
                                peakhour_vehicles=max_count
                        else:
                            peakhour_vehicles=0
                            
                #track hourly traffic and identify peak hours
                if columns[0].strip()=="Hanley Highway/Westway":
                    hour=columns[2][:2]    #extract hour from timestamp[reference- https://stackoverflow.com/questions/19350806/how-to-convert-columns-into-one-datetime-column-in-pandas]
                    hourly_vehicles[hour]=hourly_vehicles.get(hour, 0)+1

                    if hourly_vehicles[hour]>peakhour_vehicles:
                        peakhour_vehicles = hourly_vehicles[hour]
                        peak_times = [f"Between {hour}:00 and {int(hour)+1}:00"]
                    elif hourly_vehicles[hour] == peakhour_vehicles:
                        peak_times.append(f"Between {hour}:00 and {int(hour)+1}:00")  #[reference- https://www.w3schools.com/python/ref_list_append.asp]

                    outcomes['peak_time_hanley_string'] = ", ".join(peak_times)#This gives the output without square brackets by jining all elements of peak_times into a single string, separated by a comma and space
                    

                #Total hours of rain
                rain = set()  #use set to avoid duplicate hours
                for line in lines:
                    columns = line.strip().split(",")
                if columns[5].strip().lower() == "light rain" or columns[5].strip().lower() == "heavy rain":
                    rain.add(columns[2][:2])   #add hour to set if rain occured
            outcomes["rain_hours"] = len(rain) #total number of rainy hours

    
            
            return   [f"*******************\n"
                      f"Data file selected is {outcomes["file_pathway"]}\n" 
                      f"*******************\n"
                      f"The total number of vehicles recorded for this date is {outcomes['total_vehicles']}\n"
                      f"The total number of trucks recorded for this date is {outcomes['total_trucks']}\n"
                      f"The total number of electric vehicles for this date is {outcomes['electric_vehicles']}\n"
                      f"The total number of two-wheeled vehicles for this date is {outcomes['two_wheeled_vehicles']}\n"
                      f"The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes['buses_through_elm_to_N']}\n"
                      f"The total number of Vehicles through both junctions not turning left or right is {outcomes['no_turning_vehicles']}\n"
                      f"The percentage of total vehicles recorded that are trucks for this date is {outcomes['trucks_percentage']:.0f}%\n"
                      f"The average number of Bikes per hour for this date is {outcomes['average_bicycles_per_hour']}\n"
                      f"The total number of vehicles recorded as over the speed limit for this date is {outcomes['over_speed_limit']}\n"
                      f"The total vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['vehicles_ElmAvenue_RabbitRoad']}\n"
                      f"The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['vehicles_HanleyHighway_Westway']}\n"
                      f"{outcomes['scooter_percentage']:.0f}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters\n"
                      f"The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes['max_traffic']}\n"
                      f"The most vehicles through Hanley Highway/Westway were recorded between {outcomes['peak_time_hanley_string']}\n"
                      f"The number of hours of rain for this date is {outcomes['rain_hours']}\n" ]


    
    
    except FileNotFoundError:    #handle file not found error
        print(f"{file_pathway} not found")   #display error message

def display_outcomes(outcomes):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    for Outcome_row in outcomes:
        print(Outcome_row)



# Task C: Save Results into a Text File

def save_results_to_file(outcomes, file_name = "results.txt"):

    with open(file_name, 'a') as file:
        for printer in outcomes:
            file.write(f"{printer}\n")
        file.write("\n*\n")

# Task D: Histogram Display
# File: histogram_display.py
import tkinter as tk  #Import Tkinter library for creating GUI applications
import csv  #Import CSV library for reading CSV files
from datetime import datetime

class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initialize the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data  #Store the traffic data
        self.date = date  #Store the selected date for the histogram
        self.root = tk.Tk()  #Create the main Tkinter window
        self.canvas = None   #Initialize a canvas for drawing the histogram

    def setup_windows(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.root.title("Histogram")   #Set the title of the histogram window
        self.root.geometry("1500x900")  #Set the dimensions of the window
        self.canvas = tk.Canvas(self.root, width=1500, height=900, bg="white") #Create a canvas to draw on
        self.canvas.pack() #Add the canvas to the Tkinter window

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        hourly_data = self.process_hourly_data()   #Process the hourly traffic data to get counts for each hour and junction
        max_count = max(
            [count for hour, junction in hourly_data.items() for count in junction.values()]  #Find the maximum vehicle count to scale bar heights
        )
        gap_between_groups = 55  #Space between groups of bars for different hours
        bar_width = 20  #Width of each bar
        x_offset = 100  #Starting x-position for the bars
        y_offset = 600  #y-position of the x-axis
        group_gap = gap_between_groups - 2 * bar_width  #Space between groups of bars

        color_codes = {
            "Elm Avenue/Rabbit Road": "#00FF7F",  #SpringGreen for Elm Avenue/Rabbit Road
            "Hanley Highway/Westway": "#FFA07A"   #LightSalmon for hanley highway/Westway
        }

        # Draw axes
        self.canvas.create_line(x_offset, y_offset, 1421, y_offset, width=2)  #Draw the X-axis
        self.canvas.create_line(x_offset, y_offset, x_offset, 55, width=2)    #Draw the Y-axis

        # Add labels to the axes
        self.canvas.create_text(760, 675, text="Hours 00:00 to 24:00", font=("Arial", 12))    #Label for the X-axis
        self.canvas.create_text(70, 300, text="Vehicle Count", font=("Arial", 12), angle=90)  #Label for the Y-axis

        #Starting x-position for the 1st group of bars
        current_x = x_offset + group_gap

        #Loop through hourly data to draw bars for each hour and junction
        for hour, counts in hourly_data.items():
            for junction, count in counts.items():
                bar_height = (count / max_count) * 350  #Calculate the height of each bar proportional to the maximum count
                bar_color = color_codes[junction]   #Get the color for the junction

                # Draw the bar
                self.canvas.create_rectangle(
                    current_x, y_offset - bar_height,  #Top-left corner of the bar
                    current_x + bar_width, y_offset,   #Bottom-right corner of the bar
                    fill=bar_color, outline="black"    #Fill color and border color
                )

                # Draw the count label above the bar
                self.canvas.create_text(
                    current_x + (bar_width // 2),  # Center the text above the bar
                    y_offset - bar_height - 10,   # Position the text slightly above the bar
                    text=str(count),              # Display the vehicle count
                    font=("Arial", 10),           # Font size and style
                    fill="black"                  # Text color
                )

                current_x += bar_width

            # Draw the hour label after the group
            self.canvas.create_text(
                current_x - (2 * bar_width) + (group_gap // 2),  #Center the hour label below the bars
                y_offset + 20,
                text=hour,
                font=("Arial", 10)
            )
            current_x += group_gap   #Move to the next group of bars

    def process_hourly_data(self):
        """
        Processes the hourly traffic data into a structured format.
        """
        hourly_counts = {str(i).zfill(2): {"Elm Avenue/Rabbit Road": 0, "Hanley Highway/Westway": 0} for i in range(24)} #Initialize a dictionary to store counts for each hour and junction
        for record in self.traffic_data:
            hour = record['timeOfDay'].split(":")[0]  #Extract the hour from the time
            junction = record['JunctionName']    #Get the junction name
            if hour in hourly_counts:
                hourly_counts[hour][junction] += 1   #Increase the count for the junction and hour
        return hourly_counts

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """

        #Draw the legend for Elm Avenue/Rabbit Road
        self.canvas.create_rectangle(220, 130, 200, 150, fill="#00FF7F", outline="black")
        self.canvas.create_text(225, 140, text="Elm Avenue/Rabbit Road", anchor="w", font=("Arial", 10))

        #Draw the legend for Hanley Highway/Westway
        self.canvas.create_rectangle(220, 160, 200, 180, fill="#FFA07A", outline="black")
        self.canvas.create_text(225, 170, text="Hanley Highway/Westway", anchor="w", font=("Arial", 10))

        #Add a little for the histogram
        self.canvas.create_text(
            445, 90,
            text=f"Histogram of vehicle frequency per hour - {self.date}",
            font=("Arial", 16)
        )

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_windows()     #Set up the window and canvas
        self.draw_histogram()    #Draw the bars and labels
        self.add_legend()        #Add the legend to the histogram
        self.root.mainloop()     #run the Tkinter event loop

    
# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.traffic_data = None  # Store the current dataset

    def load_csv_files(self, file_pathway):
        """
        Loads a CSV file and processes its data.
        """
        try:
            with open(file_pathway, 'r') as file:
                reader = csv.DictReader(file)    #Read the CSV file into a dictionary
                self.traffic_data = [row for row in reader]  #Store the data
            print(f"Data loaded from {file_pathway}")
        except FileNotFoundError:
            print(f"Error: File {file_pathway} not found.")  #Handle file not found error
            self.traffic_data = []
        except Exception as e:
            print(f"Error loading file {file_pathway}: {e}")  #Handle other exceptions
            self.traffic_data = []

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        self.traffic_data = []   #Reset the traffic data

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        while True:
            user_input = input("Do you want to select a data file for a different date? (Y/N): ").strip().lower()
            if user_input == 'y':
                file_pathway = input("Enter the file pathway: ").strip()
                self.clear_previous_data()
                self.load_csv_files(file_pathway)
                date = input("Enter the date for this dataset (DD/MM/YYYY): ").strip()
                app = HistogramApp(self.traffic_data, date)
                app.run()
            elif user_input == 'n':
                print("Exiting the program.")
                return user_input
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
            
    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        Runs Task A (Input Validation), Task B (Data Processing),
        Task C (Save Results), and Task D (Display Histogram) sequentially.
        """
        while True:
            # Task A: Input Validation
            file_pathway = Validate_date_input()
            if not file_pathway:
                print("Invalid file path. Please try again.")
                continue

            # Task E: Load the CSV file
            self.load_csv_files(file_pathway)

            # If no data is loaded, skip to the next iteration
            if not self.traffic_data:
                print("No valid data found in the file. Please try another file.")
                continue

            # Task B: Process the CSV data
            outcomes = process_csv_data(file_pathway)
            if not outcomes:
                print("No data found in the file. Please try another file.")
                continue

            # Task C: Display and Save Results
            display_outcomes(outcomes)
            save_results_to_file(outcomes)

            # Task D: Display the Histogram
            try:
                date = file_pathway.replace("traffic_data", "").replace(".csv", "")
                app = HistogramApp(self.traffic_data, date)
                app.run()
            except Exception as e:
                print(f"Error displaying histogram: {e}")

            # Task E: Ask the user if they want to process another file
            repeat_program = Validate_continue_input()
            if not repeat_program:
                print("Exiting the program. Goodbye!")
                break


#Main Entry Point
if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.process_files()

            
            

            
