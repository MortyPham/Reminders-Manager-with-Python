import csv
from project import update_list, sorted_list, re_check


def test_update_list():
    with open("project.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date_time", "work"])
        writer.writerow({"date_time": "2024-07-14 12:30", "work": "go to the dentist"})
        writer.writerow({"date_time": "2024-06-30 15:45", "work": "tennis practice"})
        writer.writerow(
            {"date_time": "2024-07-01 09:00", "work": "video call with friends"}
        )
    assert update_list() == [
        {"date_time": "2024-06-30 15:45", "work": "tennis practice"},
        {"date_time": "2024-07-01 09:00", "work": "video call with friends"},
        {"date_time": "2024-07-14 12:30", "work": "go to the dentist"},
    ]


def test_sorted_list():
    assert sorted_list(
        [
            {"date_time": "2024-07-14 12:30", "work": "go to the dentist"},
            {"date_time": "2024-06-30 15:45", "work": "tennis practice"},
            {"date_time": "2024-07-01 09:00", "work": "video call with friends"},
        ]
    ) == [
        {"date_time": "2024-06-30 15:45", "work": "tennis practice"},
        {"date_time": "2024-07-01 09:00", "work": "video call with friends"},
        {"date_time": "2024-07-14 12:30", "work": "go to the dentist"},
    ]


def test_re_check():
    assert re_check("2024-07-01 09:00, video call with friends") != None
