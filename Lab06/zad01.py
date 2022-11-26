from inspect import signature


def argumenty(def_val):
    def caller_func(func):
        def get_def(*args):
            args_list = list(args)
            def_no_args = len(list(signature(func).parameters))
            missing = def_no_args - len(list(args))

            if missing > len(def_val):
                raise TypeError(f'{func.__name__} takes exactly {def_no_args} arguments ({len(def_val) + len(args_list)} given)')

            for i in range(missing):
                args_list.append(def_val[i])

            return func(*args_list)
        return get_def
    return caller_func


class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def __init__(self):
        self.change()

    def change(self):
        self.suma = argumenty(self.argumentySuma)(self.calc_sum)
        self.roznica = argumenty(self.argumentyRoznica)(self.calc_subtr)

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        print("%d + %d + %d = %d" % (a, b, c, a + b + c))
        return a + b + c

    def calc_sum(self, a, b, c):
        return a + b + c

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        print("%d - %d = %d" % (x, y, x - y))
        return x - y

    def calc_subtr(self, x, y):
        return x - y

    def __setitem__(self, key, value):
        match key:
            case 'suma':
                self.argumentySuma = value

            case 'roznica':
                self.argumentyRoznica = value

        self.change()
