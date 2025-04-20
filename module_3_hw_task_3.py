import re

def normalize_phone(phone_number):
    clean_number = re.sub(r'\D', '', phone_number) # delete all symbols except digits
    # check and correct phone number format
    if clean_number.startswith('38'):
        clean_number = '+' + clean_number
    else:
        clean_number = '+38' + clean_number
    return clean_number

raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS services:\n", sanitized_numbers)