logins = [{'name': 'karthik', 'password': '12345'}, {'name': 'karthik', 'password': '12345'}]


def adminloginverfication(name, password):
    for ind in logins:
        if name == ind.get('name'):
            if password == ind.get('password'):
                return True
            else:
                return 'Password is Incorrect ๐'

    return 'Account Not Found ๐'


def adminRegister(name, password, reqid):
    if reqid == '2002':
        for ind in logins:
            if name == ind.get('name'):
                return "โ ๏ธAccount is already available"
        logins.append({'name': name, 'password': password})
        return True
    else:
        return "Hospital ID is Incorrect ๐"

