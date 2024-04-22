cont = True

#commands
def check(input):
    if input == "hey": print("hey")
    elif input == "end": cont = False

#runs the code
while cont:
    ci = input("-")
    check(ci);