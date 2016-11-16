'''
Created on 16.11.2016

@author: Jacob
'''
def poly_add(a, b):
   """Add two polynomials of maybe different lengths.
   
Don't change the inputs and return the result."""
   c = []
   # polynomials could be of different lengths
   if len(a) > len(b):
      longer = a
      shorter = b
   else:
      longer = b
      shorter = a
   # for the minimum of the lengths of both
   # add the elements
   for i in range(len(shorter)):
      c.append(longer[i] + shorter[i])
   # then just copy the elements from the longer
   for i in range(len(shorter), len(longer)):
      c.append(longer[i])
   return c