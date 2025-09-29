# Hint: Company has a fixed roster of employees each pay period
employees = 12
total_payroll = 0

for i in range(employees):
    print(f"Employee {i+1}")
    employee_num = float(input("Enter  number employees : "))
    hours_worked = float(input("Enter number of hours worked: "))
    overtime_hours = float(input("Enter number of overtime hours worked: "))
    hourly_pay = float(input("Enter hourly pay rate: "))

    regular_pay = hours_worked * hourly_pay
    overtime_pay = overtime_hours * hourly_pay * 1.5
    total_pay = regular_pay + overtime_pay

    print(f"{employee_num}'s total pay: ${total_pay:.2f}")
    total_payroll += total_pay

print(f"\Total payroll for all employees: ${total_payroll:.2f}")
# Think: How do you process a predetermined number of employees?
# Your processing structure here
