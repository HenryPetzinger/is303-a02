'''
Henry Petzinger
IS 303 - A02


Fiteness Advisor
This program recommends an exercise plan based on fitness level and goals


Inputs:
- Name (string)
- Fitness level (beginner, intermediate, advanced) (string)
- Fitness goal (weight loss, strength, endurance) (string)


Processes:
- Validate fitness level (must be beginner, intermediate, or advanced)
- Validate fitness goal (must be weight loss, strength, or endurance)
- If beignner, recommend light workout, then adjust based on goal
- If intermediate, recommend moderate workout, then adjust based on goal
- If Advanced, recommend intense workout, then adjust based on goal


Outputs:
- Print: Personalized exercise recommendation using user's name
- Print: Error message if fitness level or goal is invalid

'''

# Get user inputs for name, fitness level, and fitness goal
name = input("Enter your name: ")
fitness_level = input("Enter your fitness level (beginner/intermediate/advanced) ").lower()
fitness_goal = input("Enter your fitness goal (weight loss, strength, endurance) ").lower()


#Validating inputs to make sure they are the expected valuees. If not, print an error message.
if fitness_level != "beginner" and fitness_level != "intermediate" and fitness_level != "advanced":
    print("Error. Fitness level must be beginner, intermediate, or advanced. Please try again.")
elif fitness_goal != "weight loss" and fitness_goal != "strength" and fitness_goal != "endurance":
    print("Error. Fitness goal must be weight loss, strength, or endurance. Please try again.")

#Validate beginner fitness level and recommend workout based on goal.
else:
    if fitness_level == "beginner":
        if fitness_goal == "weight loss":
            print(f"{name} we recommend 30 minutes of daily walking and light cardio")
        elif fitness_goal == "strength":
            print(f"{name} we recommend 3 days/week of bodyweight exercises.")
        elif fitness_goal == "endurance":
            print(f"{name} we recommend light jogging 3 days/week.")

#Validate intermediate fitness level and recommend workout based on goal.
    elif fitness_level == "intermediate":
        if fitness_goal == "weight loss":
            print(f"{name} we recommend 45 min cardio 4 days/week.")
        elif fitness_goal == "strength":
            print(f"{name} we recommend: weight training 4 days/week.")
        elif fitness_goal == "endurance":
            print(f"{name} we recommend: running 4 days/week, increasing distance weekly.")

    #Validate advanced fitness level and recommend workout based on goal.
    elif fitness_level == "advanced":
        if fitness_goal == "weight loss":
            print(f"{name} we recommend: high-intensity interval training (HIIT) 5 days/week.")
        elif fitness_goal == "strength":
            print(f"{name} we recommend: weight training 5 days/week, focusing on progressive overload.")
        elif fitness_goal == "endurance":
            print(f"{name} we recommend: long-distance running or cycling 5 days/week, increasing distance weekly.")






