task = input("Enter your task: ")
priority = input("Priority (high/medium/low): "). lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""
time_sensitive_addon = ""

# Determine time sensitivity add-on
if time_bound == "yes":
    time_sensitive_addon = " that requires immediate attention today!"

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task{time_sensitive_addon}."
    case "medium":
        reminder_message = f"Note: '{task}' is a medium priority task{time_sensitive_addon}. Try to complete it soon."
    case "low":
        if time_bound == "yes":
            # If a low priority task is surprisingly time-bound, still give it attention
            reminder_message = f"Heads up: '{task}' is a low priority task but is time-bound{time_sensitive_addon}."
        else:
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _: # Default case for invalid priority input
        reminder_message = "Sorry, I can't create a reminder for an unrecognized priority level. Please use high, medium, or low."

# Provide a customized reminder
print(reminder_message)