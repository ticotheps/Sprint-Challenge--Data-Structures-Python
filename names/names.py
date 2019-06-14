import time

#--------------------------ORIGINAL SOLUTION-----------------------------

start_time_original_solution = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates_original = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates_original.append(name_1)

end_time_original_solution = time.time()

#-----------------------------ITERATION #1-------------------------------

start_time_iter_1_solution = time.time()

duplicates_iter_1 = []

with open('names_1.txt') as file1, open('names_2.txt') as file2:
    for line in set(line.strip() for line in file1) & set(line.strip() for line in file2):
        if line: 
            duplicates_iter_1.append(line)

end_time_iter_1_solution = time.time()

#-----------------------------ITERATION #2-------------------------------

start_time_iter_2_solution = time.time()

with open('names_1.txt', 'r') as file1:
    with open('names_2.txt', 'r') as file2:
        duplicate = set(file1).intersection(file2)
        
duplicate.discard('\n')
    
with open('duplicates.txt', 'w') as file_out:
    for line in duplicate:
        file_out.write(line)
        
f = open('duplicates_iter_2.txt', 'r')
duplicates_iter_2 = f.read().split("\n")  # List containing 10000 names
f.close()

end_time_iter_2_solution = time.time()

#-----------------------------TEST CASES---------------------------------

print (f"{len(duplicates_original)} duplicates in original solution:\n\n{', '.join(duplicates_original)}\n")
print (f"runtime for original: {end_time_original_solution - start_time_original_solution} seconds\n\n")

print (f"{len(duplicates_iter_1)} duplicates in iteration #1:\n\n{', '.join(duplicates_iter_1)}\n")
print (f"runtime for iteration #1: {end_time_iter_1_solution - start_time_iter_1_solution} seconds\n\n")

print (f"{len(duplicates_iter_2)} duplicates in iteration #2:\n\n{', '.join(duplicates_iter_2)}\n")
print (f"runtime for iteration #2: {end_time_iter_2_solution - start_time_iter_2_solution} seconds\n\n")

