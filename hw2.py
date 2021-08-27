#hw2.py
#Jackie Prescott



def forLoops():
    '''for loops within a range, numbers within that range will print'''
    for num in range(5,25,4):
        print(num)



def pay(rate,hours):
    '''Input hourly rate and hours worked, outputs total pay'''
    if hours<=40:
        return (rate*hours)
    else:
        return ((rate*40)+(rate*1.5)*(hours-40))



def abbreviation(dayofweek):
    '''if day of the week is entered, the abbreviation is given'''
    if dayofweek =='Sunday':
        return ('Su')
    elif dayofweek == 'Monday':
        return ('Mo')
    elif dayofweek == 'Tuesday':
        return ('Tu')
    elif dayofweek == 'Wednesday':
        return ('We')
    elif dayofweek== 'Thursday':
        return ('Th')
    elif dayofweek== 'Friday':
        return ('Fr')
    else:
        return ('Sa')



import math
def collision(x1,y1,r1,x2,y2,r2):
    '''Given the coordinates and radi of two circles, if the circles collide, the function will return True but if the circles do not, the function will return False'''
    CC=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if (r1+r2) >= CC:
        return(True)
    else:
        return(False)



def partition(lst):
    '''A list of names are entered and only those that begin with the letters A through M are printed'''
    for firstname in lst:
        if firstname[0] in 'ABCDEFGHIJKLM':
            print(firstname)



def lastF(firstname,lastname):
    '''Takes fullname strings and returns Last Name, First Initial'''
    return lastname+ ', ' + firstname[0] + '.'


if __name__ == '__main__':
    import doctest
    print( doctest.testfile('hw2TEST.py'))

