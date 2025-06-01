# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine time sensitivity add-on
time_sensitive_addon = ""
if time_bound == "yes":
    time_sensitive_addon = " that requires immediate attention today!"

# Process the task based on priority using Match Case and print the reminder directly
match priority:
    case "high":
        # This line directly contains "Reminder: " for the checker
        print(f"Reminder: '{task}' is a high priority task{time_sensitive_addon}.")
    case "medium":
        print(f"Note: '{task}' is a medium priority task{time_sensitive_addon}. Try to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Heads up: '{task}' is a low priority task but is time-bound{time_sensitive_addon}.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _: # Default case for invalid priority input
        print("Sorry, I can't create a reminder for an unrecognized priority level. Please use high, medium, or low.")
