from .no_imports.tools import custom_error, index_tuples


class Matrix:
    __MAT_TYPE__ = 'Matrix'

    def mulsum(self, other, row: tuple, col: tuple):
        if len(row) != len(col):
            self.__dimension_error__(other, 'matrix multiplication')
        muls = [row[i] * col[i] for i in range(len(row))]
        return sum(muls)

    def __init__(self, array_2d):
        lens = tuple(len(row) for row in array_2d)
        len_comparisons = tuple(rowlen == lens[0] for rowlen in lens)
        if False in len_comparisons:
            # one of the rows has a different length than the others
            custom_error(
                'DimensionError',
                self + " has to have a uniform number of columns")
        tups = [tuple(row) for row in array_2d]
        self.content_tuple = tuple(tups)

    def __repr__(self):
        # number of decimal places to round to
        round_decimals = 3

        rounded = [
         [round(x, round_decimals) for x in row] for row in self.content_tuple]
        strs = [str(row) for row in rounded]
        joined = '\n'.join(strs)

        return 'Matrix(' + joined + ')'

    def __iter__(self):
        return iter(self.content_tuple)

    def transposed(self):
        new_mat_arr = list(zip(*self.content_tuple))
        return Matrix(new_mat_arr)

    def dimensions(self):
        dimy = len(self.content_tuple)
        dimx = len(self.content_tuple[0])
        return dimx, dimy

    def __dimension_error__(self, other, desc_str):
        sd, od = self.dimensions(), other.dimensions()
        msg = f"unmatching matrix dimensions {sd} and {od} for operation: "
        custom_error('DimensionError', msg + desc_str)

    def __mul__(self, other):
        # other is matrix or vector
        if hasattr(other, '__MAT_TYPE__'):
            global mulsum
            # transpose because that switches rows with cols and we do col*row
            tp = other.transposed()
            new_array_2d = []
            # multiply elementwise, row * col
            for row_i, row in index_tuples(self.content_tuple):
                ct = tp.content_tuple
                new_row = tuple(
                    self.mulsum(other, row, other_col)
                    for other_col in ct)
                new_array_2d.append(new_row)
            return Matrix(new_array_2d)
        # other is scalar
        elif type(other) in [int, float]:
            # multipy every element by that scalar
            new_carray = [
                [item * other for item in row] for row in self.content_tuple]
            new_ct = tuple(tuple(row) for row in new_carray)
            return Matrix(new_ct)
        else:
            raise TypeError(
                    'Unknown type for matrix multiplication:', type(other))

    def __add__(self, other):
        if hasattr(other, '__MAT_TYPE__'):

            s_ct = self.content_tuple
            o_ct = other.content_tuple

            arr = [
                [s_ct[y][x] + o_ct[y][x] for x, col in index_tuples(row)]
                for y, row in index_tuples(s_ct)]
            return Matrix(arr)


class Vector(Matrix):
    __MAT_TYPE__ = 'Vector'

    def __init__(self, *args):
        # input is a matrix or vector
        if hasattr(args[0], '__MAT_TYPE__'):
            # just copy content array
            cont_arr = args[0].content_tuple
        # input are 1+ numbers as *args
        else:
            # create 1*n matrix
            cont_arr = [[x] for x in args]
        super().__init__(cont_arr)

    def __repr__(self):
        # number of decimal places to round to
        round_decimals = 3

        rounded = [
         [round(x, round_decimals) for x in row] for row in self.content_tuple]
        strs = [str(row[0]) for row in rounded]
        joined = '\n'.join(strs)

        return 'Vector(' + joined + ')'

    def dot(self, other):
        tp = self.transposed()
        return tp * other

    def __iter__(self):
        return iter(x[0] for x in self.content_tuple)
