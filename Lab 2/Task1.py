


studentNameList = []
studentIDList = []
studentCityList = []


while True:
    studentName = input("Enter the name of the Student: ")
    if (studentName.lower()=="stop"):
        break
    studentNameList.append(studentName)
    studentID = input("Enter the ID of the Student: ")
    studentIDList.append(studentID)
    studentCity = input("Enter the City of the Student: ")
    studentCityList.append(studentCity)


studentDictionary = {}

for i in range(len(studentIDList)):
    studentDictionary[studentIDList[i]] = [studentNameList[i],studentCityList[i]]

for studentID, (studentName, studentCity) in studentDictionary.items():
    print(f"ID: {studentID}, Name: {studentName}, City: {studentCity}")
print()

while True:
    studentID = input("Enter student ID to query (or type 'stop' to end): ")
    if studentID.lower() == 'stop':
        break
    elif studentID in studentDictionary:
        studentName, studentCity = studentDictionary[studentID]
        print(f"Student ID: {studentID}\nName: {studentName}\nCity: {studentCity}")
    else:
        print("Student ID not found.")


