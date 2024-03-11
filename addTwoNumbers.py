class Solution:
    def addTwoNumbers(self, l1 , l2):
        a=0
        b=0
        for i in range(0,100):
            if i<len(l1):
                a+=(l1[i])*(10**i)
            if i<len(l2):
                b+=l2[i]*(10**i)
            if i>=len(l1) and  i>= len(l2):
                c=a+b
                beark

        c_str=str(c) # int to string method
        for i in range(0,len(c_str)):


            





l1 = [2,4,3]
l2 = [5,6,4]

solution=Solution()
result=solution.addTwoNumbers(l1,l2)
print(result)

            
