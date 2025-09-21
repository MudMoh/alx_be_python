# This script reminds the user about a single task based on its priority and time sensitivity.

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a match case statement to customize the message based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task that is time-bound.")
        else:
            print(f"Note: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that is time-bound.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered.")
