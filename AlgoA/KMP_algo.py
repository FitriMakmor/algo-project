def KMPSearch(pat, txt):
    pat = " " + pat + " "
    txt = " " + txt + " "
    m = len(pat)
    n = len(txt)

    lps = [0] * m
    j = 0  # index for pat[]
    i = 0  # index for txt[]

    while i < n:  # checking first index of pat and length as both starter from 0
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:  # if length of pattern and j is the same, pattern found
            print(pat + " is found at index " + str(i - j))
            createResult.write(pat + ",")
            j = lps[j - 1]

        elif i < n and pat[j] != txt[i]:  # if match not found
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def count_word(article, result):
    list1 = article.read().split()
    Pcounter = 0

    # counter for positive words in file
    for a in list2:
        for b in list1:
            if a == b:
                Pcounter += 1
    result.write("\nTotal Positive Words: " + str(Pcounter) + "\n")

    # counter for negative words in file
    Ncounter = 0
    for a in list3:
        for b in list1:
            if a == b:
                Ncounter += 1
    result.write("\nTotal Negative Words: " + str(Ncounter) + "\n")
    result.write("\n")
    result.write("________________________________________________________________\n")
    result.write("\n")


article = ["CleanedTotalThai.txt", "CleanedTotalKorea.txt", "CleanedTotalChina.txt", "CleanedTotalJapan.txt",
           "CleanedTotalHK.txt", "CleanedTotalJakarta.txt", "CleanedTotalTaiwan.txt"]
result = ["Thailand.txt", "SouthKorea.txt", "China.txt", "Japan.txt", "Hong Kong.txt", "Indonesia.txt", "Taiwan.txt"]
PList = open("PosWords.txt", 'r')
NList = open("NegWords.txt", 'r')
list2 = PList.read().split()
list3 = NList.read().split()
f = 0
q = 0

for f in range(len(article)):
    file_List = article[f]
    result_list = result[f]
    readFile = open(file_List, 'r')
    with open(result_list, 'a') as createResult:
        print("\nCounting positive and negative words in files: \n" + result[f])
        count_word(readFile, createResult)
        f += 1
    readFile.close()
    createResult.close()

print("\nAll words counting - finished")

# pattern searching for positive and negative words in articles using KMP algorithm
print("\nPattern searching:")
for i in range(len(article)):
    file = article[i]
    result_list = result[i]
    with open(result_list, 'a') as createResult:
        print("\nSearching for words in " + article[i] + "\n")
        with open(file, 'r') as readFile:
            list1 = readFile.read()
        print("\nPattern of positive words: \n")
        createResult.write("\nPositive words found in articles: \n")
        createResult.write("\n")

        for j in range(len(list2)):
            KMPSearch(list2[j], list1)
            j = j + 1

        createResult.write("\n\n")
        print("\nPattern for negative words: \n")
        createResult.write("\nNegative words found in articles: \n")
        createResult.write("\n")
        for k in range(len(list3)):
            KMPSearch(list3[k], list1)
            k = k + 1
        i += 1

print("\nAll pattern searching - completed\n")
