import csv
import re
from datetime import datetime
from tabulate import tabulate


def main():
    with open("project.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["date_time", "work"])
    reminders = []
    while True:
        reminders = update_list()
        action_keys = [
            ["v", "view reminders"],
            ["a", "add reminders"],
            ["d", "delete reminders"],
            ["c", "clear reminder"],
            ["q", "quit program"],
        ]
        print(tabulate(action_keys, headers=["key", "action"], tablefmt="heavy_grid"))
        main_input = input("Input key: ")
        match main_input:
            case "q":
                break
            case "v":
                view(reminders)
                view_input = input("Input q to quit: ")
            case "a":
                add(reminders)
            case "d":
                delete(reminders)
            case "c":
                clear(reminders)
            case _:
                print("Wrong syntax!")


# Print out a table with all the reminders in csv file
def view(reminders):
    reminders = update_list()
    if reminders:
        table_reminders = [
            [
                reminders.index(row) + 1,
                row["date_time"].split(" ")[0],
                row["date_time"].split(" ")[1],
                row["work"],
            ]
            for row in reminders
        ]
        print(
            tabulate(
                table_reminders,
                headers=["Index", "Date", "Time", "Work"],
                tablefmt="heavy_grid",
            )
        )
    else:
        print("You have no reminders.")


# Add a reminder to csv file through input
def add(reminders):
    while True:
        add_input = input(
            "Input reminder as follow: yyyy-mm-dd hh:mm,work (press q to quit): "
        )
        if re_check(add_input):
            date_time, work = add_input.split(",")
            with open("project.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["date_time", "work"])
                writer.writerow({"date_time": date_time, "work": work})
        elif add_input.lower() == "q":
            break
        else:
            print("Wrong syntax!")


# Choose a reminder to delete from csv file
def delete(reminders):
    view(reminders)
    while True:
        delete_input = input("Input an index to delete a reminder (press q to quit): ")
        if delete_input == "q":
            break
        elif int(delete_input) in [i for i in range(1, len(reminders) + 1)] and delete_input.isnumeric():
            reminders.pop(int(delete_input) - 1)
            with open("project.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["date_time", "work"])
                for reminder in reminders:
                    writer.writerow(
                        {"date_time": reminder["date_time"], "work": reminder["work"]}
                    )
            view(reminders)
        else:
            print("Wrong syntax!")


# Delete all reminders
def clear(reminders):
    reminders = []
    with open("project.csv", "w") as file:
        for reminder in reminders:
            file.write(reminder)


# Update reminders list from the reminders in csv file
def update_list():
    reminders_ = []
    with open("project.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["date_time", "work"])
        for row in reader:
            reminders_.append({"date_time": row["date_time"], "work": row["work"]})
    return sorted_list(reminders_)


# Sort the reminders in reminders list by date (earliest to farthest)
def sorted_list(reminders):
    date_time_objects = [
        datetime.strptime(date["date_time"], "%Y-%m-%d %H:%M") for date in reminders
    ]
    sorted_date_time_list = [
        datetime.strftime(date, "%Y-%m-%d %H:%M") for date in sorted(date_time_objects)
    ]
    sorted_reminders = []
    for date in sorted_date_time_list:
        for reminder in reminders:
            if reminder["date_time"] == date:
                sorted_reminders.append(reminder)
    return sorted_reminders


# Return a check for valid reminder format
def re_check(string):
    return re.search(
        r"^\d{4}\-(0[\d]|1[012])\-(0[1-9]|[12][0-9]|3[01])\s(0\d|1\d|2[0-3])\:([0-5]\d)\,",
        string,
    )


if __name__ == "__main__":
    main()
