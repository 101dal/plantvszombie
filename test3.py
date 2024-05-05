from utils.GameObjects import zombies

z = zombies[0].spawn(0,0)
for i in range(10):
    z.texture.next_frame()
    print(f"current animation index: {z.texture.current_animation_index} | Current frame: {z.texture.current_animation.time}")
    
print("---------------------------------------")

z.takeDamage(400)
for i in range(10):
    z.texture.next_frame()
    print(f"current animation index: {z.texture.current_animation_index} | Current frame: {z.texture.current_animation.time}")
    