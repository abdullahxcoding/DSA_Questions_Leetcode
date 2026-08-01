class Solution:
    def reverseVowels(self, s: str) -> str:
        char = list(s)
        i =0 
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        j = len(char)-1 

        while i < j  :
            if char[i] in vowels and  char[j] in vowels:
                char[i],char[j] = char[j],char[i]
                i+=1 
                j-=1
            elif char[i] in vowels and char[j] not in vowels:
                j-=1 
            elif char[j] in vowels and char[i] not in vowels:
                i+=1 
            else :
                i+=1 
                j-=1 
        return ''.join(char)

