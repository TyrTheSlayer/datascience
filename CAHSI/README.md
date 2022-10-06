CAHSI Data Analytics challenge
Team: NMT Space Miners
Members: Jennifer Minnich, Otto Strack, Aedan Wells
Date: 10/06/2022

See code_recursion.py for the most accurate predictive algorithm. We used an user-user 
collab filtering method that found the best users via RMSE and then chose the book values
for the most similar user. Then, went through each group of best-similar-users and predicted
their average score.

To run, just run code_recursion.py with python3.

In our submission, we included our first approach which was iterative and resulted
in a 2.6 MSE. Our above version is 2.0266