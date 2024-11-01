class Solution:

    def isBalanced(self, q, w, e, r, d):

        if ((d["Q"] > 0 and q == d["Q"]) or d["Q"] <= 0) and \
        ((d["W"] > 0 and w == d["W"]) or d["W"] <= 0) and \
        ((d["E"] > 0 and e == d["E"]) or d["E"] <= 0) and \
        ((d["R"] > 0 and r == d["R"]) or d["R"] <= 0): return True

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

    
        # find the first balanced substring
        i = 0
        j = 0
        q_cnt = w_cnt = e_cnt = r_cnt = 0
        while ( j<self.n ):
            if s[j] == "Q":
                q_cnt += 1
            elif s[j] == "W":
                w_cnt += 1
            elif s[j] == "E":
                e_cnt += 1
            else:
                r_cnt += 1
            if self.isBalanced(q_cnt, w_cnt, e_cnt, r_cnt, dict_balance):
                break
            


