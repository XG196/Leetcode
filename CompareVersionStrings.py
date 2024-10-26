class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # A version string consists of revisions separated by dots 
        # Get the revions one by one, append them to list and compare them as integers

        i = j = 0
        l1 = len(version1)
        l2 = len(version2)

        # get revisions of version1
        rev1 = []
        prev = 0
        while (i < l1):

            # handle the revision
            if version1[i] == "." or i == l1-1:
                if i == l1-1:
                    substr = version1[prev: i+1]
                else:
                    substr = version1[prev: i]

                # ignore the leading zeros
                sub_prev = 0
                while (sub_prev < len(substr)):
                    if substr[sub_prev] == "0":
                        sub_prev += 1
                    else:
                        break
                
                if sub_prev == len(substr):
                    rev1.append("0")
                else:
                    rev1.append(substr[sub_prev: len(substr)])

                prev = i+1

            i += 1
        
        
        # get revisions of version2
        rev2 = []
        prev = 0
        while (j < l2):

            # handle the revision
            if version2[j] == "." or j == l2-1:
                if j == l2-1:
                    substr = version2[prev: j+1]
                else:
                    substr = version2[prev: j]

                # ignore the leading zeros
                sub_prev = 0
                while (sub_prev < len(substr)):
                    if substr[sub_prev] == "0":
                        sub_prev += 1
                    else:
                        break
                
                if sub_prev == len(substr):
                    rev2.append("0")
                else:
                    rev2.append(substr[sub_prev: len(substr)])

                prev = j+1

            j += 1
        
        # pad zeros
        print("rev1", rev1)
        print("rev2", rev2)
        num1 = len(rev1)
        num2 = len(rev2)
        

        if num1 >= num2:
            diff = num1 - num2
            for _ in range(diff):
                rev2.append("0")
        else:
            diff = num2 - num1
            for _ in range(diff):
                rev1.append("0")
        
        # comparision
        for k, _ in enumerate(rev1):
            if int(rev1[k]) == int(rev2[k]):
                continue
            elif int(rev1[k]) > int(rev2[k]):
                return 1
            else:
                return -1 

        return 0
    

def main():
    sol = Solution()
    print(sol.compareVersion("1", "1.1"))

main()
