import sys
import timeit
import random

counter = 0


class Memoization:

    def lookup_result(self, p, i, j):
        global counter
        counter += 1
        # returns the value of m[i][j] is present
        # otherwise returns sys.maxint
        m = [[sys.maxint for x in range(j+1)] for x in range(j+1)]
        if( m[i][j] < sys.maxint ): return m[i][j]

        if( i == j ): m[i][j] = 0
        else:
            for k in range(i,j):
                q = self.lookup_result(p, i, k) + self.lookup_result(p, k+1, j) + (p[i-1] * p[k] * p[j])
                if( q < m[i][j]):
                    m[i][j] = q

        return m[i][j]



    def memoized(self, p, i, j):
        # This method used
        # p : list of dimension of matrices
        # i, j : lowest cost to compute product

        m = [[sys.maxint for x in range(j+1)] for x in range(j+1)]
        return self.lookup_result(p, i, j)


def main():

    mm = Memoization()
    p = [5, 2, 4, 7, 7, 3, 9, 7, 8, 8, 6, 3, 7, 5, 5]
    i = 1
    j = len(p)-1
    start = timeit.default_timer()
    min_value = mm.memoized(p, i, j)
    stop = timeit.default_timer()
    print("Run Time : ", stop - start)
    print("Number of Recursive calls: ", counter-1)
    print("Number of scalar multiplications:", min_value)
    print "\n \n"

    for k in range(10):
        p = random.sample(range(1, 100), 10)
        j = len(p)-1
        start = timeit.default_timer()
        min_value = mm.memoized(p, i, j)
        stop = timeit.default_timer()
        print stop - start, counter-1, min_value


if __name__ == "__main__": main()
