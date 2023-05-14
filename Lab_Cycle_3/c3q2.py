import numpy as np
from random import randint

def pca(a,k):
    #To find the mean
    mean = np.mean(a,axis = 0)
    print("Mean = ",mean)
    a_mean_adjusted = a - mean
    print("Mean adjusted Matrix : ")
    print(a_mean_adjusted)

    #To find the covarience matrix of the mean centered matrix
    cov_matrix =  np.cov(a_mean_adjusted,rowvar=False)
    print("Covarience Matrix : ")
    print(cov_matrix)

    #To Calculate the Eigenvalues and Eigenvectors of the covarience matrix
    eig_values, eig_vectors = np.linalg.eig(cov_matrix)
    print("Eigenvalues : ")
    print(eig_values)
    print("Eigenvectors : ")
    print(eig_vectors)

    #To sort the Eigenvalues and Eigenvectors 
    eig_values_index = eig_values.argsort()[::-1]
    sorted_eig_values = eig_values[eig_values_index]
    sorted_eig_vectors = eig_vectors[:,eig_values_index]

    #To select the first k Eigenvectors, k is the dimensions to which the matix is reduced
    eig_vector_subset = sorted_eig_vectors[:,0:k]

    #To Transform the data
    a_reduced = np.dot(eig_vector_subset.transpose(),a_mean_adjusted.transpose()).transpose()

    #To return the data
    return a_reduced






def main():
    M = np.random.randint(1,10,size=(3,3))
    print("Input Matrix = ")
    print(M)
    n=int(input("Enter the number of dimensions of the matrix to be reduced to : "))
    p=pca(M,n)
    print("PCA Matrix :")
    print(p)


main()