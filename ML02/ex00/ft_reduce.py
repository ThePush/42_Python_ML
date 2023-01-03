def ft_reduce(function_to_apply, iterable):
    '''Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    '''
    if not hasattr(iterable, '__iter__'):
        return None
    if not hasattr(function_to_apply, '__call__'):
        return None
    if len(iterable) == 0:
        return None
    if len(iterable) == 1:
        return iterable[0]
    result = iterable[0]
    for i in iterable[1:]:
        result = function_to_apply(result, i)
    return result

# https://www.geeksforgeeks.org/reduce-in-python/
