from . import db
from .models import User, Task, ReservedTime, WakeUpTime
import numpy as np
import json
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, jsonify

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

def createNewSchedule():
    intID = 1
    intToTask = []
    intToTask.append("free")
    # Initialize the week using vector
    week = np.zeros((48,7))
    data = get_user_schedule()
    






