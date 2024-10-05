class Car:
    def __init__(self):
        self.count_of_wheels = 4

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__()
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is going")

    def stop(self):
        print(f"{self.name} is stoped")

    def turn(self, direction):
        print(f"{self.name} is turned {direction}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__()
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is going")

    def stop(self):
        print(f"{self.name} is stoped")

    def turn(self, direction):
        print(f"{self.name} is turned {direction}")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__()
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is going")

    def stop(self):
        print(f"{self.name} is stoped")

    def turn(self, direction):
        print(f"{self.name} is turned {direction}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is going")

    def stop(self):
        print(f"{self.name} is stoped")

    def turn(self, direction):
        print(f"{self.name} is turned {direction}")

def task1():
    townCar1 = TownCar(60, "red", "Honda", False)
    sportCar1 = SportCar(60, "blue", "Ferarri", False)
    workCar1 = WorkCar(60, "black", "MAN", False)
    policeCar1 = PoliceCar(60, "red", "Honda", True)
    townCar1.go()
    sportCar1.go()
    workCar1.go()
    policeCar1.go()

class Person:
    def __init__(self):
        self.health = 100
        self.damage = None
        self.armor = None

    def damageCounter(self, damage):
        self.health -= (damage - self.armor)

    def attack(self):
        return self.damage

class Player(Person):
    def __init__(self, damage, armor):
        super().__init__()
        self.damage = damage
        self.armor = armor

class Enemy(Person):
    def __init__(self, damage, armor):
        super().__init__()
        self.damage = damage
        self.armor = armor

def task2():
    player = Player(10, 10)
    enemy = Enemy(10, 5)
    while(True):
        enemy.damageCounter(player.attack())
        player.damageCounter(enemy.attack())
        if player.health == 0:
            print("enemy is winner")
            break
        elif enemy.health == 0:
            print("player is winner")
            break

class Toy:
    def __init__(self):
        self.name = "toy"
        self.color = "Any"
        self.type = "Any"

    def __str__(self):
        return f"Toy with name={self.name} and type={self.type} has been producted"

class AnimalToy(Toy):
    def __init__(self, name, color, type):
        super().__init__()
        self.name = name
        self.color = color
        self.type = type

class CartoonToy(Toy):
    def __init__(self, name, color, type):
        super().__init__()
        self.name = name
        self.color = color
        self.type = type

class Fabric:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type
        self.buyMaterials()
        self.production()
        self.coloring()

    def returnToy(self):
        return globals()[self.type](self.name, self.color, self.type)

    def buyMaterials(self):
        print("Materials purchased")

    def production(self):
        print("Toy producted")

    def coloring(self):
        print("Toy colored")
def task3():
    print(Fabric('Bear','red',"AnimalToy").returnToy())
    print(Fabric('King Lion', 'red', "CartoonToy").returnToy())

if __name__ == '__main__':
    print("------------task1-----------")
    task1()
    print("------------task2-----------")
    task2()
    print("------------task3-----------")
    task3()