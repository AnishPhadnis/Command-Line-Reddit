from datetime import datetime
from config import *

def getTime():
	time = datetime.now()
	return time.strftime(timeDateFormat) # Format time - (global variable?)

def writePost():
	title = input('Post Title: ')

	print('Write your post here: ')
	text = input('')

	return title.strip(), text.strip()

def createPost(userProfile, postList, user):
	# Get all the attributes of a post that we want to save
	title, text = writePost()
	time = getTime()
	defaultPoints = 1
	comments = {}

	# This is the compiled list of all post information
	postInfo = [title, text, time, defaultPoints, comments, user]

	# Save it in the post history in stack fashion (most recent first)
	postList.append(postInfo)

	# Save this information in the user's account information
	userProfile[user][userPostsKey].append(postInfo)






"""

postHistoryList = [['bye', 'hi', '16:20 on 10/31/20', 1, {'comm':{'comm2':'comm3'}, 'comm4':{}, 'comm5':{'comm6':'comm7'}}, 'anish'], ['hi', 'nope', '16:20 on 10/31/20', 1, {}, 'bob']]
#postHistoryDict = {}
user = 'bob'
userInfo = {'bob': {'hi': [['hi', 'nope', '16:20 on 10/31/20', 1, {}, 'bob']]}, 'anish': {'bye': [['bye', 'hi', '16:20 on 10/31/20', 1, {}, 'anish']]}}
"""

#createPost(userInfo, postHistoryList, user, postHistoryDict)





