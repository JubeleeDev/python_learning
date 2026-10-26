
def test_pointer():
    test_list = [5,3,5]
    pointer = test_list
    pointer.append(6)
    print(test_list)
    print(pointer)

def default_values(value, mylist = []):
    mylist.append(value)
    print(mylist)

def right_default_values(value, mylist=None):
    if mylist is None:
        mylist = []
    mylist.append(value)
    print(mylist)

test_pointer()
default_values(5)
default_values(10)

right_default_values(5)
right_default_values(10)

