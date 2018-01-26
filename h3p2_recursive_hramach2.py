import sys
import timeit
import random

counter = 0

class Recursion:

    def recursive(self, p, i, j):
        global counter
        counter += 1
        # this method uses recursion
        # p : list of dimension of matrices
        # i, j : lowest cost to compute product

        if(i==j):
            #print("i == j ! Returning 0")
            return 0

        m = sys.maxint
        q = 0

        #print("m =", m)
        #print("p =", p)

        for k in range(i,j):
            #print("i =", i, "k +1 =", k+1 , "j =", j)
            q = self.recursive(p, i, k) + self.recursive(p, k+1, j) + ((p[i-1]) * p[k] * p[j])
            #print("After recursive call ")
            #print("q = ", q, "j =", j)
            if( q < m):
                m = q
        #print("Recursive: ", q)
        return q


def main():

    mm = Recursion()
    p = [5, 2, 4, 7, 7, 3, 9, 7, 8, 8, 6, 3, 7, 5, 5]
    i = 1
    j = len(p)-1
    start = timeit.default_timer()
    min_value = mm.recursive(p, i, j)
    stop = timeit.default_timer()
    print("Run Time : ", stop - start)
    print("Number of Recursive calls: ", counter-1)
    print("Number of scalar multiplications:", min_value)
    print "\n\n"

    for k in range(10):
        p = random.sample(range(1, 100), 10)
        j = len(p)-1
        start = timeit.default_timer()
        min_value = mm.recursive(p, i, j)
        stop = timeit.default_timer()
        print stop - start, counter-1, min_value


if __name__ == "__main__": main()
