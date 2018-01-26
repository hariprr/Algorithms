import sys
import timeit
import random

counter = 0

class dp:

        def dynamic(self, p, n):
            global counter
            counter += 1
            # this method uses dynamic programming
            # p : list of dimensions of matrices
            # i, j : lowest cost to compute product
            m = [[0 for x in range(n+1)] for x in range(n+1)]
            s = [[0 for x in range(n+1)] for x in range(n+1)]
            q = 0

            # setting diagonal elemets to zero
            for i in range(n+1):
                m[i][i] = 0

            # number of dimensions in p
            # range from 2 - considers only upper elements of the result matrix
            for length in range(2, n+1):
                for i in range(1, n-length+2):
                    j = i+length-1
                    m[i][j] = sys.maxint
                    for k in range(i, j-1+1):
                        q = m[i][k] + m[k+1][j] + (p[i-1]*p[k]*p[j])
                        if (q < m[i][j]):
                            m[i][j] = q
                            s[i][j] = k

            return m[1][n]


def main():

    mm = dp()
    p = [5, 2, 4, 7, 7, 3, 9, 7, 8, 8, 6, 3, 7, 5, 5]
    i = 1
    j = len(p)-1
    start = timeit.default_timer()
    min_value = mm.dynamic(p, j)
    stop = timeit.default_timer()
    print("Run Time : ", stop - start)
    print("Number of Recursive calls: ", counter-1)
    print("Number of scalar multiplications:", min_value)

    for k in range(10):
        p = random.sample(range(1, 100), 10)
        j = len(p)-1
        start = timeit.default_timer()
        min_value = mm.dynamic(p, j)
        stop = timeit.default_timer()
        print stop - start, counter-1, min_value




if __name__ == "__main__": main()
