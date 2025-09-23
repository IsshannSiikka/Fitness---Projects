
workouts = []

def add_workout(day, pushups, pullups, hiit_minutes, bodypart_trained, calories_burned):
    workout = {
         "day": day,
        "pushups": pushups,
        "pullups": pullups,
        "hiit_minutes": hiit_minutes,
        "bodypart_trained": bodypart_trained,
        "calories_burned ": calories_burned
    }
    workouts.append(workout)

add_workout("Monday", 400, 0, 20, "Back", 700)
add_workout("Tuesday", 400, 0, 20, "Shoulders", 650)

    
print("Workout Log :")
for w in workouts:
    print(w)
        
#Little indentation trap :
# . Inside the function = Python thinks it's part of the function.
# . Outside = it actually runs after the function is defined.

#STEP 2 - Weekly Summary
# . Counts total pushups & pullups 
# . Sums total HIIT minutes & calories burned 
# . Calculates averages per day 


workouts = []

def add_workout(day, pushups, pullups, hiit_minutes, bodypart_trained, calories_burned):
    workout = {
         "day": day,
        "pushups": pushups,
        "pullups": pullups,
        "hiit_minutes": hiit_minutes,
        "bodypart_trained": bodypart_trained,
        "calories_burned ": calories_burned
    }
    workouts.append(workout)


def weekly_summary() :
    total_pushups = sum(w["pushups"] for w in workouts)
    total_pullups = sum(w["pullups"] for w in workouts)
    total_hiit = sum(w["hiit_minutes"] for w in workouts)    
    total_calories = sum(w["calories_burned"] for w in workouts)

    days = len(workouts)

    print("\n---Weekly Summary---")
    print(f"Days tacked : {days}")
    print(f"Total Pushups : {total_pushups}")
    print(f"Total Pullups : {total_pullups}")
    print(f"Total Hiit minutes : {total_hiit}")
    print(f"Total Calories burned : {total_calories}")
    print(f"Average Pushups per day : {total_pushups // days}")
    print(f"Average Calories burned per day : {total_calories // days}") 

add_workout("Monday", 400, 0, 20, "Back", 700)
add_workout("Tuesday", 400, 0, 20, "Shoulders", 650)

print("Workout Log :")
for w in workouts:
    print(w)