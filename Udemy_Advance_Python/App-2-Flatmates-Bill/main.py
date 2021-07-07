from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input("Enter bill amount: "))
bill_period = input("Enter bill period(MMMM YYYY): ")

flatmate1_name = input("Enter flatmate1 name:")
flatmate1_day_in_house = int(input(f"Enter {flatmate1_name} days in house:"))

flatmate2_name = input("Enter flatmate2 name:")
flatmate2_day_in_house = int(input(f"Enter {flatmate2_name} days in house:"))

the_bill = Bill(bill_amount, bill_period)
flatmate_1 = Flatmate(flatmate1_name, flatmate1_day_in_house)
flatmate_2 = Flatmate(flatmate2_name, flatmate2_day_in_house)

print("{0} pays: {1}".format(flatmate_1.name, flatmate_1.pays(bill=the_bill, flatmate2=flatmate_2)))
print("{0} pays: {1}".format(flatmate_2.name, flatmate_2.pays(bill=the_bill, flatmate2=flatmate_1)))

pdf_report = PdfReport(filename=f"outputs/{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate_1, flatmate2=flatmate_2, bill=the_bill)
