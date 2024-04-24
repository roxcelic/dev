import os

config_Content = {
    "version": "0.0.11",
    "build_num": "5"
}

whats_New = {
    0 : "initial creation",
    1 : "plugins are now installable",
    2 : "the script cleans itself up after finishing",
    3 : "support for multiple plugins",
    4 : "plugins are now deletable and are stored locally",
    5 : "command list is now dynamically updated (but can still be improved)"
}

version_Content = {
    "0.0.01": ["0"],
    "0.0.02": ["1"],
    "0.0.03": ["2"],
    "0.0.04": ["3"],
    "0.0.10": ["4"],
    "0.0.11": ["5"]
}

current_version = "0.0.11"

filename = 'main.config'

def whatsnew(item):
    print("-"*5, "whats new", "-"*5)
    for key, value in whats_New.items():
        if key >= int(item):
            print(whats_New[key])

def write():
    with open(filename, 'w') as file:
        write = ""
        for key,value in config_Content.items():
            write = write + str(value) + "\n"
        file.write(write)

def config_check(conts):
    content = conts
    ver = content[0]
    if ver in version_Content:
        if content[1:] == version_Content[ver]:
            return True
        else: return False
    else: return False

if os.path.isfile(filename):
    cont = open(filename, "r")
    conts = cont.readlines()
    x = 0
    for item in conts:
        conts[x] = conts[x].replace("\n","")
        x = x+1
    cont.close()
    if (config_check(conts)):
        if conts[0] != current_version:
            whatsnew(conts[1])
            write()
    else:
        print("invalid config file, resetting...")
        write()
        whatsnew(config_Content["build_num"])
else:
    write()
    whatsnew(config_Content["build_num"])