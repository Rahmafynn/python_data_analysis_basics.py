import matplotlib.pyplot as plt ## using the mathplotlib for data visualisation

import matplotlib.pyplot as plt
values=(2,3,5,2,7,9,8,6,8,5,3,2)
#plt.hist(values,bins=3)
#plt.show()

## labeling
year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
plt.plot(year,pop)
plt.xlabel("year")
plt.ylabel("pop")
plt.title("world population across the years")
#plt,yticks([0,2,4,6,8,10])
#plt.show()

#### using index() to extract information from two coreesponding lists

pop=[30.55,2.77,39.21]
countries=["afghanistan","albania","algeria"]
ind_alb=countries.index("albania")
print("population of albaina is:",pop[ind_alb]) ### not convinient approach hence the dictionary 

## using dictionaries
world ={
    "afghanistan":0.55,
    "albania":2.77,
    "algeria":39.21
    }
print("population of albania is:", world["albania"])
print(world.keys())
print("albania" in world)
world["argentina"]=40
print(world)
del(world["argentina"])
print(world)

### using countries
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print("capital of france is :", europe['france']['capital'])

# Create sub-dictionary data 
data={'capital':'rome','population':58.6}

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print("the updated europe dictionary including italy is", europe)



print("INTRODUCING PANDAS (PANDA IS A HIGH LEVEL DATA MANIPULATION TOOL)")
print('I can make data frames from panda through dictionaries')

data = { 'countries': ['france','germany'],
           'capitals': ['paris','berlin'],
           'population':['9.0','86.6' ],
            }
print(data)
import pandas as pd
brics=pd.DataFrame(data)
print(brics)

brics.index=['FR','GR']
print(brics)

european=pd.DataFrame(europe)
print(european)
print(european['spain'])
type(european['spain'])
print(european[['spain']])
#print(data[1:2])


### logic control and filtering
# Create arrays 
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
my_house>=18
print(my_house>=18)
# my_house less than your_house
my_house<your_house
print(my_house<your_house)

### USING and/ or on numpy arrays
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or (my_house>18.5, my_house<10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))


# if, else , elif

Z=5
if Z % 2==0:    #false 

    print("z is even")
else:   
    print("z is odd")

## elif
Z=3
if Z % 2==0 :    #false 
    print("z is divisible by")  
elif Z % 3==0 : #true
    print("z is divisible by 3")
else:   
    print("z is neither divisible by 2 or 3")

######## Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!") 
else :  
    print ("pretty small")


######## Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area  
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")



import os
print(os.getcwd())
import os
print(os.listdir())

import os
import pandas as pd

# Change working directory
os.chdir(r"C:\Users\DELL User\Desktop\python")


import pandas as pd

# Use the full path to your file
df = pd.read_csv(r"countries.csv",index_col = 0)

# Show the first few rows
print(df)
#df.index = ['US','CA','GR','JAP','IN','BR']
#print(df)
print(df['Capital'])
print(df.loc[['Germany']])
print(df.iloc[[4]])

## SUBSETTING COUNTRIES WITH MANY POPULATION 
# Create dense: observations that have a population over 100
pop = df['Population (millions)']
many_population= pop> 100 ## BOOLEN INDEXING
dense_population = df[many_population]

# Print dense populatiom
print(dense_population)

