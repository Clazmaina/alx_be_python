def get_user_input():
    task = input("Enter task description:")
    priority = input("Enter task priority(high, medium, low):")
    time_bound = input("Is the task time-bound?(yes/no):")
    return task, priority, time_bound
if __name__ == "__main__":
        task, priority, time_bound = get_user_input()
        match priority:
              case "high":
                    urgency = "High priority"
              case "medium":
                    urgency = "Medium priority"
              case "low":
                    urgency = "Low priority"
              case _:
                    urgency = "Invalid priority. Please use 'high', 'medium', or 'low'."
                    
        if time_bound == "yes":
              urgency+=" that requires immediate attention today!"
        
        print("\nTask Description:", task)
        print("Priority:", priority)
        print("Time-Bound:", time_bound)
        print("Reminder:", urgency)
        reminder = f"Reminder: {task} {urgency}"
        print(reminder)