class Solution:

    def check(self, s1, s2, s3, i, j, k, check_s1):
        
        # check finish
        if ( k == len(s3) ):
            return True

        # if ( i == len(s1) and k < len(s3) ):
        #     return False

        # if ( j == len(s2) and k < len(s3) ):
        #     return False
        
        while (k < len(s3)):

            # check current character
            if  check_s1:

                if i < len(s1) and s1[i] == s3[k]:   
                    if self.check(s1, s2, s3, i+1, j, k+1, not check_s1):
                        return True
                    else:
                        return self.check(s1, s2, s3, i+1, j, k+1, check_s1)

                else:
                    return False
                
            else:
                if j < len(s2) and s2[j] == s3[k]:   
                    if self.check(s1, s2, s3, i, j+1, k+1, not check_s1):
                        return True
                    else:
                        return self.check(s1, s2, s3, i, j+1, k+1, check_s1)
                else:
                    return False
            

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 == 0 or n2 == 0 or n3 == 0:
            return False

        if self.check(s1, s2, s3, 0, 0, 0, True):
            return True
        elif self.check(s1, s2, s3, 0, 0, 0, False):
            return True
        else:
            return False


def main():
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    
main()




        