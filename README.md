# k-maper
Python script used to make Karnaugh maps for 4-bit synchronous counter that uses JK flip flops

How to use:
Edit the numbers array to your counting sequence (max of 16 numbers)
Example
  Your counting sequence is 3,4,5,6,2,5,7,1,0
  numbers = [3,4,5,6,2,5,7,1,0]

  Run the code
  It will out put 4 arrays for your J Karnaugh maps (J_0 to J_3)
  Then 4 arrays for your K Karnaugh maps (K_0 to K_3)

  Use the said Karnaugh maps into a K-map solver such as
    https://www.boolean-algebra.com/kmap/
  To produce your boolean equations for each J and K input
  

