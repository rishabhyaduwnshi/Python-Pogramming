class Rational_Number:
    def __init__(self,p=1,q=1):
        self.p = p;
        self.q = q;
        
    #overriding the + operator
    def __add__(self,other):
        result =  Rational_Number()
        result.p = self.p * other.q + self.q * other.p
        result.q = self.q * other.q
        return result
        
    #overriding print function
    def __str__(self):
        return str(self.p) + '/' + str(self.q)

rational_number_r1 = Rational_Number(2,3)
rational_number_r2 = Rational_Number(2,5)

r1_sum_r2 = rational_number_r1 + rational_number_r2
print(r1_sum_r2)
