import numpy

N, M = map(int, raw_input().split())

my_array = numpy.array([ map(int, raw_input().split()) for i in range(N) ])
numpy.set_printoptions(legacy='1.13')
print numpy.mean(my_array, axis = 1)
print numpy.var(my_array, axis = 0)
print numpy.std(my_array, axis = None)