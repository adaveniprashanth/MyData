import configparser

#we have to run this file to create configuration file
# CREATE OBJECT
config_file = configparser.ConfigParser()
config_file.add_section("FILESettings")
config_file.set("FILESettings","input_filename","WW_40_43_1.xlsx")
config_file.set("FILESettings","consolidated_filename","consollidated_bill.xlsx")
config_file.set("FILESettings","jira_submission_filename","jira_submission.xlsx")

# SAVE CONFIG FILE
with open(r"configurations1.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
config=configparser.ConfigParser()
config.read("configurations.ini")
input_file= config["FILESettings"]["input_filename"]
consolidated_file=config["FILESettings"]["consolidated_filename"]
jira_submission_file = config["FILESettings"]["jira_submission_filename"]

print(input_file,consolidated_file,jira_submission_file)
'''
# ADD NEW SECTION AND SETTINGS
config_file["Logger"]={
        "LogFilePath":"<Path to log file>",
        "LogFileName" : "<Name of log file>",
        "LogLevel" : "Info"
        }
'''