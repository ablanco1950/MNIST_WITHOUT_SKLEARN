# MNIST_WITHOUT_SKLEARN
The MNIST_Scipy.py module is presented which, using the Scipy library, is applied to the recognition of handwritten characters contained in the MNIST file, achieving a similar hit rate (greater than 97%) than the module referenced at https://github.com/ablanco1950/MNIST_KNN
Although with a longer execution time.

Functioning:

It is required that on disk C: you will find the files:

mnist_train.csv

mnist_test.csv

downloaded from
https://www.kaggle.com/oddrationale/mnist-in-csv

The program is run from Spyder:

MNIST_Scipy.py

The records of the test file can be selected by modifying the parameters ContMaxTest, how many records of the test records 
are tested (on line 8 of the program) and StartTest, beginning record of the test file to be tested, (line 10 of the program)

Also included is the MNIST_Numpy_linalg.py module that makes use of Numpy's linalg method, although with higher execution times-

References:

https://www.kaggle.com/oddrationale/mnist-in-csv

https://stackoverflow.com/questions/1871536/minimum-euclidean-distance-between-points-in-two-different-numpy-arrays-not-wit

https://programmerclick.com/article/87201087090/

https://github.com/ablanco1950/MNIST_KNN
