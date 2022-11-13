import pprint

# TODO решить с помощью list comprehension и распечатать его

dict_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(dict_)

