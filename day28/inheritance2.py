
class Hospital:
     def __init__(self):
              self.HName = input('enter the hospital name: ')
              self.Location = input('enter the hospital location: ')

     def showdetails(self):
              print(f"Hospital name: {self.HName}\nLocation : {self.Location}") 



class Department:
      def __init__(self):
        
            self.Departmentname = input('enter the departmentname: ')
            self.Docname = input('enter the doctorname: ')

      def showdeptdetails(self):
                        print(f"Departmentname :{self.Departmentname}\nDoctorname: {self.Docname}")


class patient(Hospital,Department):
         def __init__(self):
                Hospital.__init__(self)
                Department.__init__(self)
                super().__init__()
                self.name =input('enter your name: ')
                self.pid = input('enter the patient id: ')
                self.gender =input('enter your gender: ')
                self.place = input('enter your place: ')
                self.admn_date = input('enter your admitdate: ')
                self.dischargedate =''

         def fullsummary(self):
                 super().showdetails()
                 super().showdeptdetails()
                 print(f"Name: {self.name}\npatientid: {self.pid}\nGender: {self.gender}\nPlace: {self.place}\nAdmit_date: {self.admn_date}\n ")
                 if self.dischargedate == '':
                         print('not yet discharged')
                 else: print('Dischargedate:',self.dischargedate)

         def setdischargedate(self):
                 self.dischargedate = input('enter the dischargedate')

               
         def dischargedetails(self):
                     

                     print(f"Name: {self.name}\npatient {self.pid}\nDoctorname :{self.Docname}\nPlace: {self.place}\nAdmit_date: {self.admn_date}\nDischarge :{self.dischargedate} ")
                     if self.dischargedate == '':
                                              print('not yet discharged')
                     else: print('Dischargedate:',self.dischargedate)
        

p = patient()


p.fullsummary()
p.setdischargedate()
p.fullsummary()
p.dischargedetails() 