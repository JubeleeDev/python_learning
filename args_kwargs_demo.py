
def print_all(*args):
    for a in args:
        print(a)

def print_named(**kwargs):
    for v in kwargs:
        print(v, "|", kwargs[v])

def describe(name, *args, **kwargs):
    divider = "-" * 40
    print(name)
    print(divider)
    print_all(*args)
    print(divider)
    print_named(**kwargs)

print_all("one", "two", "three")
print_named(aboba="one", joshua="two", linda="three")
describe("lola", "one", "two", "three", aboba="one", joshua="two", linda="three")