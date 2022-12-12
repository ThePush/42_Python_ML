import numbers


class Vector:
    def __init__(self, values):
        try:
            self.values = []
            self.shape = ()
            if isinstance(values, int):
                if values < 1:
                    raise Exception('Vector.__init__ invalid int range')
                for i in range(values):
                    self.values.append([float(i)])
            elif isinstance(values, tuple):
                if not all(isinstance(x, int) for x in values) or type(values[0]) != type(values[1]) or values[0] >= values[1] or len(values) != 2:
                    raise Exception('Vector.__init__ invalid tuple range')
                for i in range(values[1]-values[0]):
                    self.values.append([float(values[0]+i)])
            elif isinstance(values, list):
                if not all(isinstance(x, list) for x in values) or not all(isinstance(y, float) for x in values for y in x):
                    raise Exception('Vector.__init__ invalid list type')
                if len(values) > 1:
                    for row in values:
                        if len(row) != 1:
                            raise Exception(
                                'Vector.__init__ invalid list size')
                self.values = values
            else:
                raise Exception('Vector.__init__ invalid type')
            self.shape = (len(self.values), len(self.values[0]))
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def T(self):
        try:
            return Vector([[row[i] for row in self.values] for i in range(len(self.values[0]))])
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def dot(self, other):
        try:
            if self.shape != other.shape:
                raise Exception('dot() different sizes of vector')
            return sum([rowself[i]*rowother[i] for (rowself, rowother) in zip(self.values, other.values) for i in range(len(rowself))])
            #result = 0
            # for (rowself, rowother) in zip(self.values, other.values):
            #    for i in range(len(rowself)):
            #        result = result + (rowself[i]*rowother[i])
            # return result
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def __add__(self, other):
        try:
            if self.shape != other.shape:
                raise Exception('__add__ different sizes of vector')
            return Vector([[rowself[i] + rowother[i] for i in range(len(rowself))] for (rowself, rowother) in zip(self.values, other.values)])
            # for (rowself, rowother) in zip(self.values, other.values):
            #    for i in range(len(rowself)):
            #        rowself[i] += rowother[i]
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other.__mul__(-1))

    def __rsub__(self, other):
        return other.__sub__(self)

    def __truediv__(self, num):
        try:
            if not isinstance(num, numbers.Number):
                raise NotImplementedError('Vector.__truediv__ not a scalar')
            if num == 0:
                raise ZeroDivisionError(
                    'Vector.__truediv__ division by zero')
            # return Vector([[values / num for values in row] for row in self.values])
            return self.__mul__(1/num)
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def __rtruediv__(self, num):
        try:
            raise NotImplementedError(
                'Vector.__rtruediv__ Division of a scalar by a Vector is not defined here.')
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def __mul__(self, num):
        try:
            if not isinstance(num, numbers.Number):
                raise NotImplementedError('Vector.__mul__ not a scalar\n')
            return Vector([[num * values for values in row] for row in self.values])
            # for row in self.values:
            #    for i in range(len(row)):
            #        row[i] = num * row[i]
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
            return

    def __rmul__(self, num):
        return self.__mul__(num)

    def __eq__(self, other):
        return self.shape == other.shape and self.values == other.values

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)

# https://www.studygate.com/blog/wp-content/uploads/2017/11/Matrix-Multiplication-dot-product.png
# https://www.calculatorsoup.com/calculators/algebra/dot-product-calculator.php
# https://datahacker.rs/dot-product-inner-product/
