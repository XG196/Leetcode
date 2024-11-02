class Solution:

    # find if replacable
    def isBalanced(self, s, d):

        n = len(s)

        q = w = e = r = 0
        for i in range(n):
            if s[i] == "Q":
                q += 1
            elif s[i] == "W":
                w += 1
            elif s[i] == "E":
                e += 1
            else:
                r += 1

        if ((d["Q"] > 0 and q == d["Q"]) or d["Q"] <= 0) and \
        ((d["W"] > 0 and w == d["W"]) or d["W"] <= 0) and \
        ((d["E"] > 0 and e == d["E"]) or d["E"] <= 0) and \
        ((d["R"] > 0 and r == d["R"]) or d["R"] <= 0): return True

        else:
            return False

    def checkMeetNewLetter(self, d, letter):

        if d["Q"] > 0 and letter == "Q":
            return (True, "Q")
        elif d["W"] > 0 and letter == "W":
            return (True, "W")
        elif d["E"] > 0 and letter == "E":
            return (True, "E")
        elif d["R"] > 0 and letter == "R":
            return (True, "R")
        else:
            return (False, -1)
    
    def updateCondition(self, d, t, ct, letter):
        
        isTargetExcluded = False
        if letter == "Q" and d["Q"] > 0: 
            isTargetExcluded = False
        elif letter == "W" and d["W"] > 0:
            isTargetExcluded = False
        elif letter == "E" and d["E"] > 0:
            isTargetExcluded = False
        elif letter == "R" and d["R"] > 0:
            isTargetExcluded = False
        else:
            isTargetExcluded = True
        
        if (t[ct] > d[ct] or ( t[ct] == d[ct] and isTargetExcluded)):
            return True
        else:
            return False


    
        
    def balancedString(self, s: str) -> int:
        
        # find the shortest substring contains the number of Qs, Qs Es, Qs Es Rs
        # Chnage Balanced substring O(N)

        dict_balance = {"Q": 0, "W":0, "E":0, "R":0}
        self.n = len(s)
        self.balance = self.n // 4
        
        # Initialize the balance number for 4 characters
        dict_balance["Q"] -= self.balance
        dict_balance["W"] -= self.balance
        dict_balance["E"] -= self.balance
        dict_balance["R"] -= self.balance

        for i in range(self.n):
            if s[i] == "Q":
                dict_balance["Q"] += 1
            if s[i] == "W":
                dict_balance["W"] += 1
            if s[i] == "E":
                dict_balance["E"] += 1
            if s[i] == "R":
                dict_balance["R"] += 1
        
        print("balance dictionary", dict_balance)

        if dict_balance["Q"] == 0 and dict_balance["W"] == 0 and dict_balance["E"] == 0 and dict_balance["R"] == 0:
            return 0

        min_len = self.n
        track_dict = {"Q": 0, "W":0, "E":0, "R":0}

        i = 0
        for k in range(self.n):

            res = self.checkMeetNewLetter(dict_balance, s[k])

            # if we have meet a new letter
            if res[0]:
                track_dict[res[1]] += 1
                
        
                # if this letter is more than we need

                # s[i] != res[1]
                # track_dict[res[1]] == dict_balance[res[1]]
                while ( i < k ):
                    if self.updateCondition(dict_balance, track_dict, res[1], s[i]):
                        track_dict[s[i]] -= 1
                        i += 1
                    else:
                        break
                
                # the process is done
                if self.isBalanced(s[i:k+1], dict_balance):
                    min_len = min(k-i+1, min_len)

        return min_len 

