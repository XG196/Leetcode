class Solution:
    def reverseWords(self, s: str) -> str:
        # word: a sequence of Non-Space characters
        # words: separated by at least one space
        
        # Get all the words
        # Reverse the words
        # Construct with single space 
        return " ".join(reversed(s.split()))
        
        

        
        
        