#The Range Riddle
#Task 1: Your Mood Today


moods = [ "Happy", "Angry", "Sad", "Pensive", "Ecstatic", "Jovial", "Energetic"]
days= ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


import random
for z in range(7):
    print(f"On {days[z]}, you were feeling {random.choice(moods)}")