# import csv module
import csv

def student_grades():
    # ask instructor to input how many students they want to enter.
    num_students = int(input("Please enter the number of students: "))

    # store the student grades into a file
    with open('grades.csv', 'w', newline='') as csvfile:
        # create a CSV writer object
        csvwriter = csv.writer(csvfile)

        # create a header
        csvwriter.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # create a for loop to ask each student to enter their exam grades
        for _ in range(num_students):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter exam 1 grade: "))
            exam2 = int(input("Enter exam 2 grade: "))
            exam3 = int(input("Enter exam 3 grade: "))

            # display new row in csv file with the student's info
            csvwriter.writerow([first_name, last_name, exam1, exam2, exam3])

    # print message to let user know grades have been stored in csv file
    print("Grades have been written to grades.csv")

# Run program
if __name__ == "__main__":
    student_grades()
