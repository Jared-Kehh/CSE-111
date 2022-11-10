
def main():
    empty_list = []
    add_list(empty_list)
    remove_list(empty_list)
    add_middle_list(empty_list)
    print(empty_list)

def add_list(empty_list):
    empty_list.append("Luke")
    empty_list.append("Jared")
    empty_list.append("Cherry")

def add_middle_list(empty_list):
    add = "Bob"
    empty_list.insert(1, add)

def remove_list(empty_list):
    empty_list.pop(1)

main()