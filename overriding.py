class Animal:
    def eat(self):
        print("Animals will eat")
    def sleep(self):
        print("Animals will sleep")
class Human(Animal):
    def eat(self):
        print("Humans will eat")
    def sleep(self):
        print("Humans will sleep")
animal=Animal()
human=Human()

animal.eat()
animal.sleep()
human.eat()
human.sleep()


