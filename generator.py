lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

lessons2 = ['a', 'b', 'c']#6
lessons3 = 'python' #2

def my_enumerate(iterable, start=0):
    # l = start
    # for i in range(l, l+len(iterable)):
    #     yield i,iterable[i-l]# Implement your generator function here
    end = start + len(iterable)
    l = len(iterable)
    begin = start
    while begin < end:
        yield begin, iterable[abs(end-begin-l)]
        begin+= 1



for i, lesson in my_enumerate(lessons2,6):
    print("Lesson {}: {}".format(i, lesson))
