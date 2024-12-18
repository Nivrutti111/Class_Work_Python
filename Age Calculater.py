from datetime import datetime

def time_lived_and_days_left(birthdate_str):
    # Convert birthdate string to datetime object
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    
    # Get today's date
    today = datetime.today()
    
    # Calculate the difference between today's date and the birthdate
    delta = today - birthdate
    
    # Get the number of days
    total_days = delta.days
    
    # Calculate years, months, and days
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30
    
    # Calculate next birthday date
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)
    
    # If the next birthday has already passed this year, set the next birthday to the next year
    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)
    
    # Calculate days left for the next birthday
    days_left = (next_birthday - today).days
    
    # Display the results
    print(f"You have lived for {years} years, {months} months, and {days} days.")
    print(f"Days left for your next birthday: {days_left} days.")

# Get the birthdate from the user
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

# Call the function
time_lived_and_days_left(birthdate_input)
