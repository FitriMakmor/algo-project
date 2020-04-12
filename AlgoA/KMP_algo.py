def check_words(s, w):
    if f' {w} ' == f' {s} ':
        return 1
    else:
        return 0


def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0] * m
    j = 0  # index for pat[]
    i = 0  # index for txt[]

    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            print(pat + " is found at index " + str(i - j))
            j = lps[j - 1]

        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def PN_wordsort(article, result):
    list1 = article.read().split()
    Pcounter = 0

    result.write("\nPositive words: \n")
    for a in list2:
        for b in list1:
            if a == b:
                result.write(a + ", ")
                Pcounter += 1
    result.write("\nTotal Positive Words: " + str(Pcounter) + "\n")

    result.write("\nNegative words: \n")
    Ncounter = 0
    for a in list3:
        for b in list1:
            if a == b:
                result.write(a + ", ")
                Ncounter += 1
    result.write("\nTotal Negative Words: " + str(Ncounter) + "\n")

    result.close()
    article.close()


article = ["CleanedTotalThai.txt", "CleanedTotalKorea.txt", "CleanedTotalChina.txt", "CleanedTotalJapan.txt",
           "CleanedTotalHK.txt", "CleanedTotalJakarta.txt", "CleanedTotalTaiwan.txt"]
result = ["Thailand.txt", "SouthKorea.txt", "China.txt", "Japan.txt", "Hong Kong.txt", "Indonesia.txt", "Taiwan.txt"]
PList = open("PosWords.txt", 'r')
NList = open("NegWords.txt", 'r')
list2 = PList.read().split()
list3 = NList.read().split()
f = 0
q = 0

print("\nPattern searching: \n")
for i in range(len(article)):
    file = article[i]
    print("\n\nSearching for words in " + article[i] + "\n\n")
    with open(file, 'r') as readFile:
        list1 = readFile.read()
    print("\nPattern of positive words: \n")
    for j in range(len(list2)):
        KMPSearch(list2[j], list1)
        j = j + 1
    print("\nPattern for negative words: \n")
    for k in range(len(list3)):
        KMPSearch(list3[k], list1)
        k = k + 1
    i += 1

print("\nAll pattern searching - completed\n")

for f in range(len(article)):
    file_List = article[f]
    result_list = result[f]
    readFile = open(file_List, 'r')
    with open(result_list, 'a') as createResult:
        print("\n\nSorting positive and negative words in files: \n" + result[f])
        PN_wordsort(readFile, createResult)
        f += 1
    readFile.close()
    createResult.close()

print("All words sorting - finished")
