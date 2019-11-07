class fraction(object):
    def __init__(self, numerator, denominator):
        #将分数正规化处理，即只在分子中出现负号
        if(denominator < 0):
            numerator = -numerator
            denominator = - denominator
        self.numerator = numerator
        self.denominator = denominator

    def add(self, a):
        numerator = self.numerator * a.denominator + self.denominator * a.numerator
        denominator = self.denominator * a.denominator
        result = fraction(numerator, denominator)
        return result.reduction()

        
    def substract(self, a):
        numerator = self.numerator * a.denominator - self.denominator * a.numerator
        denominator = self.denominator * a.denominator
        result = fraction(numerator, denominator)
        return result.reduction()

    def multiply(self, a):
        numerator = self.numerator * a.numerator
        denominator = self.denominator * a.denominator
        result = fraction(numerator, denominator)
        return result.reduction()
    
    def division(self, a):
        numerator = self.numerator * a.denominator
        denominator = self.denominator * a.numerator
        result = fraction(numerator, denominator)
        return result.reduction()


    #返回元组：约分后的分子，分母
    def reduction(self):
        #定义函数：求给定两数的最大公因数，其中x, y 是正数
        def gcd(x, y):
            if x > y:
                smaller = y
            else:
                smaller = x
            
            for i in range(1,smaller + 1):
                if((x % i == 0) and (y % i == 0)):
                    result = i
            
            return result

        if(self.numerator < 0):
            self.gcd = gcd(-self.numerator, self.denominator)
        else:
            self.gcd = gcd(self.numerator, self.denominator)
        result = fraction(self.numerator // self.gcd, self.denominator // self.gcd)
        return result

    def get_value(self):
        return self.numerator / self.denominator

    def reciprocal(self):
        return fraction(self.denominator, self.numerator)
         
    def display(self):
        print("{}/{}".format(self.numerator, self.denominator))

an, ad, bn, bd = map(int, input().split())
a = fraction(an, ad)
b = fraction(bn, bd)
a.reduction().display()
b.reduction().display()
result = a.add(b)
result.display()
result = a.substract(b)
result.display()
result = a.multiply(b)
result.display()
result = a.division(b)
result.display()
result = a.reciprocal().reduction()
result.display()
result = a.get_value()
print("{:.1f}".format(result))