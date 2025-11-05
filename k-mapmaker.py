import numpy as np
#edit the array to your counting sequence
numbers=[0,5,4,3,2,8,5,6,7,6,2]
length=len(numbers)
if length > 16:
  raise ValueError('Too many numbers')
binary=[]

#turns numbers to 4-bit binary form
for i in range(length):
  if numbers[i] > 9:
    raise ValueError(f'Invalid number, Too large -----> {numbers[i]}')
  if numbers[i] < 0:
    raise ValueError(f'Invalid number, Too small -----> {numbers[i]}')
  binary.append(f'{numbers[i]:04b}')

#shifts the numbers down
binary_next=np.roll(binary, -1)
X='X'
#make j and k arrays
J=np.full((4,4,4),X)
K=np.full((4,4,4),X)

for ii in range(length):
  Q=[]
  Qn=[]
  #Assigns row and collumn for each numbers
  #needs improved way on assinging
  if numbers[ii] == 0:
    r,c=0,0
  elif numbers[ii] == 1:
    r,c=0,1
  elif numbers[ii] == 2:
    r,c=0,3
  elif numbers[ii] == 3:
    r,c=0,2
  elif numbers[ii] == 4:
    r,c=1,0
  elif numbers[ii] == 5:
    r,c=1,1
  elif numbers[ii] == 6:
    r,c=1,3
  elif numbers[ii] == 7:
    r,c=1,2
  elif numbers[ii] == 8:
    r,c=3,0
  elif numbers[ii] == 9:
    r,c=3,1
  for i in range(4):
    Q.append(binary[ii][3-i])
    Qn.append(binary_next[ii][3-i])
    if Q[i]=='0':
      if Q[i]==Qn[i]:
        j=0
        k=X
      else:
        j=1
        k=X

    elif Q[i]=='1':
      if Q[i]==Qn[i]:
        j=X
        k=0
      else:
        j=X
        k=1

    J[i,r,c]=j
    K[i,r,c]=k
print('J k-maps from J0 to J3')
print(J)
print()
print('K k-maps from K0 to K3')
print(K)
