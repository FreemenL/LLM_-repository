from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self,emp_id,name,base_salary=5000):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    # 计算奖金
    @abstractmethod
    def calculate_bonus(self)->float:
        pass
    # 计算总工资
    def total_salary(self):
        return self.base_salary+self.calculate_bonus()

    def show_info(self):
        print(f"工号：{self.emp_id} | 姓名：{self.name} | 基本工资：{self.base_salary} | 奖金：{self.calculate_bonus()} | 总工资：{self.total_salary()}")

# 销售
class Salesman(Employee):
    def __init__(self,emp_id,name,sales_amount,base_salary=5000):
        super().__init__(emp_id,name,base_salary)
        self.sales_amount=sales_amount

    def calculate_bonus(self)->float:
        return  self.sales_amount*0.05
    def total_salary(self):
        return self.base_salary+self.calculate_bonus()

# 经理
class Manager(Employee):
      def calculate_bonus(self)->float:
          return 3000

# 程序员
class Programmer(Employee):
    def __init__(self, emp_id, name, project_number, base_salary=5000):
        super().__init__(emp_id, name, base_salary)
        self.project_number = project_number

    def calculate_bonus(self) -> float:
        return self.project_number * 500



if __name__ == "__main__":
    employees = [
        Salesman("S001", "张三", 5000),
        Manager("M001", "李四"),
        Programmer("P001", "王五", 3)
    ]

    print("=" * 70)
    print("员工工资表")
    print("=" * 70)
    for emp in employees:
        emp.show_info()
    print("=" * 70)

