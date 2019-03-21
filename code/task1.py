import os
import re
import math
from collections import Counter


hamiltonEssays = ['1.txt', '6.txt','7.txt','8.txt','13.txt','15.txt', '16.txt', '17.txt', '21.txt', '22.txt','23.txt','24.txt','25.txt', '26.txt', '27.txt', '28.txt', '29.txt']
madisonEssays = ['10.txt','14.txt','37.txt','38.txt','39.txt','40.txt', '41.txt', '42.txt', '43.txt','44.txt', '45.txt', '46.txt']
hamiltonList = []
madisonList = []
# Madison and Hamilton's essay files path.
dataPath = 'data/'
fileList = os.listdir(dataPath)
# Data Path for files which we get from.

def create_ngram(s, n):
    # Convert to lowercases
    s = s.lower()

    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

for h in hamiltonEssays:
    hFile = open(os.path.join(dataPath+h),'r')
    hamiltonList.append(hFile.readlines()[1].split())
    hFile.close()
for m in madisonEssays:
    mFile = open(os.path.join(dataPath+m),'r')
    madisonList.append(mFile.readlines()[1].split())
    mFile.close()


def wordCounter(tokens, token):
    count = 0
    for i in tokens:
        if i == token:
            count +=1
    return count







### burdannnnn
unimad =create_ngram(str(madisonList), 1)
uniham =create_ngram(str(hamiltonList), 1)

bimad = create_ngram(str(madisonList), 2)
biham = create_ngram(str(hamiltonList), 2)

trimad = create_ngram(str(madisonList), 3)
triham = create_ngram(str(hamiltonList), 3)


totalinUniHamilton = len(uniham)
uniqueinUniHamilton = len(set(uniham))
totalinUniMadison = len(unimad)
uniqueinUniMadison= len(set(unimad))

totalinBiHamilton = len(biham)
uniqueinBiHamilton = len(set(biham))
totalinBiMadison = len(bimad)
uniqueinBiMadison = len(set(bimad))

totalinTriHamilton = len(triham)
uniqueinTriHamilton = len(set(triham))
totalinTriMadison = len(trimad)
uniqeinTriMadison= len(set(trimad))


unigramDictHamilton = dict()
unigramDictMadison = dict()
bigramDictHamilton = dict()
bigramDictMadison = dict()
trigramDictHamilton = dict()
trigramDictMadison = dict()


freqUniHam = Counter(uniham)
freqUniMad = Counter(unimad)
freqBiHam = Counter(biham)
freqBiMad = Counter(bimad)
freqTriHam = Counter(triham)
freqTriMad = Counter(trimad)

for i in set(uniham):
    unigramDictHamilton[i] = freqUniHam[i]/totalinUniHamilton
print("Hamilton Unigram", unigramDictHamilton) #for test
for i in set(unimad):
    unigramDictMadison[i] = freqUniMad[i]/totalinUniMadison
print("Madison Unigram", unigramDictMadison) #for test
for i in set(biham):
    bigramDictHamilton[i] = freqBiHam[i]/totalinBiHamilton
print("Hamilton Bigram", bigramDictHamilton) #for test
for i in set(bimad):
    bigramDictMadison[i] = freqBiMad[i]/totalinBiMadison
print("Madison Bigram", bigramDictMadison) #for test
for i in set(triham):
    trigramDictHamilton[i] = freqTriHam[i]/totalinTriHamilton
print("Hamilton Trigram", trigramDictHamilton)
for i in set(trimad):
    trigramDictMadison[i] = freqTriMad[i]/totalinBiMadison
print("Madison Trigram", trigramDictMadison)
#####
### If we want we can write the dictionaries to file.
#####
dosya = open('a.txt', 'w')
dosya.write("Hamilton Uni: " + str(unigramDictHamilton)[:200] +'\n')
dosya.write("Hamilton Bi: " + str(bigramDictHamilton)[:200]+'\n')
dosya.write("Hamilton Tri: " + str(trigramDictHamilton)[:200]+'\n')
dosya.write("Madisaon Uni: " + str(unigramDictMadison)[:200]+'\n')
dosya.write("Madison Bi: " + str(bigramDictMadison)[:200]+'\n')
dosya.write("Madison Tri: " + str(trigramDictMadison)[:200]+'\n')
dosya.close()






########################################################################################################################
########################################################################################################################
#####################################               TASK 2                 #############################################
########################################################################################################################
########################################################################################################################




########################################################################################################################
########################################################################################################################
#####################################               TASK 3                 #############################################
########################################################################################################################
########################################################################################################################
testhamilton =['9.txt','11.txt','12.txt']
testMadison = ['47.txt', '48.txt', '58.txt']
unknowns = ['49.txt', '50.txt', '51.txt', '52.txt', '53.txt', '54.txt', '55.txt', '56.txt' , '57.txt', '62.txt','63.txt']
testData = unknowns #or unknowns
# testHList = []
# testHListBi = []
# testHListTri = []
# testMList = []
# testMListBi = []
# testMListTri = []
testListBi = []
testListTri = []


for td in testData:
    tdFile = open(os.path.join(dataPath+td), 'r')
    linesTD = tdFile.readlines()[1].split()
    testListBi.append(create_ngram(str(linesTD), 2))
    testListTri.append(create_ngram(str(linesTD), 3))
    tdFile.close()

sumOfPossibilitiesHamilton = 0
sumOfPossibilitiesMadison = 0
perplexityHamilton = 0
perplexityMadison = 0
for i in range(0, len(testListBi)):
    for j in testListBi[i]:

        if j in bigramDictHamilton:
            sumOfPossibilitiesHamilton += math.log2(bigramDictHamilton.get(j))
        else:
            sumOfPossibilitiesHamilton += math.log2(1/(uniqueinUniHamilton + freqUniHam[j.split()[0]]))
    for k in testListBi[i]:
        if k in bigramDictMadison:
            sumOfPossibilitiesMadison += math.log2(bigramDictMadison.get(k))
        else:
            sumOfPossibilitiesMadison += math.log2((1/(uniqueinUniMadison + freqUniMad[k.split()[0]])))
    if pow(2, -1/len(bigramDictHamilton))*sumOfPossibilitiesHamilton < pow(2, -1/len(bigramDictMadison))*sumOfPossibilitiesMadison:
        print(testData[i], "HAMILTON")
    else:
        print(testData[i], "MADISON")



# Trigram
sumOfPossibilitiesHamiltonTri = 0
sumOfPossibilitiesMadisonTri = 0

print("----- Trigram")

for i in range(0, len(testListTri)):
    for j in testListTri[i]:
        if j in trigramDictHamilton:
            sumOfPossibilitiesHamiltonTri += math.log2(trigramDictHamilton.get(j))
        else:
            sumOfPossibilitiesHamiltonTri += math.log2(1/totalinTriHamilton)
    for k in testListTri[i]:
        if k in trigramDictMadison:
            sumOfPossibilitiesMadisonTri += math.log2(trigramDictMadison.get(k))
        else:
            sumOfPossibilitiesMadisonTri += math.log2(1/totalinTriMadison)
    if pow(2, -1/len(trigramDictHamilton))*sumOfPossibilitiesHamiltonTri < pow(2, -1/len(trigramDictMadison))*sumOfPossibilitiesMadison:
        print(testData[i], "HAMILTON")
    else:
        print(testData[i], "MADISON")


# for th in testhamilton:
#     thFile = open(os.path.join(dataPath+th),'r')
#     linesh=thFile.readlines()[1].split()
#     testHList.append(create_ngram(str(linesh), 1))
#     testHListBi.append(create_ngram(str(linesh), 2))
#     testHListTri.append(create_ngram(str(linesh), 3))
#     thFile.close()
#
# for tm in testMadison:
#     tmFile = open(os.path.join(dataPath+tm),'r')
#     linesm=tmFile.readlines()[1].split()
#     testMList.append(create_ngram(str(linesm), 1))
#     testMListBi.append(create_ngram(str(linesm), 2))
#     testMListTri.append(create_ngram(str(linesm), 3))
#     tmFile.close()
#
# print(testHList)
# phn1 =0
# for i in range(0,len(testHList)):
#     for j in testHList[i]:
#         if j in unigramDictHamilton:
#             phn1 += math.log2(unigramDictHamilton.get(j))
#     print('Hamilton UniGram: ', pow(2, -1/1)*phn1)
#
# pmn1 = 0
# for i in range(0, len(testMList)):
#     for j in testMList[i]:
#         if j in unigramDictMadison:
#             pmn1 += math.log2(unigramDictMadison.get(j))
#     print('Madison UniGram: ', pow(2, -1 / 1) * pmn1)


# phn2 =0
# for i in range(0,len(testHListBi)):
#     for j in testHListBi[i]:
#         if j in bigramDictHamilton:
#             phn2 += math.log2(bigramDictHamilton.get(j))
#         else:
#             phn2 += math.log2(1/totalinBiHamilton)
#     perphn2= pow(2, -1/2)*phn2
#     print('Hamilton BiGram: ', perphn2)
#
# pmn2 = 0
# for i in range(0,len(testMListBi)):
#     for j in testMListBi[i]:
#         if j in bigramDictMadison:
#             pmn2 += math.log2(bigramDictMadison.get(j))
#         else:
#             pmn2 += math.log2(1/totalinBiMadison)
#     perpmn2=pow(2, -1/2)*pmn2
#     print('Madison BiGram: ', perpmn2)
#




# phn3 =0
# for i in range(0,len(testHListTri)):
#     for j in testHListTri[i]:
#         if j in trigramDictHamilton:
#             phn3 += math.log2(trigramDictHamilton.get(j))
#     print('Hamilton TriGram: ', pow(2, -1/1)*phn3)
#
# pmn3 = 0
# for i in range(0,len(testMListTri)):
#     for j in testMListTri[i]:
#         if j in trigramDictMadison:
#             pmn3 += math.log2(trigramDictMadison.get(j))
#     print('Madison TriGram: ', pow(2, -1/1)*pmn3)















# -------------------------------------------







# for a in uniTestHamilton:
#     if a in unigramDictHamilton:
#         print(a, unigramDictHamilton.get(a))
#     else:
#         unigramDictHamilton[a] = 0
#         print(a, unigramDictHamilton.get(a))
