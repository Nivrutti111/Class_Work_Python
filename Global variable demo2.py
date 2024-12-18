system_status = "offline"

def start_system():
    global system_status  #Access the global variable
    system_status = "online"
    print("System started.")

def stop_system():
    global system_status  #Access the global variable
    system_status = "offline"
    print("System stopped.")

def check_system_status():
    #Access the global variable without modification
    print(f"The system is currently: {system_status}")


# Using the global variable
check_system_status()  # Output: The system is currently: offline
start_system()         # Output: System started.
check_system_status()  # Output: The system is currently: online
stop_system()          # Output: System Stoped.
check_system_status()  # Output: TThe system is currently: offline
