str_manip=input("Please enter a sentence:")
length=len(str_manip)
print(len(str_manip))
last_letter = str_manip.strip()[-1]
new_str = str_manip.replace(last_letter, '@')
print("Modified sentence:", new_str)
last_three_reversed = str_manip[-3:][::-1]
print("Last 3 characters in reverse:", last_three_reversed)
new_word = str_manip[:3] + str_manip[-2:]
print("New 5-letter word:", new_word)