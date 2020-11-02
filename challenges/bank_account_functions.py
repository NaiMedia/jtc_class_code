def create_account():
	balance = float(0) 
	username = input('please enter your username: ')
	password = input('please enter your password: ')

	new_account = {'username': username, 'password': password,'balance': balance}
	return new_account

def deposit(account, amount):
	account['balance'] = account['balance'] + amount


	
