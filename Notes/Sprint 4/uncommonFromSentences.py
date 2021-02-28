""" 
We are given two sentences A and B.  (A sentence is a string of space separated words.  
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not 
appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Plan

c = {apple: 2, banana: 1}
res = ["banana"]
Create two dictionaries that contain the word count of both sentences
Go through each word in both sentences
        If a word has a count of 1 then that means it only occurs in one sentence
        add that to our result
return result
"""

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        wordCount = defaultdict(int)
        C = A + " " + B
        listC = C.split(" ")
        aggregatedList = listC

        for word in aggregatedList:
            wordCount[word] += 1

        res = []

        for word in listC:
            if wordCount[word] == 1:
                res.append(word)
        
        return res

A = "this apple is sweet"
B = "this apple is sour"

print(res)