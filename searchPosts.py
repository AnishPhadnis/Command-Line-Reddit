# Search by most comments
# Most points
# 	- For both of these, give option to sort from highest/least as well as search for specific num of comments
# Time
# 	- Create lower time bound to upper time bound and print everything in between

from config import *
import viewFeed

"""comments = {'comm':{'comm2':{'comm3':{'comm4':{'$USER' : 'cat', '$POINTS' : 1}, '$USER' : 'matt', '$POINTS' : 1}, '$USER' : 'bob', '$POINTS' : 1}, '$USER' : 'anish', '$POINTS' : 1}, 'comm5':{'$USER' : 'kat', '$POINTS' : 1}, 'comm6':{'comm7':{'comm8':{'$USER' : 'david', '$POINTS' : 1}, '$USER' : 'mat', '$POINTS' : 1}, '$USER' : 'nat', '$POINTS' : 1}}

postHistory = [['bye', 'hi', '20:20 on 10/28/20', 5, comments, 'anish'], ['hi', 'nope', '16:20 on 10/30/20', 1, {}, 'bob']]
userInfo = {'bob': {'$POSTS': [postHistory[1], postHistory[0]], '$KARMA': 1, '$COMMENTS': []}}
"""


def searchByPointsMethod():
	while True:
		print('')
		print('1 - Sort posts from greatest to least points. ')
		print('2 - Sort posts from least to greatest points. ')
		print('3 - Search posts with a specific number of points. ')

		userChoice = input('')

		if userChoice == '1' or userChoice == '2' or userChoice == '3':
			return int(userChoice)

		print('Please choose 1, 2, 3. ')

def getRangeOfPointsToFilter():
	print('')
	print('Enter the range of points you want to filter posts by. ') 
	print('If you want to see only posts with 4 points, simply put 4 for both the lowest and highest bound. ')

	while True:
		print('')
		lowBound = input('Enter the lowest number of points you want to see posts with: ')
		highBound = input('Enter the highest number of points you want to see posts with: ')

		# Repeated code in return statement but in this case I think having clear separation of the cases is needed
		if lowBound.isdigit() and highBound.isdigit() and int(lowBound) <= int(highBound):
			return int(lowBound), int(highBound)
		elif isNegativeNum(lowBound) and isNegativeNum(lowBound) and int(lowBound) <= int(highBound):
			return int(lowBound), int(highBound)
		elif isNegativeNum(lowBound) and int(lowBound) <= int(highBound):
			return int(lowBound), int(highBound)
		else:
			print('Invalid... ')

def isNegativeNum(string):
	return string[1:].isnumeric()


def printRangeOfPosts(sortedPosts, startingPosition, endingPosition):
	# Formatting posts needs work
	if startingPosition == -1 and endingPosition == -1:
		print('Error no such posts...')
	elif startingPosition > (len(sortedPosts) - 1): 
		print('Error no such posts...') # Repeated for the sake of clarity between 2 edge cases
	elif startingPosition == endingPosition:
		viewFeed.showPostContent(sortedPosts[startingPosition])
		#print(sortedPosts[startingPosition]) 
	else:
		for i in sortedPosts[startingPosition:endingPosition + 1]:
			viewFeed.showPostContent(i)
		#print(sortedPosts[startingPosition:endingPosition + 1])



def searchByPoints(postHist):
	postHistory = [x[:] for x in postHist]

	userChoice = searchByPointsMethod()

	sortedPosts = mergeSort(postHistory, postPoints)

	if userChoice == 1 or userChoice == 2:
		if userChoice == 1:
			sortedPosts.reverse()
		
		printRangeOfPosts(sortedPosts, 0, len(sortedPosts) - 1)

	elif userChoice == 3:
		lowBound, highBound = getRangeOfPointsToFilter()


		startingPosition = findStart(sortedPosts, lowBound, postPoints)
		endingPosition = findEnd(sortedPosts, highBound, postPoints)

		printRangeOfPosts(sortedPosts, startingPosition, endingPosition)

		

def findStart(alist, value, indexToSearchAt):
    if alist == []: return -1

    left = 0
    right = len(alist)

    while True:
        mid = (left + right) // 2


        if alist[mid][indexToSearchAt] == value:
            if mid == 0:
                return mid
            elif alist[mid - 1][indexToSearchAt] == value:
                right = mid - 1
            else:
                return mid
        elif alist[mid][indexToSearchAt] > value:
            right = mid - 1
        elif alist[mid][indexToSearchAt] < value:
            left = mid + 1

        if len(alist[left:right + 1]) < 1: return left


def findEnd(alist, value, indexToSearchAt):
    if alist == []: return -1

    left = 0
    right = len(alist)

    while True:
        mid = (left + right) // 2

        if alist[mid][indexToSearchAt] == value:
            if mid == len(alist) - 1:
                return mid
            elif alist[mid + 1][indexToSearchAt] == value:
                left = mid + 1
            else: 
                return mid
        elif alist[mid][indexToSearchAt] > value:
            right = mid - 1
        elif alist[mid][indexToSearchAt] < value:
            left = mid + 1

        if len(alist[left:right + 1]) < 1: return right


# Extension
# Have not implemented methods to search by methods other than point
def searchingMethod():
	while True:	
		print('')

		print('C - To view posts by the number of COMMENTS. ')
		print('P - To view posts by the number of POINTS. ')
		print('T - To view posts by the TIME they were posted. ')
		
		print('')

		choice = input('Enter your choice: ').strip().lower()

		if choice == 'c' or choice == 'p' or choice == 't':
			return choice


def binarySearch(alist, targetNum):
    left = 0
    right = len(alist)
    
    while left <= right:
        middle = (left + right) // 2  
        
        if alist[middle] == targetNum:
            return middle
            
        elif alist[middle] < targetNum:
            left = middle + 1
            
        elif alist[middle] > targetNum:
            right = middle - 1
            
    return -1
            
def mergeSort(alist, indexToSortBy):
    if len(alist) > 1: 
        middle = len(alist) // 2
        
        a = mergeSort(alist[:middle], indexToSortBy)
        b = mergeSort(alist[middle:], indexToSortBy)
        
        return mergeList(a, b, indexToSortBy)
    return alist  
          
            
def mergeList(a, b, indexToSortBy):
    merged = []
    
    if a == []: return b
    if b == []: return a
    
    while True:
        if a == []:
            merged.extend(b)
            break
        elif b == []:
            merged.extend(a)
            break
        else:
            if a[0][indexToSortBy] <= b[0][indexToSortBy]:
                merged.append(a[0])
                a.pop(0)
            elif a[0][indexToSortBy] > b[0][indexToSortBy]:
                merged.append(b[0])
                b.pop(0)
    return merged

"""postHistory = [['bye', 'hi', '20:20 on 10/28/20', 5, {}, 'anish'], ['hi', 'nope', '16:20 on 10/30/20', 1, {}, 'bob']]

searchByPoints(postHistory)"""