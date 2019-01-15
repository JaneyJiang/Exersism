import re

class Phone(object):
    country_code = '1' 
    def __init__(self, phone_number):
        #eg:+1 (613)-995-0253 | 613-995-0253 | 1 613 995 0253 | 613.995.0253 are all valid.
        #(NXX) NXX-XXXX N[2-9] X[0-9]
        numbers = re.sub("\D","",phone_number)#replace非数字为''
        if numbers[0]==self.country_code:
            numbers = numbers[1:]
            
        if len(numbers) != 10:
            raise ValueError("the input format is wrong!")

        self.area_code,self.exchange_code,self.subscriber_number = numbers[:3],numbers[3:6],numbers[6:]

        if self.area_code[0]>self.country_code and self.exchange_code[0]>self.country_code:
            self.number = numbers
        else:
            raise ValueError("the input format is wrong!")   

    def pretty(self):
        return "({}) {}-{}".format(self.area_code,self.exchange_code,self.subscriber_number)

