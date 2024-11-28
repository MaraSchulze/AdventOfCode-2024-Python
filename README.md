# 🎁 Advent of Code 2024 in Python 🎄

## What is the Advent of Code?
The Advent of Code are competitve programming tasks that are every year published in the month of December by Eric Wastl (topaz).  
For 25 days every day 2 problems appear: One immediately, the other is being unlocked after solving the first one correctly. Thus all in all 50 problems are available. For every solved problem you get a gold star.  
You habe the chance to appear on the leaderboard if you have enough points: You get points if you are under the first 100 to solve the problem, the first gets 100, the second 99 and so on.  
A problem is unlocked at UTC-5 midnight.  

## More
Every user has his/her own imput!  
You can see your own stats at https://adventofcode.com/2023/leaderboard/self.  

## 2024 Edition
The problem description of the 2024 problems:  
https://adventofcode.com/2024

## AoC Website
https://adventofcode.com

## Structure
Directories are inputs and riddles.  
The input of day n is a text file with the name "n".  
The 2 riddles of day n are in the python scripts __"dayn.1.py"__ and __"dayn.2.py"__  
There is no main function in the scripts.  
The script reads in the input data with the imported function get_input(\_\_file__), which determines the right input file from the file name. The input is a list of strings (the lines). Very often the input must be further massaged.  

## Usage
```
cd riddles
python3 <script>
```

