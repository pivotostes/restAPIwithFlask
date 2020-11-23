class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")


# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

ClassTest.class_method()
