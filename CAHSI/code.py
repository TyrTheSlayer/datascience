#CAHSI Datascience Competition
#@authors Aedan Wells, Jennifer Minnich, Otto Strack
#OLD CODE, APPROACH 1 WITHOUT RECURSION. PROPER INPUT WAS CODE_RECURSION.PY
#Date 10/6
import numpy as np

#grab the test and training set
train = np.genfromtxt("D1.csv", delimiter = ',')
testing = np.genfromtxt("D2.csv", delimiter = ',')

#set up a matrix of user mses to find the smallest
dtype = [('mse', float), ('id', int)]
user_mse = np.empty(train.shape[1]-2, dtype=dtype)

#for each user in the data
for user in range(train.shape[1] - 2):
    mse = 0
    #for each book
    for books in range(train.shape[0] - 1):
        #grab both ratings, find the square difference
        score = train[books+1, user+1]
        uy_score = train[books+1, train.shape[1]-1]
        if score != 0:
            mse += pow((score - uy_score), 2)
    #divide by number of books
    mse = mse / (train.shape[0] - 1)
    user_mse[user] = (mse, user)

#sort to find similar people
user_mse = np.sort(user_mse, order='mse')

uy_ratings = np.zeros(testing.shape[0] - 1)

#use x number of similar people to calculate uy's ratings
for books in range(testing.shape[0] - 1):
    rating = 0
    usable_counter = 0
    for i in range(500):
        index = user_mse[i][1]
        if testing[books+1, index] != 0:
            rating += testing[books + 1, index]
            usable_counter += 1
    if usable_counter != 0:
        uy_ratings[books] = round(rating / usable_counter)
    else:
       for i in range(500, 1000):
        index = user_mse[i][1]
        if testing[books+1, index] != 0:
            rating += testing[books + 1, index]
            usable_counter += 1
        if usable_counter != 0:
            uy_ratings[books] = round(rating / usable_counter)
        else:
            for i in range(1000, 1500):
                index = user_mse[i][1]
                if testing[books+1, index] != 0:
                    rating += testing[books + 1, index]
                    usable_counter += 1
                if usable_counter != 0:
                    uy_ratings[books] = round(rating / usable_counter)
                else:
                    uy_ratings[books] = 1

f = open("answer.txt", "x")

for i in uy_ratings:
    f.write(str(int(i)) + "\n")
f.close()
    
