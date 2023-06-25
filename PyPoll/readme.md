Python-Challenge - PyPoll

Tasks
=====
1. Collect the total no. of votes cast
2. Collect the candidates who received votes
3. Calculate the percentage of votes for each candidate
4. Calculate the total number of votes each candidate won
5. Find the winner of the popular vote
6. Print the analysis in terminal
7. Export a text file with analysis


Overview
========
1. Used a for loop and the += to assign the value
2. Used if/else conditional statement within the for loop to identify the candidates who received votes
3. 
    - Used another for loop to iterate through the candidate list
    - used .items to identify candidate name and their number of votes
    - within the print statement
        - printed each candidates name
        - used the print percentage format specifier and calculated each candidates vote percentage
        - used a string to print each candidates number of votes
4. (see above)
5. created a new variable to identify the winning candidate by using the max function
6. Used print statements along with f' to successfully print the results within the terminal
7. Created a new path within the analysis folder and created a text file to successfully output the printed results 


Used the following links for reference and help:

*Please also note I used several of the references that were listed in the previous PyBank assignment*

.items functionality-
https://realpython.com/iterate-through-dictionary-python/#iterating-through-items

percentage-
https://www.askpython.com/python/string/print-format-3f#:~:text=In%20Python%2C%20the%20%E2%80%9C%25.,the%20number%20of%20decimal%20places.
