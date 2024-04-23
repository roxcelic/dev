import os

config_Content = {
    "version": "0.0.02",
    "build_num": "1"
}

whats_New = {
    0 : "initial creation",
    1 : "plugins are now installable"
}

version_Content = {
    "0.0.01": ["0"],
    "0.0.02": ["1"]
}

current_version = "0.0.01"

filename = 'main.config'

def whatsnew(item):
    print("-"*5, "whats new", "-"*5)
    for key, value in whats_New.items():
        if key <= int(item):
            print(f"{value}")

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