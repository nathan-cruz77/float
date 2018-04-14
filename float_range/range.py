

class FloatRange:

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = 0
        else:
            self.start = start
            self.stop = stop

        self.step = step
        self.precision = FloatRange._precision(step)

    def __iter__(self):
        return self

    def __next__(self):
        if self._isEmpty():
            raise StopIteration

        res = round(self.start, self.precision)
        self.start += self.step
        return res

    def next(self):
        return self.__next__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        aux = ', '.join(str(x) for x in [self.start, self.stop, self.step])
        return '{0}({1})'.format(self.__class__.__name__, aux)

    def __contains__(self, item):
        if self._isEmpty():
            return False
        return True

    @staticmethod
    def _precision(number):
        try:
            number = float(number)
            decimal_part = str(number).split('.')[1]
        except (ValueError, TypeError, IndexError):
            msg = 'Cannot determine precision. \"{}\" is not a valid float'
            raise ValueError(msg.format(number))

        if decimal_part == '0':
            return 1
        else:
            return len(decimal_part)

    def _isEmpty(self):
        return ((self.start >= self.stop and self.step > 0)
                or (self.start <= self.stop and self.step < 0))


def range(start, stop=None, step=1):
    return FloatRange(start, stop, step)
