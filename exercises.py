import math

def fac(value):
	result=1
	for x in range(1, value+1):
		result=result*x
	print(result)

def fib(value):
	list=[0, 1]
	for x in range(2, value):
		list.insert(x, list[x-1]+list[x-2])
	print(list[value-1])

def bmi(kg, cm):
	height=cm/100
	result=kg/(height*height)
	message=""
	if result<18.5:
		message="you are underweight"
	if result>=18.5 and result<=25:
		message="you are at a healthy weight"
	if result>25:
		message="you are overweight"
	print(result)
	print(message)

def countLetters(string):
	result=[]
	dup=[]
	n=0
	for x in (string):
		n=n+1
		count=1
		if x not in (dup) and x is not " ":
			dup.insert(len(dup), x)
			for y in range(n, len(string)):
				if string[y]==x:
					count=count+1
			result.insert(len(result), {x: count})
	print(result)

def countLetters2(string):
	result=[]
	letters=[]
	for x in (string):
		new=True
		for y in range(0, len(letters)):
			if letters[y]==x:
				result[y][x]=result[y][x]+1
				new=False
		if new==True and x is not " ":
			result.insert(len(result), {x: 1})
			letters.insert(len(letters), x)
	print(result)

def countWords(string):
	newString=string.lower()
	newList=newString.split(" ")
	result=[]
	words=[]
	for x in (newList):
		new=True
		for y in range(0, len(words)):
			if words[y]==x:
				result[y][x]=result[y][x]+1
				new=False
		if new==True:
			result.insert(len(result), {x: 1})
			words.insert(len(words), x)
	print(result)

def capitalise(newString):
	string=newString.lower()
	result=""
	for x in range(0, len(string)):
		if string[x-1] is " " or x is 0:
			result=result+string[x].upper()
		else:
			result=result+string[x]
	print(result)

def palindrome(string):
	newList=string.split(" ")
	pals=[]
	for word in newList:
		original=word
		word=word.lower()
		result=True
		for x in range(0, math.ceil(len(word)/2)):
			if word[x] is not word[len(word)-1-x]:
				result=False
		if result is True:
			pals.insert(len(pals), original)
	print(pals)

def shortLong(string):
	tempList=string.split(" ")
	newList=[]
	longest=[]
	shortest=[]
	for word in tempList:
		newWord=""
		for letter in word:
			if letter is not "." and letter is not ",":
				newWord=newWord+letter
		newList.insert(len(newList), newWord)
	longest.insert(0, newList[0])
	shortest.insert(0, newList[0])
	for word in newList:
		if len(word)>len(longest[0]):
			longest=[]
			longest.insert(0, word)
			continue
		if len(word) is len(longest[0]) and word not in longest:
			longest.insert(len(longest), word)
			continue
		if len(word)<len(shortest[0]):
			shortest=[]
			shortest.insert(0, word)
			continue
		if len(word) is len(shortest[0]) and word not in shortest:
			shortest.insert(len(shortest), word)
			continue
	print("Shortest: ", shortest)
	print("Longest: ", longest)

def jumble(string):
	newList=string.split(" ")
	sentence=""
	for word in newList:
		pureWord=""
		newWord=""
		punc=""
		if "." in word or "," in word:
			for x in range(0, len(word)-1):
				pureWord=pureWord+word[x]
			punc=word[len(word)-1]
		else:
			pureWord=word
		if len(pureWord)%2 is not 0:
			cap=False
			if pureWord[0].isupper and len(pureWord)>1:
				cap=True
			for x in range(0, len(pureWord)):
				letter=pureWord[len(pureWord)-1-x]
				if x is 0 and cap is True:
					letter=letter.upper()
				if x is len(pureWord)-1 and cap is True:
					letter=letter.lower()
				newWord=newWord+letter
		else:
			newWord=pureWord
		sentence=sentence+newWord+punc+" "
	print(sentence)

fac(5)
fib(5)
bmi(79, 180)
countLetters("aaaa bbb cc d")
countLetters2("aaaa bbb cc d")
countWords("Joseph is a joseph is me")
capitalise("happy vAlentine'S day J-oseph")
palindrome("abc abb AbA aaA aBcde abCbA Bb")
shortLong("I love you very much, JOSEPH.")
jumble("I love You very MucH, JoSeph.")