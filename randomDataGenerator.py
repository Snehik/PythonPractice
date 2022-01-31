import random
import pandas as pd
import sys
import os

if __name__ == '__main__':
    first_name = ['Snehik', 'Saumalya', 'Saikat', 'Aniket', 'Avik', 'Avirup', 'Avijit', 'Snehasish', 'Anurag']
    age = [32, 31, 30, 37, 40]
    last_name = ['Podder', 'Pal', 'Sarkar', 'Bag', 'Chaudhuri', 'Samanta']
    city_name = ['Siliguri', 'Kolkata', 'Durgapur', 'Burdwan', 'Chandannagar']
    output = []
    for num in range(5):
        e_id = str(num + 1)
        f_name = random.choice(first_name)
        l_name = random.choice(last_name)
        em_age = str(random.choice(age))
        em_city = random.choice(city_name)

        intermediate_data = e_id+','+f_name+','+l_name+','+em_age+','+em_city
        mod_data = intermediate_data.split(',')
        output.append(mod_data)

result = pd.DataFrame(output)
column_names = ['emp_id', 'emp_first_name', 'emp_last_name', 'emp_age', 'emp_city']
result.to_csv("C:/Users/Snehik/Desktop/emp_data.csv", index=False, header=column_names)





