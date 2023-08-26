import re

def phone_number(text):
    phone_number_regex = re.compile(r"^\(?\d{3}\)?(?:-|\s)\d{3}(?:\-|\s)\d{4}$")

    def remove_prefix(text):
        return re.sub(r"^My phone number is ", "", text)

    text = remove_prefix(text)
    match = phone_number_regex.search(text)
    if match:
        return match.group()
    else:
        return None


text = "My phone number is (123)-456-7890"
phone_number = phone_number(text)
print(phone_number)
