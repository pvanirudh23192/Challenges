path = 'test_files/test_string.txt'
test_file = open(path, 'r')
print (test_file.read()[101])
test_file.close()
