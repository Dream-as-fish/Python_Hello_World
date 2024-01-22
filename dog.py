class Dog:
    """一次模拟小狗的简单尝试"""

    def _init__(self, name, age):
        """初始化Dog实例的属性"""
        self.name = name
        self.age = age

    def ist(self):
        """模拟小狗收到的命令坐下"""
        print(f"{self.name} is sitting.")

    def roll_over(self):
        """模拟小狗收到的命令滚过"""
        print(f"{self.name} is rolling over.")
