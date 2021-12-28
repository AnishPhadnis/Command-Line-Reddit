from config import *

"""userKarmaKey = '$KARMA'

userPostsKey = '$POSTS'
userPostsValPostIndex = 0

userCommentsKey = '$COMMENTS'
userCommentsPostIndex = 0
userCommentsIndex = 1

# subredditPostOrganization = ['Post Title', 'Post Content', 'Time', 'Points', 'Comments', 'Author']

# Index of each information point
postTitle = 0
postContent = 1
postTime = 2
postPoints = 3
postComments = 4
postAuthor = 5"""

"""# Duplicated in viewFeed.py

comments = {'comm':{'comm2':{'comm3':{'comm4':{'$USER' : 'cat'}, '$USER' : 'matt'}, '$USER' : 'bob'}, '$USER' : 'anish'}, 'comm5':{'$USER' : 'kat'}, 'comm6':{'comm7':{'comm8':{'$USER' : 'david'}, '$USER' : 'mat'}, '$USER' : 'nat'}}
postHistory = [['bye', 'hi', '16:20 on 10/31/20', 1, comments, 'bob'], ['hi', 'nope', '16:20 on 10/31/20', 1, {}, 'bob']]
userInfo = {'bob': {'$POSTS': [postHistory[1], postHistory[0]], '$KARMA': 1, '$COMMENTS': [[postHistory[0], 'comment'], [postHistory[1], 'comment']]}}
"""

def showUserProfile(userDict, user):
	userProfile = userDict[user]

	print('')

	print('Profile of ' + user)
	print('-------------------')
	print('')

	print('Karma:', userProfile[userKarmaKey])
	print('Authored ', len(userProfile[userPostsKey]), 'posts.')
	print('')

	for i in range(len(userProfile[userPostsKey]) - 1, -1, -1):
		print('Title:', userProfile[userPostsKey][i][postTitle])
		print('Points', userProfile[userPostsKey][i][postPoints], ' ', 'Comments', len(userProfile[userPostsKey][i][postComments]))
		print('')
		# Aware that this doesn't read true number of comments, but like Reddit only counts direct comments
	print('\n')

	print('Comments: ')
	for i in userProfile[userCommentsKey]:
		print(i[userCommentsPostIndex][postTitle])
		print(i[userCommentsIndex])
		print('')

	print('')

def searchForUser(userDict):
	print('\n')
	userToSearchFor = input('Enter the username of the profile you want to view: ')

	while userToSearchFor not in userDict:
		print('No such user exists... ')

		userToSearchFor = input('Enter the username of the profile you want to view: ')

	return userToSearchFor


def viewUserProfiles(userDict, user):
	userToSearchFor = searchForUser(userDict)
	showUserProfile(userDict, user)



#print(userInfo['bob'][userCommentsKey][1][userCommentsIndex])
#viewUserProfile(userInfo, 'bob')


