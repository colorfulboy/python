class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score


    def print_score(self):
        print('%s:%s' %(self.name,self.score))


    def get_garde(self):
        if self.score>=90:
            return  'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)

print('bart.name=:',bart.name)
print('bart.score=:',bart.score)
bart.print_score()

print('garde of bart:',bart.get_garde())
print('garde of lisa:',lisa.get_garde())

bart=Student('闄堢剷褰?',100)
print(bart.name,bart.score)


