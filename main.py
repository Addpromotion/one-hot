import random

class OneHotEncoder:
    def __init__(self, lst):
        self.lst = lst
        self.categories = list(set(lst))
        self.one_hot = self.encode()
    
    def encode(self):
        one_hot_dict = {category: [] for category in self.categories}
        
        for item in self.lst:
            for category in self.categories:
                if item == category:
                    one_hot_dict[category].append(1)
                else:
                    one_hot_dict[category].append(0)
        
        return one_hot_dict
    
    def get_dataframe(self):
        import pandas as pd
        
        data_one_hot = pd.DataFrame(self.one_hot)
        data_one_hot['original'] = self.lst
        
        return data_one_hot

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

encoder = OneHotEncoder(lst)

data_one_hot = encoder.get_dataframe()

print(data_one_hot.head())