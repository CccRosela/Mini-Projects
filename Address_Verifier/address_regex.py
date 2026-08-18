import re

email = input("What's your email address?: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|org|net|edu|at)$", email, re.IGNORECASE):
    print("Valid!")
else:
    print("Invalid!")

#### Process steps: ####
# re.search(r".+@.+\.com", email):
# . -> if any character left or right of the address
# + -> 1 or more repetitions
# \ -> escape character, `\.` lets the `.` be recognised as part of the string

# re.search(r"^.+@.+\.com$", email):
# Entering a sentence would give us valid, so we restrict the input:
# ^  -> matches the start of the string
# $  -> matches the end of the string or just before the newline at the end of the string

# re.search(r"^[^@]+@[^@]+\.com$", email):
# User can add as many @ as they want and code is still valid:
# replace `.` with `[^@] -> any character except @`
# []    set of characters
# [^]   complementing the set

# re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
# an email address cannot contain that many special characters, so we can customize further:
# [a-zA-Z0-9_] -> characters must be between a and z, between A and Z, between 0 and 9 and potentially include an _ symbol

# re.search(r"^\w+@\w+\.(com|gov|org|net|at)$", email, re.IGNORECASE):
# [a-zA-Z0-9_] = \w
# (A|B) -> either A or B -> | = or expression
# (...)   a group
# (?:...) non-capturing version
# re.IGNORECASE (e.g COM and com -> case sensitivity)

# re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|org|net|edu|at)$", email, re.IGNORECASE):
# ?  -> 0 or 1 repetition
# (\w+\.)? -> this expression can be there once, or not at all, covers cases like: rosic23@univie.ac.at
