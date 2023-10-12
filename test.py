# import CS2APY as cs2apy

import CS2APY as cs2apy

# w/o instantiation
all = cs2apy.fetch_all()
print(all)

# w/ instantiation
class_all = cs2apy.CS2APY()
print(class_all.fetch_all())