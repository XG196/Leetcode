class Solution:

    def check(self, prev_q, prev_w, prev_e, prev_r):
        
        qc = wc = ec = rc = False

        if (self.q > 0 and prev_q >= self.q) or (self.q <= 0):
            qc = True
        
        if (self.w > 0 and prev_w >= self.w) or (self.w <= 0):
            wc = True
        
        if (self.e > 0 and prev_e >= self.e) or (self.e <= 0):
            ec = True
        
        if (self.r > 0 and prev_r >= self.r) or (self.r <= 0):
            rc = True
        
        if qc == True and wc == True and ec ==  True and rc == True:
            return True
        else:
            False
    
    def balancedString(self, s: str) -> int:
        
        # substring : can be replaced with any other string of the same length to make s balanced 
        
        # the string s contains four characters Q W E and R, length of N, s is balanced if each character appears N/4 times
        # find a substring (...) inside the string s, find a shortest one.

        n = len(s)
        self.q = self.w = self.e = self.r = -(n/4)
        for i in range(n):
            if s[i] == "Q":
                self.q += 1
            elif s[i] == "W":
                self.w += 1
            elif s[i] == "E":
                self.e += 1
            else:
                self.r += 1

        if self.q == 0 and self.w == 0 and self.e == 0 and  self.r == 0:
            return 0
        
        # when the string is not balanced
        min_len = n
        # dp = [ [0 for j in range(n)] for i in range(n) ]

        for i in range(n):

            if s[i] == "Q" and self.q <= 0:
                continue
            elif s[i] == "W" and self.w <= 0:
                continue
            elif s[i] == "E" and self.e <= 0:
                continue
            elif s[i] == "R" and self.r <=0:
                continue
        
            prev_q = prev_w = prev_e = prev_r = 0
            prev_res = 0
            for j in range(i, n):
                
                if len(s[i:j+1]) > min_len:
                    continue

                # previous string is good
                if prev_res > 0:
                    # no need to do anything
                    continue

                if i == j:
                    if s[j] == "Q":
                        prev_q += 1
                    elif s[j] == "W":
                        prev_w += 1
                    elif s[j] == "E":
                        prev_e += 1
                    else:
                        prev_r += 1
                    if self.check(prev_q, prev_w, prev_e, prev_r):
                        prev_res = 1
                        min_len = min(min_len, (j-i+1))
                    else:
                        prev_res = -1
                else:
                    # if previous string is bad    
                    # update dp_save and check
                    if s[j] == "Q":
                        prev_q += 1
                    elif s[j] == "W":
                        prev_w += 1 
                    elif s[j] == "E":
                        prev_e += 1
                    else:
                        prev_r += 1

                    if self.check(prev_q, prev_w, prev_e, prev_r):
                        prev_res = 1
                        min_len = min(min_len, (j-i+1))
                    else:
                        prev_res = -1

        return min_len


        


