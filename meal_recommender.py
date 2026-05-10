'''
Henry Petzinger
IS 303 - A02

Meal Recommender
This program suggests a meal based on time of day, dietary preference, and budget.

Inputs:
- Time of day: breakfast, lunch, or dinner (string)
- Dietary preference: vegetarian, vegan, or none (string)
- Budget: low, medium, or high (string)

Processes:
- Validate time of day (must be breakfast, lunch, or dinner)
- Validate dietary preference (must be vegetarian, vegan, or none)
- Validate budget (must be low, medium, or high)
- If breakfast: recommend a morning meal adjusted by dietary preference and budget
- If lunch: recommend a midday meal adjusted by dietary preference and budget
- If dinner: recommend an evening meal adjusted by dietary preference and budget

Outputs:
- Print personalized meal recommendation using f-string
- Print error message if any input is invalid
'''

# Get user inputs
time_of_day = input("Enter time of day (breakfast/lunch/dinner): ").lower()
dietary_preference = input("Enter dietary preference (vegetarian/vegan/none): ").lower()
budget = input("Enter your budget (low/medium/high): ").lower()

# Validate inputs
if time_of_day != "breakfast" and time_of_day != "lunch" and time_of_day != "dinner":
    print("Error: time of day must be breakfast, lunch, or dinner.")
elif dietary_preference != "vegetarian" and dietary_preference != "vegan" and dietary_preference != "none":
    print("Error: dietary preference must be vegetarian, vegan, or none.")
elif budget != "low" and budget != "medium" and budget != "high":
    print("Error: budget must be low, medium, or high.")

else:
    if time_of_day == "breakfast":
        if dietary_preference == "vegetarian":
            if budget == "low":
                print(f"We recommend: oatmeal with fruit.")
            elif budget == "medium":
                print(f"We recommend: veggie omelette with toast.")
            elif budget == "high":
                print(f"We recommend: avocado eggs benedict.")
        elif dietary_preference == "vegan":
            if budget == "low":
                print(f"We recommend: peanut butter toast with banana.")
            elif budget == "medium":
                print(f"We recommend: smoothie bowl with granola.")
            elif budget == "high":
                print(f"We recommend: tofu scramble with avocado toast.")
        elif dietary_preference == "none":
            if budget == "low":
                print(f"We recommend: bacon and eggs.")
            elif budget == "medium":
                print(f"We recommend: breakfast burrito with sausage.")
            elif budget == "high":
                print(f"We recommend: steak and eggs.")

    elif time_of_day == "lunch":
        if dietary_preference == "vegetarian":
            if budget == "low":
                print(f"We recommend: grilled cheese sandwich.")
            elif budget == "medium":
                print(f"We recommend: veggie burger with fries.")
            elif budget == "high":
                print(f"We recommend: caprese panini with tomato soup.")
        elif dietary_preference == "vegan":
            if budget == "low":
                print(f"We recommend: hummus and veggie wrap.")
            elif budget == "medium":
                print(f"We recommend: quinoa salad with chickpeas.")
            elif budget == "high":
                print(f"We recommend: vegan sushi bowl with edamame.")
        elif dietary_preference == "none":
            if budget == "low":
                print(f"We recommend: turkey sandwich with chips.")
            elif budget == "medium":
                print(f"We recommend: chicken caesar salad.")
            elif budget == "high":
                print(f"We recommend: salmon poke bowl.")

    elif time_of_day == "dinner":
        if dietary_preference == "vegetarian":
            if budget == "low":
                print(f"We recommend: pasta with marinara sauce.")
            elif budget == "medium":
                print(f"We recommend: eggplant parmesan.")
            elif budget == "high":
                print(f"We recommend: mushroom risotto.")
        elif dietary_preference == "vegan":
            if budget == "low":
                print(f"We recommend: stir-fried tofu with rice.")
            elif budget == "medium":
                print(f"We recommend: vegan curry with naan.")
            elif budget == "high":
                print(f"We recommend: vegan butternut squash ravioli.")
        elif dietary_preference == "none":
            if budget == "low":
                print(f"We recommend: grilled chicken with vegetables.")
            elif budget == "medium":
                print(f"We recommend: salmon with roasted potatoes.")
            elif budget == "high":
                print(f"We recommend: ribeye steak with mashed potatoes.")