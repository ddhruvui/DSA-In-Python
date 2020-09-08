# For compiling use python3 filename.py

# method 1

# from sales import cal_tax, cal_shipping
# cal_tax()

# mehod2
import sales
sales.cal_tax()

#------------------------------------------------------------

# in case the file is not in same directory
import sys
print(sys.path)

# for importing from other folder
import ecommerce.sales_sub
ecommerce.sales_sub.cal_tax()

# or
from ecommerce.sales_sub import cal_tax
cal_tax()

# or
from ecommerce import sales
sales.cal_tax() 


#--------------------------------------------------

print(dir(sales)) # give all functions in it + default

