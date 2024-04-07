from objects.GameObjects import GameObjects


go = GameObjects()
plants = go.plants
zombies = go.zombies

# Here are all the test relative to the Plants and their ammo
plant1 = plants[0].plant(0,0)
plant2 = plants[0].plant(0,1)

print(f"Plant1: x={plant1.x} ; y={plant1.y}")
print(f"Plant2: x={plant2.x} ; y={plant2.y}")


ammo1 = plant1.spawnAmmo()
ammo2 = plant1.spawnAmmo()

ammo1.move()
ammo2.move()
ammo2.move()
ammo2.move()
ammo2.move()
ammo2.move()



print(f"Munition: x={ammo1.x} ; y={ammo1.y}")
print(f"Munition: x={ammo2.x} ; y={ammo2.y}")


# Here are all the test relative to the Zombies
zombie1 = zombies[0].spawn(10,10)
zombie2 = zombies[0].spawn(10,0)

zombie1.move()
zombie1.move()
zombie1.move()
zombie1.move()
zombie1.move()
zombie1.move()

print(f"Zombie1: x={zombie1.x} ; y={zombie1.y}")
print(f"Zombie1: x={zombie2.x} ; y={zombie2.y}")