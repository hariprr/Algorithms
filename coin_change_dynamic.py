class CoinChange:

    def NumberofCoins(self,denomination,value):
         #Write your code here to find out minimum number of coins required to provide the change for given value.
         #This method will have a denomination array and an int which specifies the value as inputs(Please see testcase file)
         #This method should return the number of coins

         value_array = []
         denomination_array = []

         print("We have coins of denomination : ", denomination)
         print("Need change for  =", value)

         value_array.insert(0, 0)
         denomination_array.insert(0, 0)
         for i in range(1, value+1):
            value_array.append(value)
            denomination_array.append(-1)
         print(len(value_array), len(denomination_array))
         print(value_array)
         print(denomination_array)

         for j in denomination:
             print("Checking for coin:", j)
             for i in range(1, value+1):
                 # check if 1 cent is not in denomination
                 if( i >= j):
                     if( value_array[i - j] + 1 < value_array[i]):
                         value_array[i] = value_array[i - j] + 1
                         denomination_array[i] = j;
             print(value_array)
             print(denomination_array)
         print(value_array)
         print(denomination_array)

         return value_array[value]

def main():

    print("\n Inside Main\n")
    denomination = [99,1,50]
    value = 99
    cc = CoinChange()

    change = cc.NumberofCoins(denomination,value)
    print("Number of Coins =", change)

if __name__ == "__main__": main()
