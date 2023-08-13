class Hashing:
    def __init__(self,size=7):
        self.data_map=[None]*size
    def hash_function(self,key):
        hash_value=0
        for letter in key:
            hash_value=