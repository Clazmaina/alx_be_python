def get_user_input():
    task = input("Enter your task:")
    priority = input("Priority(high/medium/low):")
    time_bound = input("Is it time-bound?(yes/no):")
    return task, priority, time_bound
if __name__ == "__main__":
        task, priority, time_bound = get_user_input()
        match priority:
              case "high":
                    urgency = "high priority task."
              case "medium":
                    urgency = "medium priority task."
              case "low":
                    urgency = "low priority task."
              case _:
                    urgency = "invalid priority. Please use 'high', 'medium', or 'low'."
                    
        if time_bound == "yes":
              urgency+=" that requires immediate attention today!"
        if time_bound == "no":
              urgency+=" Consider completing it when you have free time."
        
        print("\nTask:", task)
        print("Priority:", priority)
        print("Time Bound:", time_bound)
        reminder = f"Reminder:'{task}' is a {urgency}"
        print(reminder)