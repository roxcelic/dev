import os

#gets the save folder from local app data
local_app_data_path = os.getenv('LOCALAPPDATA')
folder_name = 'YourAppName'
full_path = os.path.join(local_app_data_path, folder_name)
if not os.path.exists(full_path):
    os.makedirs(full_path)
full_path = full_path + "/"

config_Content = {
    "version": "0.0.13",
    "build_num": "7",
}

whats_New = {
    0 : "initial creation",
    1 : "plugins are now installable",
    2 : "the script cleans itself up after finishing",
    3 : "support for multiple plugins",
    4 : "plugins are now deletable and are stored locally",
    5 : "command list is now dynamically updated (but can still be improved)",
    6 : "download concent can now be skipped",
    7 : "concent improvement"
}

version_Content = {
    "0.0.01": ["0"],
    "0.0.02": ["1"],
    "0.0.03": ["2"],
    "0.0.04": ["3"],
    "0.0.10": ["4"],
    "0.0.11": ["5"],
    "0.0.12": ["6","0"],
    "0.0.13": ["7"]
}

current_version = "0.0.13"

filename = 'main.config'
filename = full_path + filename

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
        if content[1:][0] == version_Content[ver][0]:
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