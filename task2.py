'''
2. Create a program whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, gross salary, and net salary.

NB: Use KRA, NHIF, and NSSF values provided in the link below.
https://www.aren.co.ke/payroll/taxrates.htm
https://www.kra.go.ke/en/individual/calculate-tax/calculating-tax/paye

'''

 #Gross Salary = Basic Salary + Benefits
#NSSF Deduction = 6% of gross salary ( at 1080)
#NHIF Deduction = Based on salary brackets
#PAYE (Tax) = Progressive tax bands with personal relief (2400)
#Net Salary = Gross - (NSSF + NHIF + PAYE)

import unittest

# Payroll class to calculate individual's salary details
class Payroll: 
    def __init__(self, basic_salary: float, benefits: float):
        self.basic_salary = basic_salary
        self.benefits = benefits

    def gross_salary(self) -> float:
        #Gross Salary = Basic Salary + Benefits
        return self.basic_salary + self.benefits

    def nssf_deductions(self) -> float:
       #NSSF pension contribution (6%  at 1080)
        return min(self.gross_salary() * 0.06, 1080)

    def nhif_deductions(self) -> float:
        #NHIF deduction based on gross salary brackets
        gross = self.gross_salary()
        if gross <= 5999:
            return 150
        elif gross <= 7999:
            return 300
        elif gross <= 11999:
            return 400
        elif gross <= 14999:
            return 500
        elif gross <= 19999:
            return 600
        elif gross <= 24999:
            return 750
        elif gross <= 29999:
            return 850
        elif gross <= 34999:
            return 900
        elif gross <= 39999:
            return 950
        elif gross <= 44999:
            return 1000
        elif gross <= 49999:
            return 1100
        elif gross <= 59999:
            return 1200
        elif gross <= 69999:
            return 1300
        elif gross <= 79999:
            return 1400
        elif gross <= 89999:
            return 1500
        elif gross <= 99999:
            return 1600
        else:
            return 1700

    def payee(self) -> float:
      #PAYE tax after applying tax band
        taxable_income = self.gross_salary() - self.nssf_deductions()

        if taxable_income <= 24000:
            tax = taxable_income * 0.1
        elif taxable_income <= 32333:
            tax = (24000 * 0.1) + (taxable_income - 24000) * 0.25
        else:
            tax = (24000 * 0.1) + (8333 * 0.25) + (taxable_income - 32333) * 0.30

        # Personal Relief (2400 per month)
        tax -= 2400
        return max(tax, 0)

    def net_salary(self) -> float:
        #Net salary = Gross - (NSSF + NHIF + PAYE)
        return self.gross_salary() - (
            self.nssf_deductions() + self.nhif_deductions() + self.payee()
        )


# TESTS 
class TestPayroll(unittest.TestCase):

    def setUp(self):
        self.payroll = Payroll(50000, 10000)

    def test_gross_salary(self):
        self.assertEqual(self.payroll.gross_salary(), 60000)

    def test_nssf_deductions(self):
        self.assertEqual(self.payroll.nssf_deductions(), 1080)  # capped

    def test_nhif_deductions(self):
        self.assertEqual(self.payroll.nhif_deductions(), 1200)  # 60k gross

    def test_payee(self):
        tax = self.payroll.payee()
        self.assertTrue(tax > 0)

    def test_net_salary(self):
        net = self.payroll.net_salary()
        self.assertTrue(net < self.payroll.gross_salary())


if __name__ == "__main__":
    # Run tests first
    unittest.main(exit=False)

    # interactive demo
    print("\n--- Salary calc demo ---")
    try:
        basic = float(input("Enter Basic Salary: "))
        benefits = float(input("Enter Benefits: "))
        payroll = Payroll(basic, benefits)

        print(f"\nGross Salary: {payroll.gross_salary():,.2f}")
        print(f"NSSF Deduction: {payroll.nssf_deductions():,.2f}")
        print(f"NHIF Deduction: {payroll.nhif_deductions():,.2f}")
        print(f"PAYE (Tax): {payroll.payee():,.2f}")
        print(f"Net Salary: {payroll.net_salary():,.2f}")

    except ValueError:
        print("Attention kindly enter valid numeric values for salary and benefits.")