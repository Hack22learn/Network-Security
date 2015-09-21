__auther__='Sudhanshu Patel@Tm'
__email__='query.b2cs@gmail.com'

#Kasiski Test To find Block Size of vigenere Cipher

def gcd(a, b):
    # Return GCd of 2 number
    while a != 0:
        a, b = b % a, a
    return b

def kasiskiTest(cipher,dependencyFactor=0.1):
    #Return aproximate block Size
    dc=dict()
    ini=0
    l=len(cipher)
    #find indexes of occurences of all triplet substring
    while True:
        if ini<l-5:
            key=cipher[ini:ini+3]
            #print key
            dc[key]=[]
            dc[key].append(ini)
            ini+=3
            ind=ini+3
        else:   break
        while True:
            ind=cipher.find(key,ind+3)
            #print ind
            #time.sleep(.2)
            if ind !=-1:
                dc[key].append(ind)
            else:   break
    #remove keys that is not repeated
    keyl=[]
    for key in dc:
        if len(dc[key])<2:
                keyl.append(key)
    for key in keyl:
        del dc[key]
    del keyl

    #finding difference of all
    diff=[]
    for key in dc:
        for i in range(1,len(dc[key])):
            diff.append(dc[key][i]-dc[key][i-1])
    # Now Take GCD OF ALL
    diff.sort()
    l=len(diff)
    margin=int(l*dependencyFactor)
    GCD=diff[margin-1]
    for i in range(margin,l-margin):
            gtemp=gcd(GCD,diff[i])
            #GCD=gtemp
            if gtemp !=1: #ignore Ossibility of blocksiZe=1
                 GCD=gtemp
    return GCD
            
if __name__=='__main__':
    #cipher='''jwmcphhbtlballjkbmkauslbzsgqmaydvlmqewifqaxehrtbfjsxxelhlipmegursqimaioamlurpbqpiiixsrtzqpqgwrut1467pvabitlxtuiiijyepbytxazaehefaswjbamtmkjyepbyqaxehrtbphbqmoayhavzjtulubnatpjrpbkqaxehrtbphvimozukmohblwokipvazmxbzouhebyuxvapspbbkrneopjxvdaxttbajtzlmjwmzvhgmpweclfuwptmoqqmqpdipbjyepbyjtfqsqimopd1508ywehdcmpahxbelcxcppdwqpdegsmvbxoohfwqxpdkmkausbeljpjrsqgmzaqpkopjxkxssdumvdtvqvvipbcyvmkyurqmougbeljgqqoubqrzsxxelhwwtlltzlubnxovlxlbkqezlnhtappltzfnysikkfgmapsiiysuhgpaubnlyilqqjxxvdiuiebldrqmougiiwxpjbairqqhjxwkuutlbkmwiqpicwtrddekhiipbcyvmkyurqmougexzegqdpdptifttazyyqmaiovqlcqcjxajxaqhrttihidqkoyh1553jlvaaizpvgialbhqdnyddxurpbqpiiiylbaipvxtjrpbicmvdipbaqqcihhtkqheubopjwmjpkhjraqslbkqgmmlqiqknsdckaugafndpsbfjdatpjrpzpfwmohbepxiuiabcuggiljimodxtzbhiptylhiqxutizfaxtufbijabkququlteiqaugvlmijjpayicqpecaylbaipvihkelctubhdibelfpbqlhcwczkqaqpjjbfvdhklbbsjblqhqifswiknusaftfagyfittbjjxvdhdtehlozmvzmtzbaoeqzhbagppdvtbdeglpvhhplyjepohitahuelvqvrdbewqgbflixvxklpvzlegbohdhufajtllbjdnyhdsiivdvefaxipbtuhaxnuqmisqhwptuiplkjwcpyufcfyusaqyecoplsjzfaouwovdagqouzmvhixbfzhttxaykmifupavaehmzbhtipoegbhloepohitaxfrnimyukqlbiezfcqimzvdkmozqiqlurttihidapfiimjdqhkluixlbyqqtv'''
    #Block size == 5 for both
    cipher='''luomfjfddbdynvzmzouqwqnlpueswqabxvcscysvsyzoxtrdpzuvzobjjkzcgewbisgokyqyovktndafkgkhitrbafseybkv1467nxkrkrnhjwgkszacrlovvcjqgfgpquullqorouzacrlosyzoxtrdzxdooyqafcfplrwvkdlcdflprlasyzoxtrdzxxgoypwioyxdjyyaknxkpovdjewfglowvxkfundlatlgyflvxnqzrvlqlrbvcluojljeozmganpkynvwesooaffgrlzacrlolrhaisgoyff1508wyoxfaozqjvdobevezffusztgeuwldvqyxhushffiouqwqdoblnlbiseojqsnmyflvmhiubwwlfrxalxgrlsatou\uu3\kk8ybuvzobjgrlqjvdobevezzacrlozbglsweyuiqcbvsaqokxheynowfcpswesnfvnxkmjrnpzlnlsbklcabesyypovdjeaaqibljolkuvzobjnvwesooapuvdhqabxubwqok\k\fjrhqafxvtcaydksfdobnvqlk\pp3\hh8owpsweweghpgesnffnvsvvrcjoaookyqtsvssalhqlvcaxtrvsxkbsueaf1553lvlcykjfxekkbdfsndabfhktndafkgkibdykzlzrlbfdgewlfgrlqsoesxjrmaxgsdyfluotfmflbqsqnlaseowbsgsudubeuqwecpdfnulvlbcdflprjfhuoyxdcrhywgclsweisblgoytzrblxknvibjgshkvgbpqzrwprkhclasssebvckaqwexvckhlzqageafgacibdykzlkfmoberwlxfgdobhndabjaympmocaflhdplffmvrdqllbsfssvuukudwqcpjhyiivkrvlzlvxnxfrgrbqxofporblqqcsjxdyizfftvltgenzljfrvolcryxkrcrkgjxaltbdomsedpbkvxhannxjbgedyxffwpqlrnvrlbpixfqkslftgpqzgrljwfchdwoosisfyzjwgrvaluezowdepowqcaogaqzbuhbpqqsyylfyiaewxofxkvdppjrvhqaiosvwncfqgfojrjrkzegedrbqcryxkrchvtlkwowisvrkcbpssgojlfioypsgsvktrvsxkbczvkgottsfmvkkvnlosovf'''
   
    print ".......Applying KasiskiTest......"
    print '.....Possible Block Size :',kasiskiTest(cipher,dependencyFactor=0.1)

    #__________________________Note______________________________#
    # I did Introduce dependencyFactor, Becouse we can't choose
    # all difference becouse some may be becouse of coincidence
    # Mostly either there value is abnormaly high or low
    # So we Sort difference list and reduce length of difference
    # list by by removing n element from begining of sorted diff
    # list and n  elelemt from end of sorted difference list
    # where n = length of diff list * dependecy Facter
    # So if result is not desirable change dependecy Facter
    # in range .05 to .5

# http://codecops.in


