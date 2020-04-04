PList = open("PosWords.txt", 'r')
NList = open("NegWords.txt", 'r')
article = open("cleaned_thai5.txt", 'r')
result = open("Thailand.txt", 'a')

PCounter = 0
NCounter = 0

list1 = PList.read().split()
list2 = NList.read().split()
list3 = article.read().split()

result.write("\n")
result.write("\n[Positive]: \n")
for i in list3:
    for j in list1:
        if i == j:
            PCounter += 1
            result.write(i + " ")

result.write("\nTotal Positive words: " + str(PCounter))
result.write("\n")

result.write("\n[Negative]: \n")
listWords = []
for i in list2:
    for j in list3:
        if i == j:
            NCounter += 1
            result.write(i + " ")

result.write("\nTotal Negative words: " + str(NCounter))
result.write("\n")

PList.close()
NList.close()
article.close()
result.close()
