class Solution:

    def check(self, s1, s2, s3, i, j, k, check_s1):

        # check finish
        if ( k == len(s3) and  i == len(s1) and j == len(s2) ):
            return True
        
        # simple optimize
        if i == len(s1):
            return s2[j:] == s3[k:]
        if j == len(s2):
            return s1[i:] == s3[k:]

        # check s1 and s2 interleave s3
        if check_s1:
            if s1[i] == s3[k]:
                return self.check(s1, s2, s3, i+1, j, k+1, check_s1) or self.check(s1, s2, s3, i+1, j, k+1, not check_s1)
            else:
                return False 
        else:
            if s2[j] == s3[k]:
                return self.check(s1, s2, s3, i, j+1, k+1, check_s1) or self.check(s1, s2, s3, i, j+1, k+1, not check_s1)
            else:
                return False 


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 == 0 and n2 == 0 and n3 == 0:
            return True
        
        if n1 == 0 and n2 != 0 and n3 == 0:
            return False

        if n1 != 0 and n2 == 0 and n3 == 0:
            return False

        if n1 != 0 and n2 != 0 and n3 == 0:
            return False
        
        if n1 == 0 and n2 == 0 and n3 != 0:
            return False

        if n1 == 0 and s2 == s3:
            return True
        if n2 == 0 and s1 == s3:
            return True


        if self.check(s1, s2, s3, 0, 0, 0, True):
            return True
        elif self.check(s1, s2, s3, 0, 0, 0, False):
            return True
        else:
            return False