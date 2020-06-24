import re

zip_code = input()

valid = re.search(r"^\d{5}$",zip_code ) is not None

if valid:
    print("true")
else:
    print("false")