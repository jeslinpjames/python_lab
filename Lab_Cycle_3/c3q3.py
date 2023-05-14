import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


iris = pd.read_csv('D:/git/python_lab/Lab_Cycle_3/iris.csv')


def freqency_species():
    num = iris['Species'].value_counts()
    num.plot.bar(color=['red','Blue','yellow'])
    plt.title('Frequency Graph')
    plt.xlabel('Species')
    plt.ylabel('Frequency')
    plt.show()
    

def pca_components():
    X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
    pca = PCA(n_components=2)
    components = pca.fit_transform(X)
    principalDf = pd.DataFrame(data=components,columns=['principal component 1','principal component 2'])
    finalDf = pd.concat([principalDf,iris[['Species']]],axis = 1)
    # finalDf.head()
    fig = plt.figure(figsize = (10,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('First Principle Component')
    ax.set_ylabel('Second Principal Component')
    ax.set_title('PCA Graph')
    targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    colors = ['r', 'g', 'b']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf['Species'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
    ax.legend(targets)
    plt.show()


def histogram():
    iris['SepalLengthCm'].plot(kind='hist')
    plt.title('Sepal Length Histogram')
    plt.xlabel('Sepal Length')
    plt.ylabel('Distribution')
    plt.show()
    iris['SepalWidthCm'].plot(kind='hist')
    plt.title('Sepal Width Histogram')
    plt.xlabel('Sepal Width')
    plt.ylabel('Distribution')
    plt.show()
    iris['PetalLengthCm'].plot(kind='hist')
    plt.title('Petal Length Histogram')
    plt.xlabel('Petal Length')
    plt.ylabel('Distribution')
    plt.show()
    iris['PetalWidthCm'].plot(kind='hist')
    plt.title('Petal Width Histogram')
    plt.xlabel('Petal Width')
    plt.ylabel('Distribution')
    plt.show()






freqency_species()
pca_components()
histogram()