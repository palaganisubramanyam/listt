'''
def count_value_in_list():
    elements = input("Enter the list elements: ").split()
    integer_list = list(map(int, elements))
    value_to_count = int(input("Enter the value to count: "))
    count = integer_list.count(value_to_count)
    print(count)
count_value_in_list()
'''

Sample Output:
3
