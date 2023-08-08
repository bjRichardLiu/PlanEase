from . import db
from .models import User, Task, ReservedTime, WakeUpTime
import numpy as np
import json
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, jsonify

# Delete all the data of the current user
# Delete the associated Task records
def delete_user_data():
    user = current_user
    Task.query.filter_by(user_id=user.id).delete()

    # Delete the associated ReservedTime records
    ReservedTime.query.filter_by(user_id=user.id).delete()

    # Delete the associated WakeUpTime record
    WakeUpTime.query.filter_by(user_id=user.id).delete()

    # Commit the changes to the database
    db.session.commit()

# Get the data of current user
def get_user_schedule():
    user = current_user

    # Get the latest wake-up time
    wakeup_time = user.wakeupTime[-1] if user.wakeupTime else None

    # Get the latest 4 tasks for the user
    tasks = user.tasks[-4:]

    # Get the latest 2 reserved times for the user
    reserved_times = user.reservedTime[-2:]

    # Prepare the data to be sent in the response
    wakeup_time_data = {"wakeUpTime": wakeup_time.wakeUpTime} if wakeup_time else {}
    tasks_data = [{"data": task.data, 
                   "timePreference": task.timePreference,
                   "deadline": task.deadline,
                   "timeRequired": int(2 * task.timeRequired),
                   "date": task.date.isoformat()} for task in tasks]
    reserved_times_data = [{"data": rt.data, 
                            "id": rt.id,
                            "beginTime": rt.beginTime, 
                            "endTime": rt.endTime, 
                            "date": rt.date.isoformat()} for rt in reserved_times]

    response_data = {
        "wakeupTime": wakeup_time_data,
        "tasks": tasks_data,
        "reservedTime": reserved_times_data
    }

    return response_data, 200

# Add reserved time to the schedule
def add_reserved_time(week, eventID=0, begin=0, end=0):
    if eventID == 0:
        return week
    if begin > end:
        return week
    for i in range(begin, end + 1):
        week[i, :5] = eventID
    return week
    
    
# Add tasks to the schedule
def add_task(week, eventID=0, time=0, timePreference=1, wakeUpTime=0, deadline=5):
    if eventID == 0:
        return week, True
    if timePreference == 0:
        week, timeLeft = addEventHelper(week, eventID, time, wakeUpTime, deadline)
        if timeLeft > 0:
            week, timeLeft = addEventHelper(week, eventID, time, 24, deadline)
    elif timePreference == 1:
        week, timeLeft = addEventHelper(week, eventID, time, 24, deadline)
        if timeLeft > 0:
            week, timeLeft = addEventHelper(week, eventID, time, wakeUpTime, deadline)
    else:
        # Evening starts from 6p.m.
        week, timeLeft = addEventHelper(week, eventID, time, 24 + 12, deadline)
        if timeLeft > 0:
            week, timeLeft = addEventHelper(week, eventID, time, wakeUpTime, deadline)
    # Check if the task is added fully
    if timeLeft > 0:
        return week, False
    else:
        return week, True


# Helper function for add_task
def addEventHelper(week, eventID, time, startTime, endDate):
    for i in range(startTime, startTime + 24):
<<<<<<< Updated upstream
        if time == 0:
=======
        if time == 0 or i >= 48:
>>>>>>> Stashed changes
            return week, time
        for j in range(endDate + 1):
            if week[i, j] == 0:
                if time == 0:
                    return week, time
                else:
                    week[i, j] = eventID
                    time -= 1

def add_sleep_time(week, wakeUpTime=8):
    # From 12a.m. to wakeUpTime
    for i in range(0, wakeUpTime):
        for j in range(0, 5):
            if week[i, j] == 0:
                week[i, j] = 1
    # From 10p.m. to 12a.m.
    for i in range(44, 48):
        for j in range(0, 5):
            if week[i, j] == 0:
                week[i, j] = 1
    return week

# TODO print the schedule to the website

def createNewSchedule():
    intID = 2
    intToTask = []
    intToTask.append({"data": "free", "class": "task-0"})
    intToTask.append({"data": "sleep", "class": "task-1"})

    # Initialize the week using vector
    week = np.zeros((48, 5))

    # Get user schedule data
    data, status_code = get_user_schedule()

    # Extract data from the response data
    wakeup_time_data = data.get("wakeupTime", {})
    tasks_data = data.get("tasks", [])
    reserved_times_data = data.get("reservedTime", [])

    # Add reserved times to the schedule
    for reserved_time in reserved_times_data:
        begin_time = int(reserved_time.get("beginTime", "0"))
        end_time = int(reserved_time.get("endTime", "0"))
        if reserved_time.get("data", "") != "" and begin_time < end_time:
            # print(begin_time, end_time)
            intToTask.append({"data": reserved_time.get("data", ""), "class": "task-" + str(intID)})
            week = add_reserved_time(week, eventID=intID, begin=begin_time, end=end_time)
            intID += 1

    # Add tasks to the schedule
    for task in tasks_data:
        if task.get("data", "") != "" and task.get("timeRequired", 0) != 0:
            intToTask.append({"data": task.get("data", ""), "class": "task-" + str(intID)})
            task_time_required = int(task.get("timeRequired", 0))
            time_preference = int(task.get("timePreference", 1))
            deadline = int(task.get("deadline", 5))
            # Add the task using the add_task function
            week, added_fully = add_task(week, eventID=intID, time=task_time_required, timePreference=time_preference, wakeUpTime=wakeup_time_data.get("wakeUpTime", 0), deadline=deadline)
            intID += 1

    # Add sleep time to the schedule
    week = add_sleep_time(week, wakeUpTime=wakeup_time_data.get("wakeUpTime", 8))
    
    """
    print(week)
    # Print the schedule (TODO: Implement printing schedule to the website)
    for i in range(0,48):
        for j in range(0, 5):
            print(intToTask[int(week[i, j])], end = " ")
        print("\n")
    """
    
    return week, intToTask






