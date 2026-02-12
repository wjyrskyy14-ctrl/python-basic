data_dict = {'car1': 'Toyota', 'car2': 'Honda', 'car3': 'Ford'}
print(data_dict['car1'])  # Output: Toyota

for i in data_dict:
    print(i)  # Output: car1, car2, car3

for i in data_dict.values():
    print(i)  # Output: Toyota, Honda, Ford

for i in data_dict.items():
    print(i)  # Output: ('car1', 'Toyota'), ('car2', 'Honda'), ('car3', 'Ford') 

data_dict['car4'] = 'Chevrolet'
print(data_dict)  # Output: {'car1': 'Toyota', 'car2': 'Honda', 'car3': 'Ford', 'car4': 'Chevrolet'}