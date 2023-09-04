import csv
import time as t
ti = t.time()
import math as m
import string

csv_file = 'numcombos.csv'

rules = "RULES: The product of 2 numbers is a number that contains every digit from both multiplied factors the same number of times. Also, every digit in the product number must appear he same number of times that it did between the two given factors. EXCEPTIONS: Neither factor can be 0, 1, or be divisible by 10."

end = 1000
start = 0
lim = end + 1 - start
totaltested = round((lim+(lim**2))*0.5, 0)

estTime = totaltested*3.96464*(10**(-5))
print(rules + "\n\nWorking Combos:" + "\nLoading... Please Wait... Estimated Time: " + str(round(estTime)) + " seconds", end = "\r")


totalworking = 0
ff = []
#number of times each digit appears in x 
def test_n(n):
  xn = x.count(str(n))
  yn = y.count(str(n))
  an = a.count(str(n))
  global qn
  qn = an - xn - yn


#tests different integers and finds product

for j in range(lim):
  x = j + start

  if(x != 0 and x != 1 and (not (x * 0.1).is_integer())):
    x = str(x)
    for i in range(int(x) - 1):
      y = int(i+2)
      if(not (y * 0.1).is_integer()):
   
        y = str(y)
        a = str(int(x) * int(y))
  
        qn = 0
        for k in range(10):
          if(qn == 0):
            test_n(k)
          else:
            break
        if(qn == 0):
           ff.append(int(x))
           ff.append(int(y))
           ff.append(int(a))
           totalworking = totalworking + 1
           

#prints final list
fff = []
for g in range(totalworking):
  d =  g * 3
  #print(ff[d:d+3])
  fff.append(ff[d:d+3])
  print(str(fff[g]))

#results
tf = t.time()
dt = round(tf-ti, 3)
print("\nTime elapsed: " + str(dt) + " seconds")
print("Total Combos Working: " + str(totalworking))
print("Total Combos Tested: " + str(totaltested))
print("Success Rate: " + str(round((100*totalworking/totaltested), 5))+"%")

length = len(fff)

def writeCombo(n):
  global fff
  combo = fff[n]
  writer.writerow([str(n+1),combo[0], combo[1], combo[2]])

with open(csv_file, 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["","x", "y", "Product"])
  for i in range(length):  
    writeCombo(i)
    
