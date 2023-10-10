import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["mydatabase"]
collection = db["student"]

def create_student_record():
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        student_age = int(input("Enter Student Age: "))
        student_address = input("Enter Student Address: ")
        student_aadhar = input("Enter Student Aadhar Number: ")
        student_record = {"student_id": student_id, "student_name": student_name, "student_age": student_age, "student_address": student_address, "student_aadhar": student_aadhar}
        collection.insert_one(student_record)
        print("Student Record created successfully!")

def read_student_records():
        for record in collection.find():
                if 'student_id' in record:
                        student_id = record['student_id']
                else:
                        student_id = "N/A"

                if 'student_name' in record:
                        student_name = record['student_name']
                else:
                        student_name = "N/A"

                if 'student_age' in record:
                        student_age = record['student_age']
                else:
                        student_age = "N/A"

                if 'student_address' in record:
                        student_address = record['student_address']
                else:
                        student_address = "N/A"

                if 'student_aadhar' in record:
                        student_aadhar = record['student_aadhar']
                else:
                        student_aadhar = "N/A"

                print(f"Student ID: {student_id}, Student Name: {student_name}, Student Age: {student_age}, Student Address: {student_address}, Student Aadhar: {student_aadhar}")

def update_student_record():
        student_id_to_update = input("Enter the Student ID to update: ")
        print("\t")
        while True:
                print("\nSelect the Field to update:")
                print("1. Student ID")
                print("2. Student Name")
                print("3. Student Age")
                print("4. Student Address")
                print("5. Student Aadhar")
                print("6. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                        new_student_id = input("Enter the new Student ID: ")
                        collection.update_one({"student_id": student_id_to_update}, {"$set": {"student_id": new_student_id}})
                elif choice == "2":
                        new_student_name = input("Enter the new Student Name: ")
                        collection.update_one({"student_id": student_id_to_update}, {"$set": {"student_name": new_student_name}})

                elif choice == "3":
                        new_student_age = input("Enter the new Student Age: ")
                        collection.update_one({"student_id": student_id_to_update}, {"$set": {"student_age": new_student_age}})

                elif choice == "4":
                        new_student_address = input("Enter the new Student Address: ")
                        collection.update_one({"student_id": student_id_to_update}, {"$set": {"student_address": new_student_address}})

                elif choice == "5":
                        new_student_aadhar = input("Enter the new Student Aadhar: ")
                        collection.update_one({"student_id": student_id_to_update}, {"$set": {"student_aadhar": new_student_aadhar}})

                elif choice == "6":
                        break
                else:
                        print("Invalid choice")
        print("Student Record Successfully Updated")

def delete_student_record():
        student_id_to_delete = input("Enter the Student ID to delete: ")
        collection.delete_one({"student_id": student_id_to_delete})
        print("Student Record deleted successfully!")

while True:
        print("\nMenu:")
        print("1. Create Student Record")
        print("2. Read Student Records")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
                create_student_record()
        elif choice == "2":
                read_student_records()
        elif choice == "3":
                update_student_record()
        elif choice == "4":
                delete_student_record()
        elif choice == "5":
                break
        else:
                print("Invalid choice.")
