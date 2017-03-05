def mkfield(n):
    '''
    Makes a square field of size n, returns field
    '''
    row = [' ' for x in range(n)]
    field = [list(row) for x in range(n)]
    return field

def showfield(field):
    '''
    Displays field object in good format
    '''
    for row in field:
        for c in row:
            print(c)

def main():
    field = mkfield(15)
    showfield(field)    

if __name__ == 'main':
    main()
