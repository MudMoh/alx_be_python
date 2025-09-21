# This script reminds the user about a single task based on its priority and time sensitivity.

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = f"Note: '{task}' is a {priority} priority task."

# Use a match case statement to customize the message based on priority
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder_message = f"Note: '{task}' is a medium priority task."
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task."
    case _:
        # Handles any priority input that is not high, medium, or low
        reminder_message = f"Note: '{task}' has an unspecified priority."

# Use an if statement to modify the message if the task is time-bound
if time_bound == "yes":
    if priority == "high":
        reminder_message += " that requires immediate attention today!"
    else:
        reminder_message += " and is time-bound."
elif time_bound == "no" and priority == "low":
    reminder_message += " Consider completing it when you have free time."

# Print the final reminder
print(reminder_message)
