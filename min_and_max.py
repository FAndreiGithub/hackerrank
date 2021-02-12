import numpy

N, M = map(int, raw_input().split())

my_array = numpy.array([ map(int, raw_input().split()) for i in range(N) ])

print numpy.max(numpy.min(my_array, axis = 1))
