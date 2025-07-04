import pandas as pd
import numpy as np
data=pd.DataFrame([[9,4,8,9],[8,10,7,6],[7,6,8,5]],columns=['maths','english','science','history'])
print(data.agg(['sum','min','max']))
m=lambda x:x+10
print(m(5))
print(data)
list(map(lambda x:x*x,data['maths']))
a=list(filter(lambda x:x%2,data['maths']))
from functools import reduce
b=reduce(lambda x,y:x+y,data['science'])
print(b )
