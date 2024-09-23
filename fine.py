from datetime import datetime


bookID = input("Enter book ID: ")
dueDate = input("Enter due date (dd/mm/yyyy): ")
returnDate = input("Enter return date (dd/mm/yyyy): ")


dueDate = datetime.strptime(dueDate, "%d/%m/%Y")
returnDate = datetime.strptime(returnDate, "%d/%m/%Y")


daysOverdue = (returnDate - dueDate).days


if daysOverdue <= 7:
    fineRate = 20
elif 8 <= daysOverdue <= 14:
    fineRate = 50
else:
    fineRate = 100


fineAmount = daysOverdue * fineRate


print("Book ID:", bookID)
print("Due Date:", dueDate.strftime("%d/%m/%Y"))
print("Return Date:", returnDate.strftime("%d/%m/%Y"))
print("Days Overdue:", daysOverdue)
print("Fine Amount:", fineAmount)