from math import sqrt
class Point():
    '''A class for points in Cartesian coordinate systems.'''
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
    def __getitem__(self, i): # return x or y of a point
        if i==0: return self.x
        if i==1: return self.y
        return None
    def __len__(self): #the number of dimensions in the point
        return 2
    def __eq__(self, other):# if two point are the same
        if isinstance(other, Point): #check other if a instance of Point
            return self.x==other.x and self.y==other.y # then check are they the same
        return NotImplemented
    def __ne__(self, other): # if two point are different
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    def __lt__(self, other): # if p1 <= p2
        if isinstance(other, Point):
            if self.x<other.x:
                return True
            elif self.x==other.x and self.y<other.y:
                return True
            return False
        return NotImplemented
    def __gt__(self, other): # if p1 > p2
        if isinstance(other, Point):
            if self.x>other.x:
                return True
            elif self.x==other.x and self.y>other.y:
                return True
            return False
        return NotImplemented
    def __ge__(self, other): # if p1 > p2
        if isinstance(other, Point):
            if self > other or self == other:
                return True
            else:
                return False
            return False
    def distance(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)