import glob
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Define directories
data_dir = os.path.join(current_dir, 'data')
obj_dir = os.path.join(data_dir, 'obj')

# Percentage split
percentage_test = 10
index_test = round(100 / percentage_test)

# Open files
file_train = open(os.path.join(data_dir, 'train.txt'), 'w')
file_test = open(os.path.join(data_dir, 'test.txt'), 'w')

counter = 1
for pathAndFilename in glob.iglob(os.path.join(obj_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(os.path.join(obj_dir, title + '.jpg') + "\n")
    else:
        file_train.write(os.path.join(obj_dir, title + '.jpg') + "\n")
        counter += 1

file_train.close()
file_test.close()
