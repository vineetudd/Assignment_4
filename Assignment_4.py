## ASSIGNMENT 4
# 1.1 Area of triangle using heron's formula
class Triangle:
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def perimeter(self):
        p=self.s1+self.s2+self.s3
        return p
    def area(self):
        s=self.perimeter()/2
        a=(s*(s-self.s1)*(s-self.s2)*(s-self.s3))**0.5
        return a
# 1.2 filter_long_words function
def filter_long_words(l,n):
    r=[]
    for i in l:
        if len(i)>n:
            r.append(i)
    return r
# 2.1 list returning length of words in the list passed as argument
def word_length(l):
    rl=[]
    for i in l:
        m=len(i)
        rl.append(m)
    return rl
# 2.2 Vowel identification function
def if_vowel(a):
    if a=='a'or a=='A'or a=='e'or a=='E'or a=='i'or a=='I'or a=='o'or a=='O':
        return True
    else:
        return False
