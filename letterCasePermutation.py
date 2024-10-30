class Solution:
    

    def getPmt(self, s, i, cons, list_of_pmt):

        if i == len(s):
            list_of_pmt.append(cons)  
            return
        
        if s[i].isalpha():
            new_str = cons + s[i].lower()
            self.getPmt(s, i+1, new_str, list_of_pmt)

            new_str = cons + s[i].upper()
            self.getPmt(s, i+1, new_str, list_of_pmt)

        else:
            new_str = cons + s[i]
            self.getPmt(s, i+1, new_str, list_of_pmt)

        return


    def letterCasePermutation(self, s: str):

        # return a list of all possible strings
        list_of_pmt = []   # can append inside other functions
        self.getPmt(s.lower(), 0, "", list_of_pmt)

        return list_of_pmt


def main():
    sol = Solution()
    sol.letterCasePermutation("A1B3")


main()


