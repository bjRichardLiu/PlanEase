from . import db
from .models import User, Task, ReservedTime, WakeUpTime
import numpy as np
import json
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, jsonify


# Get the data of current user
def get_user_schedule():
    user = current_user

    # Get the latest wake-up time
    wakeup_time = user.wakeupTime.order_by(WakeUpTime.id.desc()).first()

    # Get the latest 4 tasks for the user
    tasks = user.tasks.order_by(Task.date.desc()).limit(4).all()

    # Get the latest 2 reserved times for the user
    reserved_times = user.reservedTime.order_by(ReservedTime.date.desc()).limit(2).all()

    # Prepare the data to be sent in the response
    wakeup_time_data = {"wakeUpTime": wakeup_time.wakeUpTime} if wakeup_time else {}
    tasks_data = [{"data": task.data, "date": task.date.isoformat()} for task in tasks]
    reserved_times_data = [{"data": rt.data, "beginTime": rt.beginTime, "endTime": rt.endTime, "date": rt.date.isoformat()} for rt in reserved_times]

    response_data = {
        "wakeupTime": wakeup_time_data,
        "tasks": tasks_data,
        "reservedTime": reserved_times_data
    }

    return response_data, 200

# Add reserved time to the schedule
def add_reserved_time(week, eventID=0, begin=0, end=0, weekDays=False):
    if eventID == 0:
        return week
    begin *= 2
    end *= 2
    if weekDays:
        for i in range(begin, end + 1):
            week[i, :5] = eventID
    else:
        for i in range(begin, end + 1):
            week[i, :] = eventID
    return week
    
    
# Add tasks to the schedule
def add_task(week, eventID=0, time=0, morning=False, wakeUpTime=0, deadline=0):
    if eventID == 0:
        return week, True
    time *= 2
    wakeUpTime *= 2
    if morning:
        week, timeLeft = addEventHelper(week, eventID, time, wakeUpTime, deadline)
        if timeLeft > 0:
            week, timeLeft = addEventHelper(week, eventID, time, 24, deadline)
    else:
        week, timeLeft = addEventHelper(week, eventID, time, 24, deadline)
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
        if time == 0:
            return week, time
        for j in range(endDate):
            if week[i, j] == 0:
                if time == 0:
                    return week, time
                else:
                    week[i, j] = eventID
                    time -= 1

def createNewSchedule():
    intID = 1
    intToTask = []
    intToTask.append("free")
    # Initialize the week using vector
    week = np.zeros((48,7))
    data = get_user_schedule()
    






