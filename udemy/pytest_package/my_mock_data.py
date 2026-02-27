
mock_database={
    1:"ram",
    2:"raj",
    3:"kalyan"
}

def get_user_from_id(id):
    return mock_database.get(id,'None')