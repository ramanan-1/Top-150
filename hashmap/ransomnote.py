class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = {}

        #Count charFreq of char in magazine

        for char in magazine :
            if char not in freq :
                freq[char] = 1
            else:
                freq[char]+=1

        #loop through each element in ransomeNote

        for char in ransomNote:

            #if char in freq then reduce freq of char by 1
            if char in freq and freq[char] != 0 :
                freq[char] -= 1 
            else:
                return False
        return True                       
        