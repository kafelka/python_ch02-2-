#task 1
#Counting words - reads through a file and counts the words into a dictionary

def countWords(filename):
    counts = {}
    textfile = open(filename, "r") #r stands for read
    for line in textfile:
        words = line.split() #return substrings as a list
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

#print(countWords("mobydick.txt"))


#task 2 sorting and ranking
#function that is given a disctionary of counts and print out the 20 words with 
#the highest frequencies, in descending order
#
#counts = countWords("mobydick.txt")
#
#def printTop20(counts):
#    words = list(counts.keys())
#    
#    words.sort(reverse=True, key=lambda v:counts[v])
#    print(words[0])
#    for i in range(20):
#        word = words[i]   #words = words[:20]
#        print("word:", word.upper(), "has a frequency of:", counts[word])
#printTop20(counts)


#task3 stopwords
# function that reads in the words and return them as a list of strings
   
def readStopWords(stopfile):
    stops = []
    with open(stopfile, "r") as textfile:
        for line in textfile:
            word = line.strip()
            stops.append(word)
        return stops
  
#stops = readStopWords("stopwords.txt")
#print(stops)

def countWords2(filename, stopwords): 
    counts = {}
    with open(filename, "r") as textfile:
        for line in textfile:
            wordsInLine = line.split() #return substrings as a list
            for word in wordsInLine:
                if word not in stopwords:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1       
    #    print(counts)
        return counts

#countWords2("mobydick.txt", stops)

#task 4  
stops = readStopWords("stopwords.txt")
       
georgeFiles = ["george01.txt", "george02.txt", "george03.txt", "george04.txt"]
georgeDicts = [countWords(element) for element in georgeFiles]

#georgeDicts2 = [] #same as georgeDicts:
#for element in georgeFiles:
#    wordCountDict = countWords(element)
#    georgeDicts2.append(wordCountDict)
    
georgeDicts3 = [countWords2(element, stops) for element in georgeFiles]   
#w1 = {"karo": 3, "kier": 4, "trefl": 5}
#w2 = {"karo": 5, "pik": 8, "trefl": 10, "canasta": 300}
def similarity(words1, words2):
    if len(words1) + len(words2) == 0:
        return 0
    overlap = 0
    for key in words1.keys():
        if key in words2:
            overlap += 1
            
    return overlap / (len(words1) + len(words2) - overlap)


import itertools

print("Scores without stop words")
for pair in itertools.combinations([0,1,2,3], r=2):
    p1, p2 = pair
    score = similarity(georgeDicts3[p1], georgeDicts3[p2])
    print(f"Score for george0{p1+1}, george0{p2+1}: {score}") 
  
print("Scores using all words")    
for pair in itertools.combinations([0,1,2,3], r=2):
    p1, p2 = pair
    print(f"Score for george0{p1+1}, george0{p2+1}: {similarity(georgeDicts[p1], georgeDicts[p2])}") 

    
#print(similarity(georgeDicts3[0], georgeDicts3[3])) 

#task4 
#input: file1counts, file2counts
#def similarity():
#    size/len of the counts1, counts2
#    
#    if size1 + size2 > 0: #avoid a divide by zero error
#        overlap = 0
#        
#        functionalitty: 
#            loop through words in counts1:
#                if w in counts2:
#                    overlap value updated.
#        return float(overlap) / (size1 + size2 - overlap)
#    
#    else:
#        return 0.0