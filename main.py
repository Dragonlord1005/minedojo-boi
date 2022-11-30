import minedojo

env = minedojo.make(task_id="harvest_milk", image_size=(160, 256))

obs = env.reset()

next_obs, reward, done, info = env.step(action)