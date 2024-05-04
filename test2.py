from creatures.Zombie import Zombie
from utils.TexturedObject import TexturedObject


for _ in range(1):
    texture1 = TexturedObject(["assets/test.jpg"], 1, 0)
    new_zombie = Zombie(
        name="Zombie1",
        texture=texture1,
        hitbox=(2, 2),
        speed=0.1,
        health=20, 
        damage=10)
    spawned = new_zombie.spawn(0,0)
    print(new_zombie.unique_id)
    print(spawned.unique_id)