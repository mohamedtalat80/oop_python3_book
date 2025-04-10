class BaseClass:
    num_of_calls=0
    def call_me(self):
        BaseClass.num_of_calls += 1
        print(f"BaseClass called {BaseClass.num_of_calls} times")
class RightSupclass(BaseClass):
    num_of_right_calls=0
    def call_me(self):
        BaseClass.call_me(self)
        RightSupclass.num_of_right_calls += 1
        print(f"RightSupclass called {RightSupclass.num_of_right_calls} times")
class LeftSupclass(BaseClass):
    num_of_left_calls=0
    def call_me(self):
        BaseClass.call_me(self)
        LeftSupclass.num_of_left_calls += 1
        print(f"LeftSupclass called {LeftSupclass.num_of_left_calls} times")
class Supclass(RightSupclass, LeftSupclass):
    num_of_supclass_calls=0
    def call_me(self):
        LeftSupclass.call_me(self)
        RightSupclass.call_me(self)
        Supclass.num_of_supclass_calls += 1
        print(f"Supclass called {Supclass.num_of_supclass_calls} times")

subclass = Supclass()
subclass.call_me()