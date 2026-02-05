# Step Tracker – Daily Goal Checker
# This script tells you if you reached your daily step goal or active minutes goal

steps = int(input("Enter steps today: "))
active_minutes = int(input("Enter active minutes today: "))

goal_achieved = (steps > 10000 or active_minutes > 30)

if goal_achieved:
    print("🎉 Congrats! You reached your daily activity goal!")
else:
    print("Keep going! You didn't hit your goal yet.")
