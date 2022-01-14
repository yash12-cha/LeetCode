class Solution(object):
    def reverse(self, x):
        reverse = 0
        # when input greater than 0
        if x > 0:
            while(x>0):
                end = x%10 
                reverse = reverse*10 + end  
                x = x//10 
            # if reversed integer not overflow
            
            if reverse < 2**31-1:
                return reverse
            
            # if reversed integer overflow
          
            else:
                return 0
        # when input less than 0
        
        if x < 0:
            while(abs(x)>0):
                dig=abs(x)%10
                reverse=reverse*10+dig
                x=abs(x)//10
           
             # if reversed integer not overflow
            if -reverse > -2**31:
                return -reverse
            
            # if reversed integer overflow
            else:
                return 0
        # when input is equal to 0
        
        if x == 0:
            return x
