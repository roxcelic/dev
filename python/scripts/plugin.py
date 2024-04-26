import urllib.request
import os
import requests

#gets the save folder from local app data
local_app_data_path = os.getenv('LOCALAPPDATA')
folder_name = 'YourAppName'
full_path = os.path.join(local_app_data_path, folder_name)
if not os.path.exists(full_path):
    os.makedirs(full_path)
full_path = full_path + "/"

folder_name = 'plugins/'
folder_path = full_path + folder_name

file_paths = []

plugin_paths = []

if os.path.isfile("pluginloc.config"):
    with open('pluginloc.config', 'r') as file:
        plugin_paths = [line.strip() for line in file]

if os.path.isfile("plugin.config"):
    with open('plugin.config', 'r') as file:
        file_paths = [line.strip() for line in file]

def check_url_exists(url):
    if url[:8] == "https://" or url[:7] == "http://":
        try:
            response = requests.head(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False
    else:
        return False

def install_plugins(url):
    if (check_url_exists(url)):
        global plugin_paths, file_paths
        if url not in plugin_paths:
            plugin_paths.append(url)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_name = url[8:].replace("/", ".")
            file_name = folder_path + file_name
            urllib.request.urlretrieve(url, file_name)
            file_name = file_name.replace(os.getcwd(), "").replace("\\", "")
            file_paths.append(file_name)
            with open('pluginloc.config', 'w') as file:
                for item in plugin_paths:
                    file.write(f"{item}\n")
            with open('plugin.config', 'w') as file:
                for item in file_paths:
                    file.write(f"{item}\n")
    else:
        print("the link returned nothing")

def delete_plugins(local_ci):
    if local_ci in plugin_paths:
        plugin_paths.remove(local_ci)
        file_paths.remove(folder_name + local_ci[8:].replace("/", "."))
        with open('pluginloc.config', 'w') as file:
            for item in plugin_paths:
                file.write(f"{item}\n")
        with open('plugin.config', 'w') as file:
            for item in file_paths:
                file.write(f"{item}\n")
        os.remove(folder_name + local_ci[8:].replace("/", "."))
    else:
        print("sorry that plugin wasnt found")

print("type 'delete' if you would like to delete a plugin or 'update' if you would like to update all of your plugins")
ci = input("link- ")

if ci == "delete":
    print("pick the file you would like to delete")
    for item in plugin_paths:
        print(item)
    local_ci = input("-")
    delete_plugins(local_ci)

elif ci == "update":
    for item in plugin_paths:
        delete_plugins(item)
        install_plugins(item)

else:
    install_plugins(ci)
