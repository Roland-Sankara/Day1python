
Alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def list_sort(t):
        Even = []
        Odd = []
        Chars = []
        d = {'Even':Even,'Odd':Odd,'Chars':Chars}


        for s in t:
                if s in Alpha:
                        Chars.append(s) 
                elif s%2 == 0:
                        Even.append(s)
                else:
                        Odd.append(s)        
        return d


print(list_sort([0,1,2,3,4,5,6,7,8,'A','B','C']))           
