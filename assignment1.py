from statistics import stdev
import os.path
from os import path



## global variables ##

nums = []
counter = 1
sum = 0
Avg = 0

#### Function to sum user numbers ####

def sumNumbers(arr):
    global sum
    for i in arr:
        sum += i
    return sum

##### Function to create an array of user numbers #############

def createInputArray():
    global counter
    global nums
    while(counter <= 10):
        inputNum = int(input("Enter number --- %d " %counter ))
        nums.append(inputNum)
        counter += 1
    sumNumbers(nums)

#### Funtion to calculate the average ####

def Average(sum, arr):
    global Avg
    Avg = sum/len(arr)
    return Avg

### Function to create/write/apppend file with user numbers ####
def createFile(numsArr, s, fileName):
    if(path.exists(fileName)):
        f1 = open(fileName, "a")
        f1.write("\n \n ########################## \n \n")
    else:
        f1 = open(fileName, "w")
    for i in numsArr:
        f1.write(str(i))
        f1.write("\n")
    f1.write("Average: ")
    f1.write(str(round(Average(s, numsArr),1)))
    f1.write(" Standard Dev: ")
    f1.write(str(round(stdev(numsArr), 1)))




### main program ###

createInputArray()
FName = str(input("Enter name of File to be created ---- with format extension (File.txt)"))
createFile(nums, sum, FName)





