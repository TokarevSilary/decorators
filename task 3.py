from datetime import datetime
import types

def logger(path):
    def logger_dec(old_function):
        def new_function(*args, **kwargs):
            gen = old_function(*args, **kwargs)
            for result in gen:
                with open(path, "a", encoding="UTF-8") as log:
                    print("args =", args,
                          "kwargs =", kwargs,
                          "result =", result,
                          "time_start =", datetime.now(),
                          "name_function =", old_function.__name__,
                          file=log)
                yield result
        return new_function
    return logger_dec




@logger(path= "generator")
def flat_generator(list_of_lists):
    for x in list_of_lists:
        for y in x:
            yield y

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()