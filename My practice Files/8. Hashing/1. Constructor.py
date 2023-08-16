class Hash_Table:
    def __init__(self,size=7):
        self.data_map=[None]*size
    def hash_function(self,key):
        hash_value=0
        for letter in key:
            hash_value+=ord(letter)
        hash_value=hash_value%len(self.data_map)
        return hash_value
    def print_hash_table(self):
        for i,j in enumerate(self.data_map):
            print(i,":", j)
my_hash_table=Hash_Table()
my_hash_table.print_hash_table()