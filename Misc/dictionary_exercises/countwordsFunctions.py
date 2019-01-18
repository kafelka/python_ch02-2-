#task 1
#Counting words - reads through a file and counts the words into a dictionary

def countWords(filename):
    counts = {}
    textfile = open(filename, "r")
    for line in textfile:
        words = line.split() #return substrings as a list
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

#print(countWords("mobydick.txt"))

#alternatively:
#            if word not in stops:
#                if word in counts:
#                    counts[word] += 1
#                else:
#                    counts[word] = 1       
#    return counts
    

#task 2 sorting and ranking
#function that is given a disctionary of counts and print out the 20 words with 
#the highest frequencies, in descending order

counts = countWords("mobydick.txt")

def printTop20(counts):
    words = list(counts.keys())
    words.sort(reverse=True, key=lambda v:counts[v])
    for i in range(20):
        word = words[i]   #words = words[:20]
        print("word:", word.upper(), "has a frequency of:", counts[word])
        
printTop20(counts)


#task3 stopwords






#    
#def readStopWord(stopfile):
#    stops = []
#    inf = open(stopfile, "r")
#    for line in inf:
#        word = line.strip()
#        stops.append(word)
#    return stops
#  