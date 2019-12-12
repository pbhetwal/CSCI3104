# Python imports 
import string 
# NOTE: sympy LIBRARY MUST BE DOWNLOADED 
import sympy 
import random 
import matplotlib.pylab as plt 
from matplotlib.pyplot import figure 

# f and h_1 
def f(x_i):
	return string.ascii_lowercase.index(x_i.lower())+1

def h_1(x, l):
	tot = 0 
	for i in x: 
		tot += f(i)
	return tot % l

# f_2 and h_2 
def f_2(x_i, a_i):
	return f(x_i) * a_i 

def h_2(x, l):
	global choose 
	tot = 0 
	j = 0 
	for i in range(len(x)): 
		tot += f_2(x[i], choose[j])
		if(j < len(choose)-1):
			j += 1
	return tot % l 



# CREATE HISTOGRAM 
names = []
with open('dist.all.last.txt', 'r') as file:
	for line in file: 
		names += [line.split('\t')[0]]
sample = random.sample(names, int(len(names)*0.5))

h1_arr = []
h2_arr = []
l = 5987
choose = list(range(0, l))
random.shuffle(choose)

freq = {}
freq_2 = {} 
longest_h1 = []
longest_h2 = []
for i in sample:
	h1_arr += [h_1(i, l)]
	if h1_arr[-1] in freq:
		freq[h1_arr[-1]] += 1
	else:
		freq[h1_arr[-1]] = 1
	longest_h1.append(max(freq.values()))

	h2_arr += [h_2(i, l)]
	if h2_arr[-1] in freq_2:
		freq_2[h2_arr[-1]] += 1
	else:
		freq_2[h2_arr[-1]] = 1 
	longest_h2.append(max(freq_2.values()))

# Distribution of hash locations  
x_1 = list(range(1, len(h1_arr)+1))
x_2 = list(range(1, len(h2_arr)+1))

bins = range(0, l, 50)
figure(figsize=(16, 8), edgecolor = 'b')
plt.hist(h1_arr, bins=bins, alpha=0.5, label='h_1(x)')
plt.xlabel("Bucket", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.title("Distribution of Hash Locations", fontsize=18)

plt.hist(h2_arr, bins=bins, alpha=0.5, label='h_2(x)')
plt.legend(fontsize=18)
plt.show()

# Longest chain for h_1(x)
plt.xlabel("Strings Hashed So Far")
plt.ylabel("Longest Chain")
plt.title("Longest Chain in Relation to Strings Hashed So Far (h_1(x))")
plt.plot(x_1, longest_h1)
plt.show()

# Longest chain for h_2(x)
plt.xlabel("Strings Hashed So Far")
plt.ylabel("Longest Chain")
plt.title("Longest Chain in Relation to Strings Hashed So Far (h_2(x))")
plt.plot(x_2, longest_h2)
plt.show()

# Collisions for h_1(x) and h_2(x)
# Terribly inefficent:  takes several additional 
# minutes to run - will eventually output graphs 
sample = random.sample(names, 10000)
primes = list(sympy.primerange(2, 5987))
COLL1 = []
COLL2 = [] 
for i in primes: 
	h1 = []
	h2 = [] 
	# Used by h_2(x, l)
	# Choose randomly for a_i 
	choose = list(range(0, i))
	random.shuffle(choose)
	freq = {}
	freq_2 = {}
	for j in sample:
		h1 += [h_1(j, i)]
		if h1[-1] in freq:
			freq[h1[-1]] += 1
		else:
			freq[h1[-1]] = 0

		h2 += [h_2(j, i)]
		if h2[-1] in freq_2:
			freq_2[h2[-1]] += 1
		else:
			freq_2[h2[-1]] = 0
	
	COLL1.append(sum(freq.values()))
	COLL2.append(sum(freq_2.values()))

plt.plot(primes, COLL1)
plt.xlabel("Number of Buckets")
plt.ylabel("Number of Collisions")
plt.title("Number of Buckets vs. Collisions (h_1(x))")
plt.show()

plt.plot(primes, COLL2)
plt.xlabel("Number of Buckets")
plt.ylabel("Number of Collisions")
plt.title("Number of Buckets vs. Collisions (h_2(x))")
plt.show()
