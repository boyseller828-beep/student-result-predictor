import numpy as np
array = np.array([[['A', 'B', 'C'], ['D','E','F'],['G','H','I']],
                  [['J', 'K', 'L'], ['M','N','O'],['P','Q','R']]])
                  

word = array[0,0,0] + array[0,1,2] + array[1,1,1] + array[0,0,0] + array[1,1,1]
print(word)