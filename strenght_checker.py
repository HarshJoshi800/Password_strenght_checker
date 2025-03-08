import re
input_password = input("Type your password to check its strenght :")

lenght = len(input_password)

upper_case = re.search(r"[A-Z]", input_password)
lower_case= re.search(r"[a-z]", input_password)
digit= re.search(r"[0-9]", input_password)
special_characters= re.search(r"[@$!%*?&]", input_password)

if lenght and upper_case and lower_case and digit and special_characters:
    print("its is a Strong password")
else:
    print("it is not a strong password")