def change_list(a_list):
    a_list = [1, 2, 3]
    return a_list


main_list = []
change_list(main_list)
print(main_list)

class Cat:

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    cat1 = Cat('Tom')
    cat2 = Cat('Tom')
    print(cat1 == cat2)


var = 1,
var_2 = (1)
print(type(var))
print(type(var_2))

#a_tuple = (1, 2, [3, 4])
#a_tuple[2] += [5]
#print(a_tuple)

a_dict = {}
a_dict[1] = 'foo'
a_dict[True] = 'bar'
print(a_dict)




def num_in(m):
    if sorted(set([i for i in m])) == list('0123456789'):
        return True
    return False

print(num_in(input()))