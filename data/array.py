# -*- coding=utf-8 -*-

import operator

## Returns a tuple of tuples instead of a list of tuples
## just to reduce parenthesis usage
def tupled_zip(rhs, lhs):
    return tuple(zip(rhs.tuple(), lhs.tuple()))

## An array class with common behaviour for deriving vectors, quaternions. etc.
class Array(object):
    def __init__(self):
        pass

    ## MUST BE OVERRIDEN. Returns a tuple representation of the object.
    def tuple(self):
        return ()

    ## Applies a function to each element
    #  @param fn function :: a -> a
    def apply(self, fn):
        return self.__class__(*map(fn, self.tuple()))

    ## Merges objects <obj1> and <obj2> applying a function <fn>
    #  @param obj1 An object
    #  @param obj2 Another object
    #  @param fn function :: (a, a) -> a
    #  @return Merged object
    @staticmethod
    def merge(obj1, obj2, fn):
        if obj1.__class__ != obj2.__class__:
            raise ValueError('obj1 and obj2 must be instances of the same class')
        return obj1.__class__(
            *map(lambda p: fn(p[0], p[1]), tupled_zip(obj1, obj2))
        )

    ## Binary operator +. Sums the elements of each object.
    def __add__(self, other):
        return self.__class__.merge(self, other, operator.add)

    ## Binary operator -. Substracts the elements of each object.
    def __sub__(self, other):
        return self.__class__.merge(self, other, operator.sub)

    ## Unary operator -. Negates the elements of the object.
    def __neg__(self):
        return self.apply(operator.neg)

    ## Binary operator *. Multiplies each element by the value <value>.
    def __mul__(self, value):
        return self.apply(lambda x: value*x)

    ## Binary operator *. Reverse-multiplies each element by the value <value>.
    def __rmul__(self, value):
        return self*value

    ## Called by str(<obj>). String representation of the object.
    def __str__(self):
        return str(self.tuple())

    def __repr__(self):
        return str(self)

    ## Called by abs(<obj>). Returns the length in a cartesian basis.
    def __abs__(self):
        return self.length()

    ## Returns the length of the object in a cartesian basis
    def length(self):
        return (reduce(operator.add, self.apply(lambda x: x**2).tuple()))**0.5

    ## Returns the object of length 1 and same direction as the original.
    def unit(self):
        return 1./self.length()*self
