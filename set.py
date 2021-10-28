def remove_duplicates(some_list):
    my_set = set(some_list)
    return my_set

def run():
    random_list=[1,2,3,2,2,4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()   