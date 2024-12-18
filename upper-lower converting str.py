#String related methods

strmsg="helLoWorld!!!"

#converting data to lowercase

new_msg=strmsg.lower()

print("The lower case string is:",new_msg)

#converting data to upper case

upp_msg=strmsg.upper()
print("The upper case tring is:",upp_msg)

# removing spaces from beginning and at the end

name="        Nivrutti         "
final_name=name.strip()
print("The final input is",final_name)

#removing left space  and right space
lspace=name.lstrip()
print("The left space removed",lspace)

rspace=name.rstrip()
print("The right space removed",rspace)

#str.replace(old, new): This method replaces all occurrences of the "old" substring
#with the "new" substring in the string.

sentence = "I like apples, and I like pineapple."
new_sentence = sentence.replace("like", "love")
print(new_sentence)
# "I love apples, and I love pineapple."



