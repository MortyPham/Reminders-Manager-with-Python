 # Reminders Manager
### Video Demo:  https://youtu.be/TZrKlsz6Byw
### Description:
This is my final project for CS50's introduction to programming with Python (CS50P). My project is (aptly) named: ***Reminder Manager***. This project can help you manage all the reminders that you need to be reminded of. There are several actions you can do in this project: add, delete, clear, view, ... All of which are to aid you into finding the best experience to manage all your dates and work.

### Files
There are 5 files in my project when run:

    1. project.py: this is the main area of code for the project
    2. test_project.pt: this is where the tests for the functions in my project.py file are, this file is essential to find the bugs and fix it for my code.
    3. project.csv: this file is created when running project.py
    4. requirements.txt: a file with all the dependencies to run my program
    5. README.md: a mark-up file explaining my project.

### Functions
There are 8 functions in my code:

    1. main()
    2. view()
    3. add()
    4. delete()
    5. clear()
    6. update_list()
    7. sorted_list()
    8. re_check

#### main()
This is my "main" function, where my program is actually ran. After integrating every other functions as well as setting up the ***project.csv*** file and updating the ***reminders*** list, both of those absolutely necessary for the core of the program as these are the main data storers. My ***main()*** function boosts up the menu where users can navigate and manage their reminders, this is also the only place where users can quit and end the program.

#### view()
My ***view()*** function serve its purpose as printing out a table, using the ***tabulate*** library, of every reminders the users has input so far. If there are no reminders, the ***view()*** function outputs:

    You have no reminders.

#### add()
The ***add*** function is where users can input their reminders as the following syntax, using the ***re_check*** function:

    yyyy-mm-dd hh:mm,work

If the input does not fit the syntax, the input is not added. If the input is indeed true to the syntax, the input is then added to the ***project.csv*** file.

#### delete()
Same as the ***add*** function, the ***delete*** function helps users delete unwanted reminders. It outputs a table with all the reminders and their corresponding syntax, users can input a syntax and the corresponding reminder is deleted. However, if there are no more reminders, the function outputs:

    Wrong syntax!

#### clear()
Users use the ***clear*** function to delete every reminders the program has.

#### update_list()
This function helps the ***reminders*** list to has every reminders that the ***project.csv*** file has. It returns a list with all the reminders from the ***project.csv*** file.

#### sorted_list()
This function return a list of reminders that is sorted by date from earliest to latest. This creates a better experience for the users.

### Conclusion:
This project is the fruit of more than 2 weeks of coding and I am quite satisfied with the way it turns out. At first my project's idea is to get together as much things that I learned from CS50P as I could, and that is when I first got the idea of this project. After many days of coding and mostly debugging, the project's shape and size was actually starting to form in my head. Sure, there are many ups and downs in the journey of creating this final project, but looking back, I actually enjoy it very much. And now, finally, it was finished.
