from flask import render_template, Blueprint, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .service import createNewSchedule
import numpy as np

schedule = Blueprint('schedule', __name__)

# Global variable to store the intID
intID = 1

@schedule.route('/schedule', methods=['GET', 'POST'])
@login_required
def display_schedule():
    schedule_data = generate_schedule()
    return render_template("schedule.html", schedule=schedule_data)

# The following code is for generating the schedule data

def generate_schedule():
    week, intToTask = createNewSchedule()

    # Prepare the schedule data to be sent to the template
    schedule_data = []
    for i in range(24):
        time1 = f'{i // 2:02d}:{i % 2 * 30:02d}'
        j = i + 24
        time2 = f'{j // 2:02d}:{j % 2 * 30:02d}'
        row_data = {
            'time1': time1,
            'monday1': intToTask[int(week[i, 0])],
            'tuesday1': intToTask[int(week[i, 1])],
            'wednesday1': intToTask[int(week[i, 2])],
            'thursday1': intToTask[int(week[i, 3])],
            'friday1': intToTask[int(week[i, 4])],
            'time2': time2,
            'monday2': intToTask[int(week[j, 0])],
            'tuesday2': intToTask[int(week[j, 1])],
            'wednesday2': intToTask[int(week[j, 2])],
            'thursday2': intToTask[int(week[j, 3])],
            'friday2': intToTask[int(week[j, 4])],
        }
        schedule_data.append(row_data)

    # Return the schedule data
    return schedule_data

