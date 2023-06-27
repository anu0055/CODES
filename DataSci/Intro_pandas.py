import pandas as pd

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passing' : [3, 7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)