import csv

def read_grades():
    # Open the grades.csv file for reading
    with open('grades.csv', mode='r') as file:
        csvreader = csv.reader(file)

        # Read the header. this will avoid repetition of first header
        header = next(csvreader)

        # Print the header with students name and grades of exams
        print(f"{'First Name':<18}{'Last Name':<18}{'Exam 1':<12}{'Exam 2':<12}{'Exam 3':<12}")
        # create a line to separate the titles/headers
        print("-" * 70)

        # Read and print each row of grades
        for row in csvreader:
            print(f"{row[0]:<18}{row[1]:<18}{row[2]:<12}{row[3]:<12}{row[4]:<12}")


if __name__ == "__main__":
    read_grades()
