from typing import List
def minReplacements(words: List[str]) -> List[int]:
    result=[]

    for word in words:
        i=0
        count=0
        while i<len(word)-1:
            if word[i]==word[i+1]:
                count+=1
                i+=2
            else: 
                i+=1
        result.append(count)
    return result
print(minReplacements(["aaaa", "bbbb", "aabbbaac"]))
