infile = "korea4.txt"
outfile = "cleaned_korea4.txt"

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

fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, " ")
    fout.write(line)
fin.close()
fout.close()