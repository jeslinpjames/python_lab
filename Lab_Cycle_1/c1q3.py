#Function to compute the gross salary
def gross_salary(bp,da,hra,ma):
  gs=bp+da+hra+ma
  return(gs)

#Function to compute the deduction
def deduction(pt,pf,it):
  d=pt+pf+it
  return(d)

#Function to compute the net salary
def net_salary(gs,d):
  ns=gs-d
  return(ns)

#Function to generate and print the payslip
def gen_payslip(name,code,bp):
  if(bp<10000):#Condition when the basic pay is less than 10000
    ma,pt=500,20
    da=(5/100)*bp#To compute the value of DA from Basic Pay
    hra=(2.5/100)*bp#To compute the value of HRA from Basic Pay
    pf=(8/100)*bp#To compute the value of PF from Basic Pay
    it=0
  elif(bp<=30000)and (bp>10000):#Condition when the basic pay is greater than 10000 but less than 30000
    ma,pt=2500,60
    da=(7.5/100)*bp
    hra=(5/100)*bp
    pf=(8/100)*bp
    it=0
  elif(bp>30000)and(bp<=50000):#Condition when the basic pay is greater than 30000 but less than 50000
    ma,pt=5000,60
    da=(11/100)*bp
    hra=(7.5/100)*bp
    pf=(11/100)*bp
    it=(11/100)*bp
  else:#Condition when the basic pay is greater than 50000
    ma,pt=7000,80
    da=(25/100)*bp
    hra=(11/100)*bp 
    pf=(12/100)*bp
    it=(20/100)*bp
  #To display all the details accepted and computed in the payment slip
  gs=gross_salary(bp,da,hra,ma)
  d=deduction(pt,pf,it)
  ns=net_salary(gs,d)
  print("********PAYMENT SLIP*********")
  print("Employee name      :",name)
  print("Employee code      :",code)
  print("Basic Pay          :",bp)
  print("Employee DA        :",da)
  print("Employee HRA       :",hra)
  print("Employee MA        :",da)
  print("Employee PT        :",pt)
  print("Employee PF        :",pf)
  print("Employee IT        :",it)
  print("Gross Salary       :",gs)
  print("Deduction          :",d)
  print("Net Salary         :",ns)

  #To accept Employee name code and basic pay from the user and call the functions to print the payment slip
name=input("Enter the Employee name:")
code=int(input("Enter the code:"))
bp=int(input("Enter the basic pay:"))
gen_payslip(name,code,bp)