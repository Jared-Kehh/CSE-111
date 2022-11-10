import csv
def main():
    student_index = 0
    student_dict = read_dict("students.csv", student_index)
    print(student_dict)
    student_ID = input("Enter a your Student ID#: ")
    for list_of_student in student_dict:
        if student_ID == list_of_student:
            name = student_dict[student_ID]
        else:
            print("No Student ID was found")
    print(name[1])
                
        

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    list_stu = []
    with open (filename, "r") as student_filename:
        readers = csv.reader(student_filename)

        for list_student in readers:
            list_stu.append(list_student)

            
    return list_stu



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary

main()