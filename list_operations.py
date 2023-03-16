"""Utilities for manipulating lists."""


### List Slicing Problems ###

def head(input_list):
    """Return the first item of the input list.

    For example:

      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'
    """

    return input_list[0]


def tail(input_list):
    """Return a new list of all items, excluding the first item.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar'] """
    # create a new list 
    # slice the input_list starting at 1, ending at 3
    
    new_list = input_list[1:3]

    return new_list



def last(input_list):
    """Return the last item of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """
    # use the negative index, [-1]

    return input_list[-1]


def top(input_list):
    """Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """

    return input_list[0:2]


def first_three(input_list):
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """
    # input_list [:3]

    return input_list[0:3]


def last_five(input_list):
    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """

    return input_list [-5: ]


def middle(input_list):
    """Return all elements of input_list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """

    return input_list[2:-2]


def inner_four(input_list):

    """Return the third, fourth, fifth, and sixth elements of input_list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]

    """

    return input_list[2:6]


def inner_four_end(input_list):
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

    """

    return input_list[-6:-2]


def replace_head(input_list):
    """Replace the head of input_list with the value 42 and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples
    [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]

    """
    input_list[0] = 42
    


def replace_third_and_last(input_list):
    """Replace third and last elements of input_list with 37 and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples
    [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]

    """
    input_list[2] = 37
    input_list[-1] = 37


def backwards(input_list):
    """Return the input list in reverse order. 
    
    You cannot use the built-in reverse() method or reversed() function.

    For example:

    >>> backwards(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['May', 'Apr', 'Mar', 'Feb', 'Jan']

    """

    return input_list[ : :-1]


def every_other(input_list):
    """Return every other item in the input list, starting with the first item. 

    For example:

    >>> every_other(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
    ['Jan', 'Mar', 'May']

    """

    return input_list[0: :2]


def delete_third_and_seventh(input_list):
    """Remove third and seventh elements of input_list and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes
    ['Do', 'Re', 'Fa', 'So', 'La', 'Do']

    """

    input_list.pop(2)
    input_list.pop(6)


### List Iteration Problems. Built-in methods are allowed for these! ###

def indices_of_positive_numbers(input_list):
    """Given a list of numbers, return a list of the indices of all positive numbers.

    For example:

    >>> indices_of_positive_numbers([1, -2, 3, 5, -8, -13, 21])
    [0, 2, 3, 6]

    """
    #create a new list 
    even_indices = []
    #need to use enumerate because we want both num and index
    for i, num in enumerate(input_list):
        #check to see if num > 0
        if num > 0:
            even_indices.append(i)
    return even_indices


def sum_repeats(input_list):
    """
    Given a list of numbers, return the sum of all numbers that are the same as the 
    next number in the list.

    In this example, there are two 1's next to each other and two 6's next to each 
    other, so the function should return 7.

    >>> sum_repeats([1, 1, 5, 1, 2, 6, 6])
    7

pu    """
    

    # create a new - to store the sum repeats 
    sum_of_repeats = []
    
    # for loop range(1,len(input_list))
    for i in range(1, len(input_list)):

    #if statement to check if i[1] == i[i-1]
        if input_list[i] == input_list[i-1]:
    #append to the new list 
            sum_of_repeats.append(input_list[i])
    
    #sum up the values
            return sum(sum_of_repeats)
    #return sum using built-in