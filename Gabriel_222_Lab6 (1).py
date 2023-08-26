import re

def is_strong_password(password):

  if len(password) < 8:
    return False

  if not re.search("[A-Z]", password):
    return False

  if not re.search("[a-z]", password):
    return False

  if not re.search("[0-9]", password):
    return False

  if not re.search("[!@#$%^&*()_+-]", password):
    return False

  return True


password = "Christ@123"

if is_strong_password(password):
  print("The password is strong.")
else:
  print("The password is not strong.")
