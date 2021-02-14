def share_class(classes, instructors):
    pass


def get_departments(file):
    """
    This function will read file and extract the names of 
    departments, the number of students in each department
    and return it as a list of dicts with names as keys and 
    the number of students as values.

    eg:
        get_departments('departments.txt')
        --> returns [{'a': 45}, {'b': 87}, {'c': 23}]

    @param: str - file
    @return: list of dicts.
    """

    # Initialize variables
    ls = list()
    d = dict()

    # Open file, read line by line
    with open(file, 'r') as f:
        for line in f:
            line = line.split() # Split line by space.
            d[line[0]] = line[1]    # Add first element to d as key and second element as value
            ls.append(d)    # Add d into ls.
            d = dict()  #Re-initialize d for next round.

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
        dic[name] = []
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


def main():
    departments = 'classes.txt'
    instructors = 'instructors.txt'

    share_class(departments, instructors)
    print(get_instructors(instructors))
    print(randomize_names(instructors))
    print(get_departments(departments))


if __name__ == '__main__':
    main()