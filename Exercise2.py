#Double Scoop with Nested Loops
#Task 1: Your Mood Tracker


days = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday"]
times = [ "Morning", "Afternoon", "Evening"]
moods = ["Jovial","Angry", "Overwhelmed", "Happy", "Tired", "Sad", "Pensive" ]


import random
for i in range(7):
    for n in range(3):
        print(f"On {days[i]} {times[n]} you were {random.choice(moods)}.")



