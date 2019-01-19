#task 1
#Counting words - reads through a file and counts the words into a dictionary

#def countWords(filename):
#    counts = {}
#    textfile = open(filename, "r") #r stands for read
#    for line in textfile:
#        words = line.split() #return substrings as a list
#        for word in words:
#            if word in counts:
#                counts[word] += 1
#            else:
#                counts[word] = 1
#    return counts

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
    textfile = open(stopfile, "r")
    for line in textfile:
        word = line.strip()
        stops.append(word)
    return stops
  
stops = readStopWords("stopwords.txt")
#print(stops)

def countWords2(filename, stopwords):
    
    counts = {}
    textfile = open(filename, "r")
    for line in textfile:
        wordsInLine = line.split() #return substrings as a list
        for word in wordsInLine:
            if word not in stops:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1       
    print(counts)
    return counts

countWords2("mobydick.txt", stops)

    


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