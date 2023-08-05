from . import db
from .models import User, Task, ReservedTime, WakeUpTime
import numpy as np



intID = 1
intToTask = []
intToTask.append("free")
# Initialize the week using vector
week = np.zeros((48,7))





