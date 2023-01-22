class TinyStatistician:
    def __init__(self):
        pass
    
    def mean(self, x):
        '''Computes the mean of a given non-empty list or array x, using a for-loop.
        The method returns the mean as a float, otherwise None if x is an empty list or
        array.'''
        if len(x) == 0:
            return None
        return sum(x) / len(x)

    def median(self, x):
        '''Computes the median of a given non-empty list or array x. The method
        returns the median as a float, otherwise None if x is an empty list or array.'''
        if len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 == 0:
            return (float(x[int(len(x) / 2)]) + float(x[int(len(x) / 2) - 1])) / 2
        else:
            return float(x[int(len(x) / 2)])

    def quartile(self, x):
        '''Computes the 1st and 3rd quartiles of a given non-empty array x.
        The method returns the quartile as a float, otherwise None if x is an empty list or
        array.'''
        x.sort()
        return ([self.median(x[1:len(x) // 2]), self.median(x[len(x) // 2:])])

    def var(self, x):
        '''Computes the variance of a given non-empty list or array x, using a for-
        loop. The method returns the variance as a float, otherwise None if x is
        an empty list or array.'''
        # the variance is the average of each point from the mean squared
        if len(x) == 0:
            return None
        mean = self.mean(x)
        return sum([(i - mean) ** 2 for i in x]) / len(x)

    def std(self, x):
        '''Computes the standard deviation of a given non-empty list or array x,
        using a for-loop. The method returns the standard deviation as a float, otherwise
        None if x is an empty list or array.'''
        if len(x) == 0:
            return None
        return self.var(x) ** 0.5