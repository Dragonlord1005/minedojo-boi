import minedojo

env = minedojo.make(task_id="harvest_milk", image_size=(160, 256))

obs = env.reset()


for i in range(10):
    act = env.action_space.no_op()
    act[0] = 1
    if i % 10 == 0:
        act[2] = 1
    next_obs, reward, done, info = env.step(act)

env.close()
