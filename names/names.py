import time

start_time = time.time()

#--------------------------ORIGINAL SOLUTION-----------------------------

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#-----------------------------ITERATION #1-------------------------------

duplicates = []

with open('names_1.txt') as file1, open('names_2.txt') as file2:
    for line in set(line.strip() for line in file1) & set(line.strip() for line in file2):
        if line: 
            duplicates.append(line)

#-----------------------------ITERATION #2-------------------------------

# with open('names_1.txt', 'r') as file1:
#     with open('names_2.txt', 'r') as file2:
#         duplicate = set(file1).intersection(file2)
        
# duplicate.discard('\n')
    
# with open('duplicates.txt', 'w') as file_out:
#     for line in duplicate:
#         file_out.write(line)
        
# f = open('duplicates.txt', 'r')
# duplicates = f.read().split("\n")  # List containing 10000 names
# f.close()

#-----------------------------TEST CASES---------------------------------

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

