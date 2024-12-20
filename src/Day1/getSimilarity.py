from collections import Counter
# Define the two arrays
array1 = []
array2 = []

with open('Data.txt', 'r') as file:
    for line in file:
        value1, value2 = map(int, line.split()) 
        array1.append(value1) 
        array2.append(value2) 

right_count = Counter(array2)

similarity_score = sum(left_number * right_count[left_number] for left_number in array1)
print("Similarity score is:", similarity_score)
