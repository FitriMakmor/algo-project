import dash
import dash_core_components as dcc
import dash_html_components as html

#variables
d = 256
q = 101 # A prime number
input = ["TotalChina.txt","TotalHK.txt","TotalJakarta.txt","TotalJapan.txt","TotalKorea.txt","TotalTaiwan.txt","TotalThai.txt"]
cleaned = ["CleanedTotalChina.txt","CleanedTotalHK.txt","CleanedTotalJakarta.txt","CleanedTotalJapan.txt","CleanedTotalKorea.txt","CleanedTotalTaiwan.txt","CleanedTotalThai.txt"]
country = ["China","Hong Kong","Jakarta","Japan","Korea","Taiwan","Thailand"]
result = ["China.txt", "Hong Kong.txt", "Indonesia.txt", "Japan.txt", "SouthKorea.txt", "Taiwan.txt", "Thailand.txt"]
#assigning values of 0 to the int arrays as the value will change later.
numbers = [0,0,0,0,0,0,0] #total words before clean
totalnumber = [0, 0, 0, 0, 0, 0, 0] #totalwords after clean
stopwords = [0,0,0,0,0,0,0]
economic = [0.99,0,0,0,0,0,0,0]
PList = open("PosWords.txt", 'r')
NList = open("NegWords.txt", 'r')
Pcount = [0, 0, 0, 0, 0, 0, 0]
Ncount = [0, 0, 0, 0, 0, 0, 0]
list2 = PList.read().split()
list3 = NList.read().split()

def KMPSearch(pat, txt):

    pat = " " + pat + " "
    txt = " " + txt + " "
    m = len(pat)
    n = len(txt)

    lps = [0] * m
    j = 0  # index for pat[]
    i = 0  # index for txt[]
    computeLPSArray(pat, m, lps)

    while i < n:  # checking first index of pat and length as both starter from 0
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:  # if length of pattern and j is the same, pattern found
            print(pat + " is found at index " + str(i - j))
            j = lps[j - 1]

        elif i < n and pat[j] != txt[i]:  # if match not found
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
def storeposneg(a1,a2): #txt,result
    print("\n######################  COUNT/STORING POSITIVE & NEGATIVE WORDS IN TXT.FILE #################################\n")
    article = a1
    result = a2
    file1 = open("countpos.txt", "w")
    file2 = open("countneg.txt", "w")
    for f in range(len(article)):
        file_List = article[f]
        result_list = result[f]
        readFile = open(file_List, 'r')
        list1 = readFile.read().split()
        with open(result_list, 'w+') as createResult:
            print("\nCounting positive and negative words in file: " + result[f] + "\n")
            #uncomment the .write to append changes to text file
            createResult.write("\n[Positive]: \n")
            Pcounter = 0
            for a in list2:
                for b in list1:
                    if a == b:
                        createResult.write(a + ", ")
                        Pcounter += 1
            Pcount[f] = Pcounter
            createResult.write("\n")
            createResult.write("\nTotal Positive Words: " + str(Pcounter) + "\n")

            # append mode
            file1.writelines(str(Pcounter))
            file1.writelines("\n")


            createResult.write("______________________\n")

            # counter for negative words in file
            Ncounter = 0
            createResult.write("\n[Negative]: \n")
            for a in list3:
                for b in list1:
                    if a == b:
                        createResult.write(a + ", ")
                        Ncounter += 1
            Ncount[f] = Ncounter
            # uncomment the commands to append changes to text file
            createResult.write("\n")
            createResult.write("\nTotal Negative Words: " + str(Ncounter) + "\n")
              # append mode
            file2.writelines(str(Ncounter))
            file2.writelines("\n")


            print("Total Positive words: ", Pcount[f])
            print("Total Negative words: ", Ncount[f])

            f += 1
        readFile.close()
        createResult.close()
    file1.close()
    file2.close()
    print("\nAll words counting - finished")
    print("\n######################  COUNT/STORING POSITIVE & NEGATIVE WORDS IN TXT.FILE - END #################################\n")
def posnegwordspattern(b1):
    print("\n######################   POSITIVE & NEGATIVE WORDS PATTERN FROM TXT.FILE #################################\n")
    # pattern searching for positive and negative words in articles using KMP algorithm
    article = b1
    print("\nPattern searching:")
    for i in range(len(article)):
        file = article[i]
        print("\nSearching for words in " + article[i] + "\n")
        with open(file, 'r') as readFile:
            list1 = readFile.read()
        print("\nPattern of positive words: \n")

        for j in range(len(list2)):
            pattern = list2[j]
            KMPSearch(pattern, list1)
            j = j + 1

        print("\nPattern for negative words: \n")
        for k in range(len(list3)):
            pattern = list3[k]
            KMPSearch(pattern, list1)
            k = k + 1
            i += 1

    print("\nAll pattern searching - completed")
    print("\n######################   POSITIVE & NEGATIVE WORDS PATTERN FROM TXT.FILE - END #################################\n")
def search(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0
	t = 0
	h = 1
	count = False


	for i in range(M-1):
		h = (h*d)%q


	for i in range(M):
		p = (d*p + ord(pat[i]))%q
		t = (d*t + ord(txt[i]))%q


	for i in range(N-M+1):

		if p==t:

			for j in range(M):
				if txt[i+j] != pat[j]:

					break

			j+=1

			if j==M:

				print ("Stopword pattern found at index " + str(i))
				count = True


		# Calculate hash value for next window of text: Remove
		# leading digit, add trailing digit
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

			# We might get negative values of t, converting it to
			# positive
			if t < 0:
				t = t+q
	return count
def stopwordPatternSearch(x1,x2):
    print("\n######################  STOPWORD PATTERN SEARCH USING RABIN-KARP FROM TXT.FILE #################################\n")
    array = [" a ", " the ", " about ", " an ", " are ", " as ", " at ", " be ", " by ", " for ", " from ", " how ",
             " in ", " is ", " it ", " of ", " on ", " or", " that ", " this ", " to ", " was ", " what ", " when ",
             " where ", " who ", " with ", " above ", " after ", " again ", " against ", " all ", " am ", " and ",
             " any ", " aren’t ",
             " because ", " been ", " before ", " being ", " below ", " between ", " both ", " but ", " can’t ",
             " cannot ", " could ", " couldn’t ", " did ", " didn’t ", " do ", " does ", " doesn’t ", " doing ",
             " don’t ", " down ", " during ", " each ", " few ", " further ", " had ", " hadn’t ", " has ", " hasn’t ",
             " have ", " haven’t ", " having ", " he ", " he’d ", " he’ll ", " he’s ", " her ", " here ", " here’s ",
             " hers ", " herself ", " him ", " himself ", " his ", " how’s ", " I’d ", " I’ll ", " I’m ", " I’ve ",
             " if ", " into ", " isn’t ", " its ", " its ", " itself ", " let’s ", " me ", " more ", " most ",
             " mustn’t ", " my ", " myself ", " no ", " nor ", " not ", " off ", " once ", " only ", " other ",
             " ought ", " our ", " ours ", " ourselves ", " out ", " over ", " own ", " same ", " shan’t ", " she ",
             " she’d ", " she’ll ", " she’s ", " should ", " shouldn’t ", " so ", " some ", " such ", " than ",
             " that’s ", " their ", " theirs ", " them ", " themselves ", " then ", " there ", " there’s ", " these ",
             " they ", " they’d ", " they’ll ", " they’re ", " they’ve ", " those ", " through ", " too ", " under ",
             " until ", " up ", " very ", " wasn’t ", " we ", " we’d ", " we’ll ", " were ", " we’ve ", " were ",
             " weren’t ", " what’s ", " when’s ", " where’s ", " which ", " while ", " who’s ", " whom ", " why ",
             " why’s ", " won’t ", " would ", " wouldn’t ", " you ", " you’d ", " you’ll ", " you’re ", " you’ve ",
             " your ", " yours ", " yourself ", " yourselves ", " com ", " will "
        , " A ", " The ", " About ", " An ", " Are ", " As ", " At ", " Be ", " By ", " For ", " From ", " How ",
             " In ",
             " Is ", " It ", " Of ", " On ", " Or", " That ", " This ", " To ", " Was ", " What ", " When ",
             " Where ", " Who ", " With ", " Above ", " After ", " Again ", " Against ", " All ", " Am ", " And ",
             " Any ", " Aren’t ", " Because ", " Been ", " Before ", " Being ", " Below ", " Between ", " Both ",
             " But ", " Can’t ", " Cannot ", " Could ", " Couldn’t ", " Did ", " Didn’t ", " Do ", " Does ",
             " Doesn’t ", " Doing ", " Don’t ", " Down ", " During ", " Each ", " Few ", " Further ", " Had ",
             " Hadn’t ", " Has ", " Hasn’t ", " Have ", " Haven’t ", " Having ", " He ", " He’d ", " He’ll ",
             " He’s ", " Her ", " Here ", " Here’s ", " Hers ", " Herself ", " Him ", " Himself ", " His ", " How’s ",
             " I’d ", " I’ll ", " I’m ", " I’ve ", " Hf ", " Into ", " Isn’t ", " Its ", " Its ", " Itself ",
             " Let’s ", " Me ", " More ", " Most ", " Mustn’t ", " My ", " Myself ", " No ", " Nor ", " Not ",
             " Off ", " Once ", " Only ", " Other ", " Ought ", " Our ", " Ours ", " Ourselves ", " Out ", " Over ",
             " Own ", " Same ", " Shan’t ", " She ", " She’d ", " She’ll ", " She’s ", " Should ", " Shouldn’t ",
             " So ", " Some ", " Such ", " Than ", " That’s ", " Their ", " Theirs ", " Them ", " Themselves ",
             " Then ", " There ", " There’s ", " These ", " They ", " They’d ", " They’ll ", " They’re ", " They’ve ",
             " Those ", " Through ", " Too ", " Under ", " Until ", " Up ", " Very ", " Wasn’t ", " We ", " We’d ",
             " We’ll ", " Were ", " We’ve ", " Were ", " Weren’t ", " What’s ", " When’s ", " Where’s ", " Which ",
             " While ", " Who’s ", " Whom ", " Why ", " Why’s ", " Won’t ", " Would ", " Wouldn’t ", " You ",
             " You’d ", " You’ll ", " You’re ", " You’ve ", " Your ", " Yours ", " Yourself ", " Yourselves ",
             " Com ", " Will ", " Rights Reserved ", " rights reserved "

             ]
    input = x1
    country = x2

    for k in range(len(input)):
        inputfile = input[k]
        inputname = country[k]
        print("\n------------------For ", country[k], ": -----------------------------------------\n")
        with open(inputfile, 'r') as myfile:
            txt = myfile.read()
        for i in range(len(array)):
            pattern = array[i]
            search(pattern, txt, q)
            i += 1
        k += 1
    print("\n######################  STOPWORD PATTERN SEARCH USING RABIN-KARP FROM TXT.FILE - END #################################\n")
def removeStop(x,y,z):
    print("\n######################  REMOVING STOPWORDS FROM TXT.FILE #################################\n")
    input = x
    clean = y
    country = z
    print("\n----------------Filtering-------------------------")
    delete_list = [" a ", " the ", " about ", " an ", " are ", " as ", " at ", " be ", " by ", " for ", " from ",
                   " how ", " in ", " is ", " it ", " of ", " on ", " or", " that ", " this ", " to ", " was ",
                   " what ", " when ", " where ", " who ", " with ", " above ", " after ", " again ", " against ",
                   " all ", " am ", " and ", " any ", " aren’t ",
                   " because ", " been ", " before ", " being ", " below ", " between ", " both ", " but ", " can’t ",
                   " cannot ", " could ", " couldn’t ", " did ", " didn’t ", " do ", " does ", " doesn’t ", " doing ",
                   " don’t ", " down ", " during ", " each ", " few ", " further ", " had ", " hadn’t ", " has ",
                   " hasn’t ", " have ", " haven’t ", " having ", " he ", " he’d ", " he’ll ", " he’s ", " her ",
                   " here ", " here’s ", " hers ", " herself ", " him ", " himself ", " his ", " how’s ", " I’d ",
                   " I’ll ", " I’m ", " I’ve ", " if ", " into ", " isn’t ", " its ", " its ", " itself ", " let’s ",
                   " me ", " more ", " most ", " mustn’t ", " my ", " myself ", " no ", " nor ", " not ", " off ",
                   " once ", " only ", " other ", " ought ", " our ", " ours ", " ourselves ", " out ", " over ",
                   " own ", " same ", " shan’t ", " she ", " she’d ", " she’ll ", " she’s ", " should ", " shouldn’t ",
                   " so ", " some ", " such ", " than ", " that’s ", " their ", " theirs ", " them ", " themselves ",
                   " then ", " there ", " there’s ", " these ", " they ", " they’d ", " they’ll ", " they’re ",
                   " they’ve ", " those ", " through ", " too ", " under ", " until ", " up ", " very ", " wasn’t ",
                   " we ", " we’d ", " we’ll ", " were ", " we’ve ", " were ", " weren’t ", " what’s ", " when’s ",
                   " where’s ", " which ", " while ", " who’s ", " whom ", " why ", " why’s ", " won’t ", " would ",
                   " wouldn’t ", " you ", " you’d ", " you’ll ", " you’re ", " you’ve ", " your ", " yours ",
                   " yourself ", " yourselves ", " com ", " will "
        , " A ", " The ", " About ", " An ", " Are ", " As ", " At ", " Be ", " By ", " For ", " From ", " How ",
                   " In ",
                   " Is ", " It ", " Of ", " On ", " Or", " That ", " This ", " To ", " Was ", " What ", " When ",
                   " Where ", " Who ", " With ", " Above ", " After ", " Again ", " Against ", " All ", " Am ", " And ",
                   " Any ", " Aren’t ", " Because ", " Been ", " Before ", " Being ", " Below ", " Between ", " Both ",
                   " But ", " Can’t ", " Cannot ", " Could ", " Couldn’t ", " Did ", " Didn’t ", " Do ", " Does ",
                   " Doesn’t ", " Doing ", " Don’t ", " Down ", " During ", " Each ", " Few ", " Further ", " Had ",
                   " Hadn’t ", " Has ", " Hasn’t ", " Have ", " Haven’t ", " Having ", " He ", " He’d ", " He’ll ",
                   " He’s ", " Her ", " Here ", " Here’s ", " Hers ", " Herself ", " Him ", " Himself ", " His ",
                   " How’s ",
                   " I’d ", " I’ll ", " I’m ", " I’ve ", " If ", " Into ", " Isn’t ", " Its ", " Its ", " Itself ",
                   " Let’s ", " Me ", " More ", " Most ", " Mustn’t ", " My ", " Myself ", " No ", " Nor ", " Not ",
                   " Off ", " Once ", " Only ", " Other ", " Ought ", " Our ", " Ours ", " Ourselves ", " Out ",
                   " Over ",
                   " Own ", " Same ", " Shan’t ", " She ", " She’d ", " She’ll ", " She’s ", " Should ", " Shouldn’t ",
                   " So ", " Some ", " Such ", " Than ", " That’s ", " Their ", " Theirs ", " Them ", " Themselves ",
                   " Then ", " There ", " There’s ", " These ", " They ", " They’d ", " They’ll ", " They’re ",
                   " They’ve ",
                   " Those ", " Through ", " Too ", " Under ", " Until ", " Up ", " Very ", " Wasn’t ", " We ",
                   " We’d ",
                   " We’ll ", " Were ", " We’ve ", " Were ", " Weren’t ", " What’s ", " When’s ", " Where’s ",
                   " Which ",
                   " While ", " Who’s ", " Whom ", " Why ", " Why’s ", " Won’t ", " Would ", " Wouldn’t ", " You ",
                   " You’d ", " You’ll ", " You’re ", " You’ve ", " Your ", " Yours ", " Yourself ", " Yourselves ",
                   " Com ", " Will ", " Rights Reserved ", " rights reserved "

                   ]

    #to filter the stopwords
    for i in range(len(input)):
        infile = input[i]
        outfile = cleaned[i]
        fin = open(infile)
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
                line = line.replace(word, " ") #it removes the stopwords
            fout.write(line)
        fin.close()
        fout.close()

        print("Done scanning and filtering process for:", infile)
        i += 1


    # Calculating the total number of words and stopwords
    # before
    for i in range(len(input)):
        file_name = input[i]
        words = 0
        with open(file_name, 'r') as file:
            for line in file:
                words += len(line.split())
        numbers[i] = words #total number of words before clean
        i += 1
    # after
    for i in range(len(cleaned)):
        file_name = cleaned[i]
        words = 0
        with open(file_name, 'r') as file:
            for line in file:
                words += len(line.split())
        totalnumber[i] = words #total number of words after clean
        stopwords[i] = numbers[i] - totalnumber[i] #number before clean - after clean
        i += 1

    # printing the data
    print("\n-----------Total number of words--------------")

    for k in range(len(numbers)):
        print("For ", country[k], ": ", numbers[k], " words ")
        k += 1

    print("\n--------------Total number of stopwords-----------\n")
    for k in range(len(stopwords)):
        print("For ", country[k], ": ", stopwords[k], " stopwords")
        k += 1



    print("\n######################  REMOVING STOPWORDS FROM TXT.FILE - END #################################\n")
def graph(P,N,n,t):
    Pcount = P
    Ncount = N
    numbers = n
    totalnumber = t
    app = dash.Dash()

    app.title = 'word count'

    print("Histogram for Word Count and Stopwords")

    app.layout = html.Div(
        html.Div([
            html.H1(
                children='Histogram',

            ),

            dcc.Graph(
                id='Word and Stop Count',
                figure={
                    'data': [
                        {'x': country, 'y': numbers, 'type': 'bar', 'name': 'Word Count'},
                        {'x': country, 'y': stopwords, 'type': 'bar', 'name': 'Stop Count'},
                    ],
                    'layout': {
                        'title': 'Word and Stop Count'
                    }
                }
            ), dcc.Graph(
                id='Histogram for Positive Word Count and Negative Word Count',
                figure={
                    'data': [
                        {'x': country, 'y': Pcount, 'type': 'bar', 'name': 'Positive Count'},
                        {'x': country, 'y': Ncount, 'type': 'bar', 'name': 'Negative Count'},
                    ],
                    'layout': {
                        'title': 'Positive and negative word'

                    }
                }
            ),

        ])
    )


    if __name__ == '__main__':
        app.run_server(port=3007,host= '127.0.0.1', debug = False
        )
def countecon(e,P,N):
    print("############## PROCESS OF CALCULATING & WRITING ECON VALUE TO FILE - BEGIN ##################")

    j = 0
    # #totalnumberofpos&neg
    # for a in range(len(Pcount)):
    #     tempStor = tempStor + (P[a] + N[a]) #


    for i in range(1, len(e),1):
        e[i] = (P[j] / (P[j] + N[j]))
        j = j + 1

    #to write the econ value to txt file for use in problem 3
    filex = open("econs.txt","w")
    for b in range (len(e)):
        filex.writelines(str(e[b]) + " \n")
    filex.close()
    print("Economic values is written to the file.")
    print("############## PROCESS OF CALCULATING & WRITING ECON VALUE TO FILE - END ##################")

# Driver program to test the above function

removeStop(input,cleaned,country)
#stopwordPatternSearch(input,country) #to see the pattern of stopwords using Rabin Karp algo
#posnegwordspattern(cleaned) # to see the pattern of pos/neg words using KMPSearch algo
storeposneg(cleaned,result)
countecon(economic,Pcount,Ncount)
#graph(Pcount,Ncount,numbers,totalnumber)

#to view the economic values
for i in range (1,len(economic),1):
    print("For country : ",country[i-1],", the economic value is = ", economic[i] ,"\n")





