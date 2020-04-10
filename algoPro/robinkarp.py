d = 256
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

# Driver program to test the above function
input = ["TotalChina.txt","TotalHK.txt","TotalJakarta.txt","TotalJapan.txt","TotalKorea.txt","TotalTaiwan.txt","TotalThai.txt"]
cleaned = ["CleanedTotalChina.txt","CleanedTotalHK.txt","CleanedTotalJakarta.txt","CleanedTotalJapan.txt","CleanedTotalKorea.txt","CleanedTotalTaiwan.txt","CleanedTotalThai.txt"]
country = ["China","Hong Kong","Jakarta","Japan","Korea","Taiwan","Thailand"]
#assigning values of 0 to the int arrays as the value will change later.
numbers = [0,0,0,0,0,0,0]
numbers1 = [0,0,0,0,0,0,0]
stopwords = [0,0,0,0,0,0,0]


array = [" a ", " the ", " about ", " an ", " are ", " as ", " at ", " be ", " by ", " for ", " from ", " how ", " in ", " is ", " it ", " of ", " on ", " or", " that ", " this ", " to ", " was ", " what ", " when ", " where ", " who ", " with ", " above ", " after ", " again ", " against ", " all ", " am ", " and ", " any ", " aren’t ",
 " because ", " been ", " before ", " being ", " below ", " between ", " both ", " but ", " can’t ", " cannot ", " could ", " couldn’t ", " did ", " didn’t ", " do ", " does ", " doesn’t ", " doing ", " don’t ", " down ", " during ", " each ", " few ", " further ", " had ", " hadn’t ", " has ", " hasn’t ", " have ", " haven’t ", " having ", " he ", " he’d ", " he’ll ", " he’s ", " her ", " here ", " here’s ", " hers ", " herself ", " him ", " himself ", " his ", " how’s ", " I’d ", " I’ll ", " I’m ", " I’ve ", " if ", " into ", " isn’t ", " its ", " its ", " itself ", " let’s ", " me ", " more ", " most ", " mustn’t ", " my ", " myself ", " no ", " nor ", " not ", " off ", " once ", " only ", " other ", " ought ", " our ", " ours ", " ourselves ", " out ", " over ", " own ", " same ", " shan’t ", " she ", " she’d ", " she’ll ", " she’s ", " should ", " shouldn’t ", " so ", " some ", " such ", " than ", " that’s ", " their ", " theirs ", " them ", " themselves ", " then ", " there ", " there’s ", " these ", " they ", " they’d ", " they’ll ", " they’re ", " they’ve ", " those ", " through ", " too ", " under ", " until ", " up ", " very ", " wasn’t ", " we ", " we’d ", " we’ll ", " were ", " we’ve ", " were ", " weren’t ", " what’s ", " when’s ", " where’s ", " which ", " while ", " who’s ", " whom ", " why ", " why’s ", " won’t ", " would ", " wouldn’t ", " you ", " you’d ", " you’ll ", " you’re ", " you’ve ", " your ", " yours ", " yourself ", " yourselves ", " com ", " will "
    , " A ", " The ", " About ", " An ", " Are ", " As ", " At ", " Be ", " By ", " For ", " From ", " How ", " In ",
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
q = 101 # A prime number

print("-------------------------This is a program designed to solve problem number 2 which are : ----------------------------")
print("-------------------------1. Implementing rabin karp algorithm to find and remove stopwords. ----------------------------")
print("-------------------------2. Counting the number of words and stopwords in an article----------------------------")

for k in range(len(input)):
    inputfile = input[k]
    inputname = country[k]
    print("\n------------------For ",country[k],": -----------------------------------------\n")
    with open(inputfile, 'r') as myfile:
        txt = myfile.read()
    for i in range(len(array)):
        pattern = array[i]
        search(pattern,txt,q)
        i +=1
    k += 1

print("\n---------------end of search-------------------")

print("\n-------------Counting the total number of words and stopwords.------------")

#Counting the number of words before and after cleaning.
#before
for i in range(len(input)):
    file_name = input[i]
    words = 0
    with open(file_name, 'r') as file:
        for line in file:
            words += len(line.split())
    numbers[i] = words
    i += 1
#after
for i in range(len(cleaned)):
    file_name = cleaned[i]
    words = 0
    with open(file_name, 'r') as file:
        for line in file:
            words += len(line.split())
    numbers1[i] = words
    stopwords[i] = numbers[i] - numbers1[i]
    i += 1

#printing the data
print("\n-----------Total number of words--------------")

for k in range(len(numbers)):
    print("For ",country[k] ,": ",numbers[k], " words ")
    k +=1


print("\n--------------Total number of stopwords-----------\n")
for k in range(len(stopwords)):
    print("For ",country[k] ,": ",stopwords[k], " stopwords")
    k +=1

#printing the filtering process
print("\n----------------Filtering-------------------------")
delete_list = [" a ", " the ", " about ", " an ", " are ", " as ", " at ", " be ", " by ", " for ", " from ", " how ", " in ", " is ", " it ", " of ", " on ", " or", " that ", " this ", " to ", " was ", " what ", " when ", " where ", " who ", " with ", " above ", " after ", " again ", " against ", " all ", " am ", " and ", " any ", " aren’t ",
 " because ", " been ", " before ", " being ", " below ", " between ", " both ", " but ", " can’t ", " cannot ", " could ", " couldn’t ", " did ", " didn’t ", " do ", " does ", " doesn’t ", " doing ", " don’t ", " down ", " during ", " each ", " few ", " further ", " had ", " hadn’t ", " has ", " hasn’t ", " have ", " haven’t ", " having ", " he ", " he’d ", " he’ll ", " he’s ", " her ", " here ", " here’s ", " hers ", " herself ", " him ", " himself ", " his ", " how’s ", " I’d ", " I’ll ", " I’m ", " I’ve ", " if ", " into ", " isn’t ", " its ", " its ", " itself ", " let’s ", " me ", " more ", " most ", " mustn’t ", " my ", " myself ", " no ", " nor ", " not ", " off ", " once ", " only ", " other ", " ought ", " our ", " ours ", " ourselves ", " out ", " over ", " own ", " same ", " shan’t ", " she ", " she’d ", " she’ll ", " she’s ", " should ", " shouldn’t ", " so ", " some ", " such ", " than ", " that’s ", " their ", " theirs ", " them ", " themselves ", " then ", " there ", " there’s ", " these ", " they ", " they’d ", " they’ll ", " they’re ", " they’ve ", " those ", " through ", " too ", " under ", " until ", " up ", " very ", " wasn’t ", " we ", " we’d ", " we’ll ", " were ", " we’ve ", " were ", " weren’t ", " what’s ", " when’s ", " where’s ", " which ", " while ", " who’s ", " whom ", " why ", " why’s ", " won’t ", " would ", " wouldn’t ", " you ", " you’d ", " you’ll ", " you’re ", " you’ve ", " your ", " yours ", " yourself ", " yourselves ", " com ", " will "
    , " A ", " The ", " About ", " An ", " Are ", " As ", " At ", " Be ", " By ", " For ", " From ", " How ", " In ",
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

for i in range(len(input)):
    infile = input[i]
    outfile = cleaned[i]
    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, " ")
        fout.write(line)
    fin.close()
    fout.close()

    print("Done scanning and filtering process for:", infile)
    i +=1


