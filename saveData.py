import json

def saveData(filename, dataToSave):
	f = open(filename, 'w')
	data = json.dumps(dataToSave)

	f.write(data)
	f.close()


def readSavedData(filename):
	f = open(filename, 'r')
	data = json.load(f)
	f.close()

	return data


	
"""
comments = {'comm':{'comm2':{'comm3':{'comm4':{'$USER' : 'cat', '$POINTS' : 1}, '$USER' : 'matt', '$POINTS' : 1}, '$USER' : 'bob', '$POINTS' : 1}, '$USER' : 'anish', '$POINTS' : 1}, 'comm5':{'$USER' : 'kat', '$POINTS' : 1}, 'comm6':{'comm7':{'comm8':{'$USER' : 'david', '$POINTS' : 1}, '$USER' : 'mat', '$POINTS' : 1}, '$USER' : 'nat', '$POINTS' : 1}}

postHistory = [['bye', 'hi', '16:20 on 10/31/20', 1, comments, 'anish'], ['hi', 'nope', '16:20 on 10/31/20', 1, {}, 'bob']]
userInfo = {'bob': {'$POSTS': [postHistory[1], postHistory[0]], '$KARMA': 1, '$COMMENTS': []}}

loginDetailsDatabase = {'anish':'comp1405', 'danish':'Cu1ed!!!', 'lanish':'comp1405!C'}

saveData('userProfiles.txt', userInfo)
saveData('subredditHistory.txt', postHistory)
"""
#saveData('test.txt', [userInfo, postHistoryList])
#readSavedData('test.txt')