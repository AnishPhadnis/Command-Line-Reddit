from config import *
import loginValidation
import saveData
import searchPosts
import viewProfiles
import viewFeed
import writePost

loginDetails = {}
userProfiles = {}
subredditHistory = []

def welcomeUser():
	print('Welcome to Reddit! ')
	print('')

def loadAllData():
	global loginDetails
	global subredditHistory
	global userProfiles

	loginDetails = saveData.readSavedData(loginDetailsFile)
	subredditHistory = saveData.readSavedData(subredditHistoryFile)
	userProfiles = saveData.readSavedData(userProfilesFile)
	

def saveAllData():
	global loginDetails
	global subredditHistory
	global userProfiles

	saveData.saveData(loginDetailsFile, loginDetails)
	saveData.saveData(subredditHistoryFile, subredditHistory)
	saveData.saveData(userProfilesFile, userProfiles)


	loginDetails.clear()
	subredditHistory.clear()
	userProfiles.clear()

def toContinue():
	print('')
	toContinue = input('Press any key to continue. Press q to quit. ').strip().lower()

	if toContinue == 'q':
		return False
	return True

def inputMenuOption():
	while True:
		print('')
		print('V - To View your feed')
		print('P - To look at user Profiles')
		print('W - To Write a post')
		print('S - To Search for posts')

		userChoice = input('Enter you choice: ').strip().lower()

		if userChoice == 'v' or userChoice == 'p' or userChoice == 'w' or userChoice == 's':
			return userChoice

		print('Please input one of the accepted inputs. ')
		print('')

def confirmLogout():
	print('')
	print('Would you like to logout? ')
	userChoice = input('Press any key to continue, press q to logout. ').strip().lower()

	return userChoice == 'q'



def main():
	while True:
		welcomeUser()
		loadAllData()

		user = loginValidation.loginToAccount(loginDetails, userProfiles)

		while True:
			userChoice = inputMenuOption()

			if userChoice == 'v':
				viewFeed.main(subredditHistory, userProfiles, user)
			elif userChoice == 'p':
				viewProfiles.viewUserProfiles(userProfiles)
			elif userChoice == 'w':
				writePost.createPost(userProfiles, subredditHistory, user)
			elif userChoice == 's':
				searchPosts.searchByPoints(subredditHistory)

			if confirmLogout(): break

		loginValidation.logout()

		# If user does not currently logout, the data is not saved
		saveAllData()
		


main()

