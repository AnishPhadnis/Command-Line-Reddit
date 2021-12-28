from config import *


def showUserProfile(userDict, username):
	userProfile = userDict[username]

	print('')

	print('Profile of ' + username)
	print('-------------------')
	print('')

	print('Karma:', userProfile[userKarmaKey])
	print('Authored', len(userProfile[userPostsKey]), 'posts.')
	print('')

	for i in range(len(userProfile[userPostsKey]) - 1, -1, -1):
		print('Title:', userProfile[userPostsKey][i][postTitle])
		print('Points', userProfile[userPostsKey][i][postPoints], ' ', 'Comments', len(userProfile[userPostsKey][i][postComments]))
		print('')
		# Aware that this doesn't read true number of comments, but like Reddit only counts direct comments
	print('\n')

	print('Comments: ')
	for i in userProfile[userCommentsKey]:
		print('Title of Post: ', i[userCommentsPostIndex][postTitle])
		print('Commented ', i[userCommentsIndex])
		print('')

	print('')

def searchForUser(userDict):
	print('\n')
	userToSearchFor = input('Enter the username of the profile you want to view: ')

	while userToSearchFor not in userDict:
		print('No such user exists... ')

		userToSearchFor = input('Enter the username of the profile you want to view: ')

	return userToSearchFor


def viewUserProfiles(userDict):
	userToSearchFor = searchForUser(userDict)
	showUserProfile(userDict, userToSearchFor)



