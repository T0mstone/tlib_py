import math
import copy

if __name__ != '__main__':
    print('\x1b[4m\x1b[1;31mWARNING:\x1b[0m\x1b[4m Don\'t import this! '\
    'Use "exec(open(\'path/to/this/tLib/vector.py\').read())".\nUse it in the TOP LEVEL SCRIPT. You don\'t have to import it anywhere else!! :D\x1b[0m')
class DimensionError(Exception):
    """Error for dimensions not fitting in Vectors or matrices etc."""
    def __init__(self, msg=None):
        if msg is None:
            super().__init__()
        else:
            super().__init__(msg)


__builtins__.__dict__['DimensionError'] = DimensionError
del DimensionError


class Vector:
    __arctan__ = copy.copy(math.atan)
    __deg__ = copy.copy(math.degrees)

    def __init__(self, *args):
        newargs = list(args)
        for arg in args:
            if type(arg) is not float:
                valerr = False
                try:
                    f = float(arg)
                    newargs[args.index(arg)] = f
                except ValueError:
                    valerr = True
                finally:
                    if valerr:
                        raise TypeError('%s (argument number %s) is not of type float or int' % (arg, args.index(arg)))
        self.__tuple__ = tuple(newargs)
        if len(self) == 2:
            self.angle = self.angles

    # properties
    def __len__(self):
        return self.__tuple__.__len__()

    def __str__(self):
        if self.__tuple__.__len__() == 0:
            return 'zero-vector'
        def cond(x): return type(x) is float and x.is_integer()

        def item(x): return int(x) if cond(x) else x
        list_ = [item(x) for x in self.__tuple__]
        return 'vector(%s)' % str(list_)[1:-1]

    def __repr__(self):
        return str(self)

    # math
    def mag(self):
        squaresum = sum([pow(x, 2) for x in self.__tuple__])
        return pow(squaresum, 0.5)

    def angles(self):
        vec = type(self)
        if len(self) in (0, 1):
            return ()
        result = []
        for i in range(1, len(self.__tuple__)):
            x1 = self.__tuple__[i - 1]
            x2 = self.__tuple__[i]
            angle = vec.__arctan__(x2 / x1)
            # noinspection PyCallByClass
            result.append(vec.__deg__(angle))
        if len(result) == 1:
            return result[0]
        else:
            return tuple(result)

    def __add__(self, other):
        vec = type(self)
        if self.__tuple__.__len__() != other.__tuple__.__len__():
            raise __builtins__.__dict__['DimensionError']('lengths don\'t match! (%i != %i)' % (len(self), len(other)))
        else:
            result = list(self.__tuple__)
            for i in range(len(self)):
                si = self.__tuple__[i]
                oi = other.__tuple__[i]
                result[i] = si + oi
            return vec(*result)

    def __sub__(self, other):
        vec = type(self)
        return self + vec(*[-x for x in other.__tuple__])

    def __iter__(self):
        return self.__tuple__

    def __mul__(self, other):
        vec = type(self)
        assert type(other) in (int, float), 'scalar has to be a real number!'
        return vec(*[other * x for x in self.__tuple__])


__builtins__.__dict__['vector'] = Vector
del Vector, math, copy
vector.zero_vector = vector()
