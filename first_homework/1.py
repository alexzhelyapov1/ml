from sklearn import datasets
import pandas as pd

# dataset = datasets.load_digits()
# df = pd.DataFrame(dataset.data)
# print(df.head())

# First 100 images will be used for testing. This dataset is not sorted by the labels, so it's ok
# to do the split this way.
# Please be careful when you split your data into train and test in general.
import numpy as np
# test_border = 100
# X_train, y_train = dataset.data[test_border:], dataset.target[test_border:]
# X_test, y_test = dataset.data[:test_border], dataset.target[:test_border]

# print('Training data shape: ', X_train.shape)
# print('Training labels shape: ', y_train.shape)
# print('Test data shape: ', X_test.shape)
# print('Test labels shape: ', y_test.shape)
# num_test = X_test.shape[0]

a = np.array([[1, 2], [3, 5]])
print(np.sum(a, axis = 1))