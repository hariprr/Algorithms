#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class MatrixMultiplication:
    def __init__(self,cnter):
        self.counter=cnter

    def Call_multiplier(self,matrice,power):
        #Write your code here to call Multiply_matrices lg(power) times.
        #This method will have the 2-dimensional array and a number which specifies the power as inputs(Please see testcase file)
        #This method should return the final matrice
		
	# get the dimension of input sqaure matrix
        dimen = len(matrice)

	# check if power is 1, no need to proceed is true
        if power == 1:
            return matrice

	# Initialize a temp matrix = identity matrix
        temp = [[1 if i==j else 0 for j in range(len(matrice))] for i in range(len(matrice))]
        #print temp

	# Iteratively multiply the input matrix lg(power) times in a loop
        while power > 1:
            # checking if power is even
            if power % 2 == 0: 
                matrice = self.Multiply_matrices(matrice, matrice)
                power = power / 2
            # when power is odd
            else:
                temp = self.Multiply_matrices(matrice, temp)
                matrice = self.Multiply_matrices(matrice, matrice)
                power = (power - 1) / 2
        # one extra multiplication for odd powers
        return self.Multiply_matrices(matrice, temp)

    def Multiply_matrices(self,a,b):
        self.counter +=1
        #Write code here to multiply 2 matrices and return the resultant matrice

        # Initialize a product matrix = zero matrix
        prod = [[0 if i==j else 0 for j in range(len(a))] for i in range(len(a))]
	#print len(a), len(b), len(prod)

        # 		
        for i in range(len(a)):
            for j in range(len(a)):     #using same len since matrix is a square matrix
                for k in range(len(a)): #rows of b matrix = matrix a dimensions 
                    #print i,j,k
                    prod[i][j] += a[i][k] * b[k][j]
        return prod
	


