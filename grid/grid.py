class Grue():
    def __init__(self, x, y):
        self._x = x #The under before x is to imply this variable is private
        self._y = y
    
    def __repr__(self):
        '''
        Defines the official string representation of the Grue object, for machine 
        Returns string '(x, y)'
        '''
        return f'Grue({self._x}, {self._y})'
    
    def __str__(self):
        '''
        Returns a readable string of the Grue object's position used by print, etc.
        '''
        return f'(x:{self._x} y:{self._y})'

    def __eq__(self, other):
        '''
        Describes what will happen with == operator between instances of Grue objects
        '''
        return self._x == other._x and self._y == other._y

    def yell(self):
        #print('I am located at: column {} row {}'.format(self._x, self._y))
        print(f'I am located at: column {self._x}, row {self._y}')

    def location(self):
        return (self._x, self._y)

def view(field, grue):
    #for 
    pass

def mkfield(n):
    '''
    Makes a square field of size n, returns field
    '''
    row = [' ' for x in range(n)]
    field = [list(row) for x in range(n)]
    return field

def wall(field, x, y, char):
    field[x, y] = char

def showfield(field, grues):
    '''
    Displays field object in good format
    '''
    print('.', ' '.join('.' for x in field[0]))
    # for row in field:
        # print('.', '.'.join(row), '.', sep='')
        #Looks bad, is OK 
    for y, row in enumerate(field):
        for x, c in enumerate(row):
            if Grue(x, y) in grues:
                c = 'M'
            print('.', c, sep='', end='')
        print('.')

def main():
    field = mkfield(15)
    grues = [
        (4,4),
        (3,2),
        ]

    showfield(field, grues)    

if __name__ == '__main__':
    main()
