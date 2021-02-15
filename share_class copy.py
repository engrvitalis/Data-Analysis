def share_class(departments, instructors):
    """
    This function takes 2 arguments, departments and instructors which are
    both list of dictionaries. It then allocate departments to instructors
    based on the number students in it while keeping to minimum the difference 
    in the total number of students allocated to each instructor.

    @param: list - departments, instructors
    @return: list
    """

    import operator as op

    # Initialize variable
    index = 0
    count = 0

    # Sort departments by number of students in ascending order.
    s = sorted(departments, key=op.itemgetter(1), reverse=True)

    for instructor in instructors:
        print(instructor)
    print(s)


    # return s


def get_departments(file):
    """
    This function will read file and extract the names of 
    departments, the number of students in each department
    and return it as a list of tuples containing the name 
    and students count.

    eg:
        get_departments('departments.txt')
        --> returns [('a': 45), ('b': 87), ('c': 23)]

    @param: str - file
    @return: list of tuples.
    """

    # Initialize variables
    ls = list()

    # Open file, read line by line
    with open(file, 'r') as f:
        for line in f:
            line = line.split() # Split line by space.
            ls.append((line[0], int(line[1])))    # Add tuple of first and second item into ls.

    return ls


def get_instructors(names):
    """
    This function accepts an iterable, names as argument and creates 
    a list of dictionaries with elements of names as keys and empty list
    as values.

    eg:
        get_instructors({'a', 'b', 'c'})
        --> return [{'a': [], 'b': [], 'c': []}]

    @param: iterables
    @return: list of dicts.
    """

    # Initialize variables
    ls = list()
    dic = dict()

    # Assign names as keys and [] as values in dic and append 
    # dic to ls.
    for name in randomize_names(names):
        dic[name] = {}
        ls.append(dic)
        dic = dict() # Re-initialize dic.

    return ls


def randomize_names(file):
    """
    This function reads file and add lines to 
    set, s.

    @param: str - file.
    @return: set - with names in no particular order.
    """

    # Initialize variables.
    s = set()

    # Go through file and add the content to s.
    with open(file, 'r') as f:
        for line in f:
            s.add(line.strip())
    return s


def disp(ls):
    for schedule in ls:
        for instructor, departments in schedule.items():
            print(f'Instructor: {instructor}')
            print('*'*50)
            print('Departments\tNumber of Students')
            print('*'*50)
            for department, count in departments.items():
                print(f'{department}\t\t{count}')
            print()


def main():
    departments = 'classes.txt'
    instructors = 'instructors.txt'

    instructors = get_instructors(instructors)
    departments = get_departments(departments)

    # disp(share_class(departments, instructors))
    share_class(departments, instructors)


if __name__ == '__main__':
    main()