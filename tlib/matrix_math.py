from tools import custom_error, index_tuples
from copy import copy


class Matrix:
    def __init__(self, array_2d):
        lens = [len(row) for row in array_2d]
        len_comparisons = [rowlen == lens[0] for rowlen in lens]
        if False in len_comparisons:
            # one of the rows has a different length than the others
            custom_error(
                'DimensionError',
                self + " has to have a uniform number of columns")
        self.content_array = array_2d

    def __repr__(self):
        # number of decimal places to round to
        round_decimals = 3

        rounded = [
         [round(x, round_decimals) for x in row] for row in self.content_array]
        strs = [str(row) for row in rounded]
        joined = '\n'.join(strs)

        return 'Matrix[' + joined + ']'

    def __iter__(self):
        return iter(self.content_array)

    def transposed(self):
        new_mat_arr = list(zip(*self.content_array))
        return Matrix(new_mat_arr)

    def dimensions(self):
        dimy = len(self.content_array)
        dimx = len(self.content_array[0])
        return dimx, dimy

    def __mul__(self, other):
        if type(other) in [int, float]:
            new_content_array = copy(self.content_array)
            for y in range(len(self.content_array)):
                curr_y = self.content_array[y]
                for x in range(len(curr_y)):
                    new_content_array[y][x] = other * self.content_array[y][x]
            typ = type(self)
            if typ is Vector:
                single_values = [x[0] for x in new_content_array]
                return typ(*single_values)
            else:
                return typ(new_content_array)
        elif type(other) in [Matrix, Vector]:
            sum_2d = []
            for row, curr_row_here in index_tuples(self.content_array):
                tp = other.transposed()
                sum_row = []
                for col, curr_col_there in index_tuples(tp.content_array):
                    if len(curr_row_here) != len(curr_col_there):
                        err_msg = f"{self} has dimensions " +\
                            f"{self.dimensions()} while {other} has" +\
                            f" dimensions {other.dimensions()}"
                        custom_error('DimensionError', err_msg)
                    muls = []
                    for i in range(len(curr_row_here)):
                        mul = curr_row_here[i] * curr_col_there[i]
                        muls.append(mul)
                    sum_row.append(sum(muls))
                sum_2d.append(sum_row)
            return Matrix(sum_2d)
        else:
            raise TypeError(
                    'Unknown type for matrix multiplication:', type(other))

    def __add__(self, other):
        if type(other) in [Matrix, Vector]:
            if self.dimensions() != other.dimensions():
                err_msg = f"{self} has dimensions " +\
                    f"{self.dimensions()} while {other} has" +\
                    f" dimensions {other.dimensions()}"
                custom_error('DimensionError', err_msg)
            new_arr_2d = []
            for row in range(len(self.content_array)):
                curr_row = []
                for col in range(len(self.content_array[row])):
                    self_i = self.content_array[row][col]
                    other_i = other.content_array[row][col]
                    curr_row.append(self_i + other_i)
                new_arr_2d.append(curr_row)
            return Matrix(new_arr_2d)


class Vector(Matrix):
    def __init__(self, *args):
        if type(args[0]) in [Matrix, Vector]:
            in_rows = args[0].content_array
        else:
            in_rows = [[x] for x in args]
        super().__init__(in_rows)

    def __repr__(self):
        ret = 'Vector('
        first = True
        for row in self.content_array:
            rrow = [round(x, 10) for x in row]
            if first:
                ret += str(rrow[0])
                first = False
            else:
                ret += ', ' + str(rrow[0])
        ret += ')'
        return ret

    def dot(self, other):
        tp = self.transposed()
        return tp * other

    def __iter__(self):
        return iter(x[0] for x in self.content_array)
