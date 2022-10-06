#CAHSI Datascience Competition
#@authors Aedan Wells, Jennifer Minnich, Otto Strack
#Date 10/6
import numpy as np
import math

#recursively go through each user, picking the best user in similarity each time
#i is the user index
#books is the book index
#user_mse is the user_mse similarity value
#testing is the testing dataset
#returns the rating for the book that is closest
def recursive(i, books, user_mse, testing):
    rating = 0
    usable_counter = 0
    value = 0
    #for a set of 5 most similar users
    for j in range(i, i+5):
        index = user_mse[j][1]
        #if the testing value is not 0, add it to the overall rating
        if testing[books+1, index] != 0:
            rating += testing[books + 1, index]
            usable_counter += 1
    #if there is a usable user, return the average rounded
    if usable_counter != 0:
        return round(rating / usable_counter)
    #else if out of people, return 1
    elif i > 5000:
        return 1
    else:
        #else, rerun it with the next best 5 users.
        value = recursive(i+5, books, user_mse, testing)
    return value

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
    mse = math.sqrt(mse / (train.shape[0] - 1))
    user_mse[user] = (mse, user)

#sort to find similar people
user_mse = np.sort(user_mse, order='mse')

uy_ratings = np.zeros(testing.shape[0] - 1)

#use x number of similar people to calculate uy's ratings
for books in range(testing.shape[0] - 1):
    uy_ratings[books] = recursive(1, books, user_mse,testing)

f = open("answer.txt", "x")

#write to answer file
for i in uy_ratings:
    f.write(str(int(i)) + "\n")
f.close()
    
