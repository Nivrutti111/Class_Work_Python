# List of email addresses (som duplicates)
email_addresses = [
    "user1@example.com", "user2@example.com", "user3@example.com",
     "user1@example.com", "user4@example.com", "user2@example.com"

]

# Use a set to remove duplicates
unique_emails = set(email_addresses)

# Convert the set back to a sorted list if needed
unique_emails_list = sorted(unique_emails)

print(unique_emails_list)
# Output the unique email addresses
print("Unique email addresses:")
for email in unique_emails_list :
    print(email)

#Now add more three emails(some reperated from set1) in another set
#and print only email which are present in first set

additional_emails={"sang12@gmail.com","ram@gmail.com","user1@example.com","user2@example.com"}

Emails_in_firstSet-unique_emails-addition_emails
print("The set difference is", Emails_in_firstSet)
