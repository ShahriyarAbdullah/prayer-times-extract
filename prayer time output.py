import monthcalc
import timeconverter as alpha
import os
import time

# Compiled and tested by Shahriyar Abdullah
# "monthcalc" and "timeconverter" modules have been compiled and tested by Shahriyar Abdullah

os.system('cls')
print("Please input the name/path of text file containing the prayer timetable below.")
print("It is recommended to keep the text file in the same directory as this script to avoid dealing with paths.")
print("In the specified text file, each line must contain salah times delimited by commas in the file (hence the .csv format is recommended; regular text files are also fine).")
print("Each line should be in the format: FB,FJ,SR,DB,DJ,AB,AJ,Maghrib,Maghrib,IB,IJ (The duplicated 'Maghrib' time is intentional)")
print("For example: 06:27,06:45,08:02,12:01,01:00,01:40,02:30,03:56,03:56,05:25,07:15")
print("FB stands for Fajr Begin")
print("FJ stands for Fajr Jamaat")
print("SR stands for Sunrise")
print("DB stands for Dhuhr Begin")
print("...and so on.")
print("-------------------------") # Above is the explanation of what the contents of the file they are inputting must contain and in what way the contents should be laid out
tt_fileinput = input("File Name/Path (including file extension e.g. .txt, .csv, etc.): ")
os.system('cls')
if '"' in tt_fileinput:
    tt_fileinput = tt_fileinput.replace('"', '')
    print("You have inputted the file: " + tt_fileinput)
    time.sleep(1)
    print("This message will disappear in 5 seconds. If the name/path is wrong, press Ctrl+C to stop the script now.")
    time.sleep(5)
    os.system('cls')
else:
    print("You have inputted the file: " + tt_fileinput)
    time.sleep(1)
    print("This message will disappear in 5 seconds. If the name/path is wrong, press Ctrl+C to stop the script now.")
    time.sleep(5)
    os.system('cls')

# The user will input the month, which will be assigned to the "monthin" variable
monthin = input("Please input the first 3 letters of the name of the month you want the code to output for, e.g. Mar. If the month is February and is in a leap year, input Fel (case-sensitive): ")
os.system('cls')
month_var = monthcalc.Month(monthin) # Usage of the Month class to establish how many days are in the inputted month

monthlist = []
for day in range(1, int(month_var.daycalc() + 1)): # Range starting from 1 and ending on an integer before day + 1
    if monthin != "Fel":
        if day < 10:
            monthlist.append(monthin + " " + "0" + str(day) + "--")
        elif day >= 10:
            monthlist.append(monthin + " " + str(day) + "--")
    elif monthin == "Fel":
        if day < 10:
            monthlist.append(monthin.replace('l', 'b') + " " + "0" + str(day) + "--")
        elif day >= 10:
            monthlist.append(monthin.replace('l', 'b') + " " + str(day) + "--")
# This for loop generates the "Month Day--" prefixes and adds them to the list "monthlist", e.g. ["Dec 01--", "Dec 02--", "Dec 03--", ... ]

# STAGE 1 IS COMPLETE

timetablecsv = open(tt_fileinput, "r")

for day in monthlist:
    for line in timetablecsv:
        codeline = line.split(',') # Splitting all times into entities in the list "codeline"
        new24hr = []
        for time in range(3, len(codeline)):
            new24hr.append(alpha.tfhour(codeline[time])) # Iterating through each time in the "codeline" list from the 4th time (Dhuhr Begin) and appending the new 24hr time to "new24hr"
        codeline[3:] = new24hr # Adding the new converted times to the original "codeline" list of times from DB (index 3/entity 4) onwards
        newcode = '--'.join(codeline) # Converting the "codeline" list into a string, separating each time entity with '--' separator
        fullcode = day + newcode # Appending the "Month Day--" prefix onto the string, e.g. "Dec 01--". The "for day in monthlist" loop iterates through the "monthlist" list created in Stage 1
        print(fullcode) # Printing the finalised line of code, this will print out each new line of code for each day individually
        break # Exit the inner loop after printing one line of code

timetablecsv.close() # STAGE 2 IS COMPLETE. By now the required lines of code should have been printed onto the terminal.