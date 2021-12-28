from config import *

def validateLoginDetailsHelper(username, password, loginDetails):
	return username in loginDetails and loginDetails[username] == password

def validateLoginDetails(loginDetails):
	username = input('Enter your username: ').strip()
	password = input('Enter your password: ').strip()

	while not validateLoginDetailsHelper(username, password, loginDetails):
		print('Incorrect! ')
		print('')

		# Extension: Would you like to quit?
		# In case the user accidently pressed create account instead of sign in

		username = input('Enter your username: ')
		password = input('Enter your password: ')

	print('Welcome ' + username + '!')
	print('')

	return username

def loginToAccount(loginDetails, userDict):

	while True:
		print('C - To Create A New Account ')
		print('S - To Sign Into Your Account ')

		userChoice = input('')

		if userChoice.lower().strip() == 'c':
			user = addNewUser(loginDetails, userDict)
			return user

		elif userChoice.lower().strip() == 's':
			user = validateLoginDetails(loginDetails)
			return user

		print('Not a valid option! ')


def logout():
	print('Thank you for using the program! ')
	print('')

def addNewUser(loginDetails, userDict):
	username = input('Please input a username: ')

	while username in loginDetails:
		print('That username is taken...')
		username = input('Please input a username: ')

	password = input('Please input a password: ')

	while not passwordStrength(password):
		password = input('Please input a password: ')

	loginDetails[username] = password
	userDict[username] = {userPostsKey: [], userKarmaKey: defaultNewAccountKarma, userCommentsKey:[]}

	print('Welcome ' + username + '!')

	return username


def passwordStrength(password):
	goodPassword = True

	if len(password) < 8:
		print('Please input a password that is at least 8 characters long! ')
		goodPassword = False

	if password.lower() == password:
		print('Please input a password that has at least 1 uppercase letter. ')
		goodPassword = False

	if password.upper() == password:
		print('Please input a password that has at least 1 lowercase letter. ')
		goodPassword = False

	numsInPassword = [x.isnumeric() for x in password]

	if not any(numsInPassword):
		print('Please include at least 1 number. ')
		goodPassword = False

	if not checkAnySpecialCharacters(password):
		goodPassword = False

	print('')

	return goodPassword


def checkAnySpecialCharacters(password):
	specialChars = '!@#$%^&*()-+'

	for i in password:
		if i in specialChars:
			return True

	print('Please include special characters. ')
	print('Currently we support: ' + specialChars)

	print('')

	return False


#loginDetailDatabase = loadLoginDetails('loginDetails.txt')
#validateLoginDetails(loginDetailDatabase)
#addNewUser(loginDetailDatabase)
#saveLoginDetails('loginDetails.txt', loginDetailDatabase)
