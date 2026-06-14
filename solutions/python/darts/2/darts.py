''' This function return the points scored in a single toss of a Dart game.
'''
def score(x_coordinate,y_coordinate):
    ''' The function calculates the different amount of points, depending on where the Dart lands.
    parameter:
        x : The x coordinate of the Dart. Can be int or float.
        y : The y coordinate of the Dart. Can be int or float.
    return (int): Returns the amount of points, depending on the coordinates
                  of the Dart.
                  Inner circle = 10 points
                  Middle circle = 5 points
                  Outer circle = 1 point
                  Outside of the target = 0 points
    '''
    if x_coordinate ** 2 + y_coordinate ** 2 <=1:
        return 10
    if x_coordinate ** 2 + y_coordinate ** 2 <=25:
        return 5
    if x_coordinate ** 2 + y_coordinate ** 2 <=100:
        return 1
    return 0