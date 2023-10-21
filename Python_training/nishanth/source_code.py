try:
    import sys
    import requests,sqlite3,configparser
except ModuleNotFoundError as e:
    print(e)
    print("you have to install the module to run effectively")
    print("You can install by using pip module. pip install <module_name>")
    sys.exit(" Please install the module")

# Read token value from config file
config=configparser.ConfigParser()
config.read('config.ini')
token=config['Credentials']['token']

# Function to run SQL queries
def run_queries_from_file(filename, table_name):
    l = []
    with open(filename, 'r') as file:
        for line in file: l.append(line.strip())
    all_commands = "".join(l).replace("data_table", table_name)
    cursor.executescript(all_commands)
if 1:
    database_name="result.db"
    table_name = "data_table"
    # creating the database and cursor
    database = sqlite3.connect(database_name)
    cursor =database.cursor()

    # colleting data from API
    if 1:
        # creating the table in database
        run_queries_from_file('design_schema.sql',table_name)

        # colecting start and end date
        start_date=input('Enter the start date. Format YYYY-MM-DD\n')
        end_date = input('Enter the end date. Format YYYY-MM-DD\n')

        # Define the API endpoint
        url = "https://api.libring.com/v2/reporting/get"
        # Set the headers
        headers = {"Authorization": f"Token {token}"}
        # Define the query parameters
        params = {
            "allow_mock": "true",
            "period": "custom_date",
            "start_date": start_date,  # Replace with your start date
            "end_date": end_date,    # Replace with your end date
            "group_by": "connection,app,platform,country",
            "lock_on_collection": "false"
        }
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # The API response is stored in 'response.json()'
            api_data = response.json()
            # print(api_data)
            # f=open('result.txt','w') # For storing the retrieved data in normal text file
            for i in api_data['connections']:
                print(i)
                sql_query = f"INSERT INTO {table_name} ({', '.join(i.keys())}) VALUES ({', '.join(['?' for _ in i])})"
                cursor.execute(sql_query,tuple(i.values()))
                # f.writelines(str(i)+"\n")
            # f.close()
            database.commit()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    if 0: #printing the custom data
        cursor.execute(f"SELECT * FROM {table_name} GROUP BY connection;")
        column_names=[i[0] for i in cursor.description]
        print(column_names)
        for i in cursor:
            print(i)

    cursor.close()
    database.close()

