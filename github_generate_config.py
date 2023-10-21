import configparser

#we have to run this file to create configuration file
# CREATE OBJECT
config_file = configparser.ConfigParser()
config_file.add_section("GITHUBSettings")
config_file.set("GITHUBSettings","initialization","1")
config_file.set("GITHUBSettings","clone","1")


# SAVE CONFIG FILE
with open(r"github_configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'github_configurations.ini' created")

# PRINT FILE CONTENT
config=configparser.ConfigParser()
config.read("github_configurations.ini")
initialization= config["GITHUBSettings"]["initialization"]
clone=config["GITHUBSettings"]["clone"]


print(initialization,clone)
'''
# ADD NEW SECTION AND SETTINGS
config_file["Logger"]={
        "LogFilePath":"<Path to log file>",
        "LogFileName" : "<Name of log file>",
        "LogLevel" : "Info"
        }
'''