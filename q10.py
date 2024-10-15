'''
def sort_and_print_list():
    elements = input("Enter the list elements: ").split()
    integer_list = list(map(int, elements))
    integer_list.sort()
    print(" ".join(map(str, integer_list)))
sort_and_print_list()
'''

Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
