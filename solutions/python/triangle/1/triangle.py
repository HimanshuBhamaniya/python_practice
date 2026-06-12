def equilateral(sides):
    while sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        for side in sides:
            if side <= 0:
                return False
        if sides[0] == sides[1] == sides[2]:
            return True
        return False
    return False


def isosceles(sides):
    while sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        for side in sides:
            if side <= 0:
                return False
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
        
        return False
    return False


def scalene(sides):
    while sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        for side in sides:
            if side <= 0:
                return False
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return False
        return True
    return False
