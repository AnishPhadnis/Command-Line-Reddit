from config import *
import userProfile
import os

user = ''


def showPostContent(post):
	print('-------')

	print(post[postTitle]) # Title
	print('')

	print(post[postTime]) # Time
	print('Author:', post[postAuthor]) # Author
	print('Points:', post[postPoints]) # Points

	print('\n')

	print(post[postContent])

	print('\n')

	print('-------')
	print('')


def viewAllPosts(postList):
	print('-------')

	enumeratedPosts = {}

	for num, post in enumerate(postList):
		enumeratedPosts[num + 1] = post

		print(str(num + 1) + '. ' + post[0])
		print(len(post[postComments]), 'comments ', post[postPoints], 'points')
		print('')

	print('')	
	print('-------')

	return enumeratedPosts


def getPostNumberToView(enumeratedPosts):
	while True:
		postNum = input('What post number would you like to view? ')

		if postNum.isnumeric() and int(postNum) in enumeratedPosts:
			return int(postNum)
		else:
			print("That post number is out of bounds. Please input a valid post number. ")
			print('')


def viewFeed(postList):
	enumeratedPosts = viewAllPosts(postList)
	return enumeratedPosts, getPostNumberToView(enumeratedPosts)

def getDictKeys(dic):
	return list(dic.keys())

def getDictValues(dic):
	return list(dic.values())

def nestedCommentColourGenerator():
	os.system("color")

	colours = ['\u001b[31;1m', '\u001b[32;1m', '\u001b[33;1m', '\u001b[36;1m', '\u001b[37;1m']
	i = -1	

	while True:
		for i in range(len(colours)):
			yield colours[i]


def showPostCommentsHelper(comments, enumeratedComments, spaces = 0, commentNum = 1, colourGen = nestedCommentColourGenerator()):
	# Prints out all comments showing relationship (is a comment a reply to another comment?)
	# Returns value of highest comment number
	# Returns reference to each comment to easily access and reply to specific comments
	
	reset = '\u001b[0m'
	tabs = '---' * spaces

	# Recursive base case
	if len(comments) == 2:
		if authorOfCommentKey in comments and pointsOfCommentKey in comments:
			return commentNum, enumeratedComments

	textColour = next(colourGen)
	highestLevelComments = getDictKeys(comments) 

	# Keys of comments{} will be the highest level of comments - will be replying directly to post and not replies to other comments
	for comment in highestLevelComments:
		# Don't want to print author, num points of comment
		if comment == authorOfCommentKey or comment == pointsOfCommentKey: continue 

		# Plain version to play it safe cross platform
		# Print comment with points
		print(str(commentNum).zfill(2) + tabs + '|>' + ' ' + comment + '\t| (Points ' + str(comments[comment][pointsOfCommentKey]) + ')')
		
		# Alternative Comment Print Out Approach
		#print(str(commentNum).zfill(2) + tabs + '|>' + ' ' + comments[comment][authorOfCommentKey] + '\t| (Points ' + str(comments[comment][pointsOfCommentKey]) + ')')
		#print('  ' + (' ' * len(tabs)) + '  ' + ' ' + comment)
		#print('')

		#COLOURED COMMENTS VERSION - Works on windows, may not work on mac - Looks 100x better though
		#print(textColour + str(commentNum).zfill(2) + tabs + '|>' + ' ' + comment + '\t| (Points ' + str(comments[comment][pointsOfCommentKey]) + ')' + reset)

		# Store comment hierarchy - which comment it's a reply to/which comments are replying to it
		enumeratedComments[commentNum] = comments[comment]

		# Recursive Case - go into comments of this comment
		commentNum, enumeratedComments = showPostCommentsHelper(comments[comment], enumeratedComments, spaces + 1, commentNum + 1) # Iterate one level deeper to read direct replies of this comment

		# Only direct comments to the post will have a new line after them
		if tabs == '': 
			print('')

	return commentNum, enumeratedComments


def showPostComments(post):
	print('Press any key to see comments. ')
	input()

	print(str(commentOnPostNumber).zfill(2) + '. Comment on post.')
	print('')

	commentNum, enumeratedComments = showPostCommentsHelper(post[postComments], {0 : post[postComments]})
	return commentNum - 1, enumeratedComments
	# Necessary step since commentNum is initialized at 1

def getUserChoiceVoteOrReply():
	while True:
		print('')
		print('V - To Vote on a comment/post. ')
		print('R - To Reply to a post or to another comment. ')

		upvoteOrComment = input('Enter your choice: ').strip().lower()

		if upvoteOrComment == 'v' or upvoteOrComment == 'r':
			return upvoteOrComment

		print('Please only enter expected input... ')


def getUserChoiceVote():
	while True:
		print('')
		upvoteOrDownvoteChoice = input('Press U to upvote or D to downvote: ').strip().lower()

		if upvoteOrDownvoteChoice == 'u' or upvoteOrDownvoteChoice == 'd':
			break
		print('Sorry invalid entry...')

	if upvoteOrDownvoteChoice == 'u':
		pointsToAdd = defaultUpvotePointsPerVote

	elif upvoteOrDownvoteChoice == 'd':
		pointsToAdd = defaultDownvotePointsPerVote

	return pointsToAdd


def commentLocation(post):
	if len(post[postComments]) > 0:
		while True:
			userChoice = input('On a post or a comment (press P or C): ').strip().lower()

			if userChoice == 'p' or userChoice == 'c':
				return userChoice
			
			print('Please enter p or c. ')
			print('')

	return 'p'


def userActionsOnPost(post, userDict):
	toContinue = ''

	while toContinue != 'q':
		showPostContent(post)
		totalCommentNum, enumeratedComments = showPostComments(post) # All info needed to do any supported user action in regards to comments
		
		voteOrComment = getUserChoiceVoteOrReply()

		if voteOrComment == 'v':

			commentNum = getCommentNumToActOn(totalCommentNum)
			pointsToAdd = getUserChoiceVote()

			if commentNum == commentOnPostNumber:
				voteOnPost(post, userDict, pointsToAdd)

			else:
				voteOnComment(enumeratedComments[commentNum], userDict, user, pointsToAdd)

		elif voteOrComment == 'r':
			commentNum = getCommentNumToActOn(totalCommentNum)
			commentText = commentOnPost(enumeratedComments[commentNum], userDict, user)
			addCommentToProfile(userDict, post, commentText)


		toContinue = input('Do you want to continue? Press any key to continue or press "q" to quit: ')


def voteOnPost(post, userDict, pointsToAdd):
	post[postPoints] += pointsToAdd
	updateUserKarma(userDict, user, pointsToAdd)


def commentOnPost(comment, userDict, user): # NEED TO ADD USER # ADD COMMENT NUM
	commentText = input('Enter your comment: ')

	# Point on Comment
	comment[commentText] = {'$USER' : user, '$POINTS' : defaultPointsPerComment}
	updateUserKarma(userDict, user, 1)

	return commentText


def addCommentToProfile(userDict, post, comment):
	userDict[user][userCommentsKey].append([[post][postTitle], comment])


def voteOnComment(comment, userDict, user, pointsToAdd):
	comment[pointsOfCommentKey] += pointsToAdd
	updateUserKarma(userDict, user, pointsToAdd)


def updateUserKarma(userDict, user, karmaPoints):
	userDict[user][userKarmaKey] += karmaPoints


def getCommentNumToActOn(totalNumComments):
	if totalNumComments == 0:
		return 0

	print('')
	print('Enter the number of where you want to act on.')
	print('If you comment,', commentOnPostNumber, ', you will act directly in response to the post.')
	print('Any other number will act on the comment at that number. ')
	print('')

	commentNum = input('Enter the comment number: ')

	while not isValidCommentNum(commentNum, totalNumComments):
		print('That is not a valid choice...')
		print('Choose something from', commentOnPostNumber, 'to', totalNumComments)
		print('')

		commentNum = input('Enter the comment number: ')

	print('')
	return int(commentNum)


def isValidCommentNum(commentNum, totalComments):
	if commentNum.isnumeric():
		if commentOnPostNumber <= int(commentNum) <= totalComments:
			return True

	return False


def main(postList, userDict, username):
	global user
	user = username

	enumeratedPosts, postToView = viewFeed(postList)
	userActionsOnPost(enumeratedPosts[postToView], userDict)


comments = {'comm':{'comm2':{'comm3':{'comm4':{'$USER' : 'cat', '$POINTS' : 1}, '$USER' : 'matt', '$POINTS' : 1}, '$USER' : 'bob', '$POINTS' : 1}, '$USER' : 'anish', '$POINTS' : 1}, 'comm5':{'$USER' : 'kat', '$POINTS' : 1}, 'comm6':{'comm7':{'comm8':{'$USER' : 'david', '$POINTS' : 1}, '$USER' : 'mat', '$POINTS' : 1}, '$USER' : 'nat', '$POINTS' : 1}}


postHistoryList = [['bye', 'hi', '16:20 on 10/31/20', 1, comments, 'anish'], ['hi', 'nope', '16:20 on 10/31/20', 1, {}, 'bob']]
userInfo = {'bob': {'$POSTS': [postHistoryList[1], postHistoryList[0]], '$KARMA': 1, '$COMMENTS': []}}






