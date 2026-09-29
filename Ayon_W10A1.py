while True:
    print("-----COMPANY B ALTERNATIVE PAYROLL-----")
    print("\t\t\t SET B")

    Ayon_employee = input("Enter employee name: ").title()
    Ayon_position = input("Enter Job position \nJanitor"
                          "\nClerk"
                          "\nCashier"
                          "\nManager\n").title()
    Ayon_actual_hours = float(input("Enter actual hours worked: "))

    match Ayon_position.lower():
        case"janitor":
            Ayon_monthly_salary = 20000
        case "clerk":
            Ayon_monthly_salary = 25000
        case "cashier":
            Ayon_monthly_salary = 28000
        case "manager":
            Ayon_monthly_salary = 45000
        case _:
            print("Invalid job position")
            exit()

    Ayon_weekly_salary = Ayon_monthly_salary / 4
    Ayon_allowance = Ayon_weekly_salary*0.05

    Ayon_basic_salary = Ayon_weekly_salary + Ayon_allowance

    Ayon_hourly_rate = Ayon_basic_salary / 48

    Ayon_absent_hours = 0
    Ayon_absence_deduction = 0
    Ayon_overtime_hours = 0
    Ayon_overtime_rate = 0
    Ayon_overtime_pay = 0

    if Ayon_actual_hours < 48:
        Ayon_absent_hours = 48 - Ayon_actual_hours
        Ayon_absence_deduction = (Ayon_absent_hours * Ayon_hourly_rate * 1.10)
    elif Ayon_actual_hours > 48:
        Ayon_overtime_hours = Ayon_actual_hours - 48
        Ayon_overtime_rate = Ayon_overtime_hours * 1.50
        Ayon_overtime_pay = (Ayon_overtime_rate * Ayon_overtime_rate)

    Ayon_net_weekly_salary = (Ayon_basic_salary - Ayon_absence_deduction + Ayon_overtime_pay)
    Ayon_half_month_salary = Ayon_weekly_salary * 2
    Ayon_gross_half_month_salary = (Ayon_basic_salary * 2)

    Ayon_half_month_absence_deduction = (Ayon_absence_deduction * 2)

    Ayon_half_month_overtime_pay = (Ayon_overtime_pay * 2)
    Ayon_net_half_month_salary = (Ayon_gross_half_month_salary - Ayon_half_month_absence_deduction + Ayon_half_month_overtime_pay)

    print("-----Payroll-----")
    print(f"Employee's name: {Ayon_employee}\n"
          f"Job position: {Ayon_position}\n"
          f"Actual Hours worked: {Ayon_actual_hours:,.2f}\n"
          f"**************************\n"
          f"Monthly Salary: ${Ayon_monthly_salary:,.2f}\n"
          f"Gross Basic Salary: ${Ayon_basic_salary:,.2f}\n"
          f"Net weekly salary: ${Ayon_net_weekly_salary:,.2f}\n"
          f"Hourly Rate: {Ayon_hourly_rate:,.2f}\n"
          f"Absent: {Ayon_absent_hours}\n"
          f"Absence deduction: {Ayon_absence_deduction}\n")

    again = input("Do you want to enter again? (Y/N): " )

    if again.lower() != "y":
        print("Program ended.")
        break








