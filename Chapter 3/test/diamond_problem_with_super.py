class BaseClass:
    num_of_calls=0
    def call_me(self):
        BaseClass.num_of_calls += 1
        print(f"BaseClass called {BaseClass.num_of_calls} times")
class RightSupclass(BaseClass):
    num_of_right_calls=0
    def call_me(self):
        super().call_me()
        RightSupclass.num_of_right_calls += 1
        print(f"RightSupclass called {RightSupclass.num_of_right_calls} times")
class LeftSupclass(BaseClass):
    num_of_left_calls=0
    def call_me(self):
        super().call_me()
        LeftSupclass.num_of_left_calls += 1
        print(f"LeftSupclass called {LeftSupclass.num_of_left_calls} times")
class Supclass(RightSupclass, LeftSupclass):
    num_of_supclass_calls=0
    def call_me(self):
        super().call_me()
        Supclass.num_of_supclass_calls += 1
        print(f"Supclass called {Supclass.num_of_supclass_calls} times")

subclass = Supclass()
subclass.call_me()
print(Supclass.__mro__)