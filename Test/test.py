 
 
def greet1(name, *args):
    string = ""
    length = len(args)
    for n in (name,) + args:
        string = string + n
        if args:
            if length > 0:
                string = string + " and "
                length -= 1
    print(string.join(['Hello, ', '!']))
    
    

def greet(who, *args):
    names = ' and '.join((who,) + args)
    print('Hello, {}!'.format(names))


greet('Bob')
greet('Moe', 'Mary')
greet1(*'ABC')
