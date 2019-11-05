s=" If comrade Napoleon says it, it must be right "

a= [100, 200, 300]
def foo(arg):
        print(f'arg= {arg}')
        

class Foo:
        pass
if(__name__== '__main__'):
        print(s,'\n', a)

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
 
    
    def printMembers(self):
        if(__name__=='__main__'):
                print('Printing members of the Birds class')
                for member in self.members:
                        print('\t%s ' % member)


class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
 
 
    def printMembers(self):
        if(__name__=='__main__'):
                print('Printing members of the Mammals class')
                for member in self.members:
                        print('\t%s ' % member)

