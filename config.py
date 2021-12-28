# subredditPostOrganization = ['Post Title', 'Post Content', 'Time', 'Points', 'Comments', 'Author']

# Index of each information point in subreddit History
postTitle = 0
postContent = 1
postTime = 2
postPoints = 3
postComments = 4
postAuthor = 5

# User Profile Dict keys
userKarmaKey = '$KARMA'

userPostsKey = '$POSTS'
#userPostsValPostIndex = 0

# How comments are stored in user profiles
userCommentsKey = '$COMMENTS'
userCommentsPostIndex = 0
userCommentsIndex = 1

# Comments Dictionary Keys
authorOfCommentKey = '$USER'
pointsOfCommentKey = '$POINTS'

# How much karma each user gets per comment on default 
defaultPointsPerComment = 1

defaultUpvotePointsPerVote = 1
defaultDownvotePointsPerVote = -1

# Data Storage Files
loginDetailsFile = 'loginDetails.txt'
userProfilesFile = 'userProfiles.txt'
subredditHistoryFile = 'subredditHistory.txt'


# Comment # To Reference If User Is Commenting on Post
commentOnPostNumber = 0

# Karma a new user starts off with
defaultNewAccountKarma = 1

# Time Date Format For Recording when a post was written
timeDateFormat = '%H:%M on %D'





