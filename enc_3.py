class GovernmentWorker:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def _salary_check(self):
        print('Salary of government worker ' + self.name + ' from ' + self.department + ' department is ' + str(self.salary) + '$')

    def is_from_department(self, department):
        if department == self.department:
            self._salary_check()
        else:
            print('Government worker ' + self.name + ' is not from ' + department + ' department')


s = GovernmentWorker('Vlad', 'tourism', 200000)
s.is_from_department('education')
s.is_from_department('tourism')
