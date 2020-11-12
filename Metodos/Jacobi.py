import math
import numpy as np
def Jacobi(A, b, t, iter, x0):
    n = len(A)
    l = len(A[0])
    if (n!=l):
        print("A is not a square matrix please check and run again.")
    else:
        x =[None] * n
        aux=0
        cont = 0
        error = t + 1
        iteration = 1
        T = np.zeros((n, n))
        C = np.zeros(n)
 
        while(error > t and cont <= iter):
            print("")
            print("iteration:# " + str(iteration))
            error = 0
            for i in range(0,n):
                sum = 0
                for j in range(0,n):
                    if (i != j):
                        sum = sum + A[i][j] * x0[j]
                        T[i][j] = -A[i][j] / A[i][i]
                        C[i] = b[i] / A[i][i]
                        
                        
                    
                x[i] = (b[i] - sum) / A[i][i]
                aux = x[i] - x0[i]
                error = error + math.pow(aux, 2)
               
            error = math.pow(error, 0.5)

            print("error abs = " + str(error))

            for i in range(0,n):
                x0[i] = x[i]
                print("x"+str(i+1)+": "+str(round(x0[i],4)))
                    
                


            iteration=iteration+1
            cont = cont+1
            
        print("")
        print("T: \n"+str(T))
        print("")
        print("C: \n"+str(C))
        print("")
        spectralRadius = np.amax(abs(T))
        print("Spectral radius: \n"+str(spectralRadius))   

        if (error < t):
            return x
        else:
            print ("no solution reached in" + str (iter) + "iterations")
            return        
    
    
    
if __name__ == "__main__":
    A= [[4, -1, 0,3],
        [1, 15.5, 3, 8],
        [0, -1.3, -4, 1.1],
        [14, 5, -2, 30]]

    b = [1,1,1,1]
    x0 = [0, 0, 0,0]
        
    Jacobi(A,b,math.pow(10,-7),100,x0)
    