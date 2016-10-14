# EXPERIMENTAL: all may be removed soon

from gym.benchmarks import scoring
from gym.benchmarks.registration import register_benchmark

register_benchmark(
    id='Atari7Pixel-v0',
    scorer=scoring.ClipTo01ThenAverage(),
    name='Atari7Pixel',
    description='7 Atari games, with pixel observations',
    task_groups={
        'BeamRider-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Breakout-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Enduro-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Pong-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Qbert-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Seaquest-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'SpaceInvaders-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
    })

register_benchmark(
    id='Atari7Ram-v0',
    name='Atari7Ram',
    description='7 Atari games, with RAM observations',
    scorer=scoring.ClipTo01ThenAverage(),
    task_groups={
        'BeamRider-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Breakout-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Enduro-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Pong-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Qbert-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Seaquest-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'SpaceInvaders-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
    })

register_benchmark(
    id='ClassicControl2-v0',
    name='ClassicControl2',
    description='Simple classic control benchmark',
    scorer=scoring.ClipTo01ThenAverage(),
    task_groups={
        'CartPole-v0': [{
            'seeds': 1,
            'timesteps': 2000,
        }],
        'Pendulum-v0': [{
            'seeds': 1,
            'timesteps': 1000,
        }],
    })

### Autogenerated by tinkerbell.benchmark.convert_benchmark.py

register_benchmark(
    id="Mujoco10M-v0",
    name="Mujoco10M",
    description="Mujoco benchmark with 10M steps",
    scorer=scoring.ClipTo01ThenAverage(),
    task_groups={
    "Ant-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Hopper-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Humanoid-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "HumanoidStandup-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Walker2d-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ]
}
)

register_benchmark(
    id="Mujoco1M-v0",
    name="Mujoco1M",
    description="Mujoco benchmark with 1M steps",
    scorer=scoring.ClipTo01ThenAverage(),
    task_groups={
    "HalfCheetah-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Hopper-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "InvertedDoublePendulum-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "InvertedPendulum-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Reacher-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Swimmer-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ],
    "Walker2d-v1": [
        {
            "seeds": 1,
            "timesteps": 1000000
        }
    ]
}
)
