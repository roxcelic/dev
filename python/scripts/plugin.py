import urllib.request
import os

folder_name = 'plugins/'
folder_path = os.path.join(os.getcwd(), folder_name)

file_paths = []

plugin_paths = []

if os.path.isfile("pluginloc.config"):
    with open('pluginloc.config', 'r') as file:
        plugin_paths = [line.strip() for line in file]

if os.path.isfile("plugin.config"):
    with open('plugin.config', 'r') as file:
        file_paths = [line.strip() for line in file]

def install_plugins(url):
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
        print("after deleting a plugin you may have to restart your client for it to update the help menu")
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