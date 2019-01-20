from countwordsFunctions import * 

counts = countWords("mobypara.txt")

printTop20(counts)
stops = readStopWords("stopwords.txt")

counts2 = countWords2("mobypara.txt", stops)

print(similarity(counts, counts))
print(similarity(counts, counts2))