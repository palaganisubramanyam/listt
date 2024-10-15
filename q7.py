'''
def search_element_in_list():
    n = int(input("Enter the size of the list: "))
    elements = input("Enter the elements of the list: ").split()
    integer_list = list(map(int, elements))
    search_element = int(input("Enter the element to search: "))
    if search_element in integer_list:
        print(f"{search_element} is present in the given list")
    else:
        print(f"{search_element} is not present in the given list")
search_element_in_list()
'''
3 is present in the given list
Sample Input 2:
5
1 2 3 6 5
4
Sample Output 2:
4 is not present in the given list
