# goseek-challenge

Welcome to the GOSEEK challenge page, which is run in conjunction with the [Perception, Action, Learning Workshop](https://mit-spark.github.io/PAL-ICRA2020/) at [ICRA 2020](https://www.icra2020.org/competitions/goseek-challenge).

For this competition, participants create a reinforcement learning (RL) agent that combines perception and high-level decision-making to search for objects placed within complex indoor environments from a Unity-based simulator.
Simply put: like PACMAN, but in a realistic scene and with realistic perception capabilities.
Several data modalities are provided from both the simulator ground truth and a perception pipeline (e.g., images, depth, agent location) to enable the participants to focus on the RL/search aspects.
The contest will be hosted on the EvalAI platform, where participants will submit solutions, via docker containers run on AWS instances, for scoring.

__Outline__
1. [Task Overview](#task-overview)
2. [Logistics](#logistics)
3. [Getting Started](#getting-started)
4. [Participation](#participation)

## Task Overview

The objective of this challenge is to navigate an agent through an office environment to collect randomly-spawned fruit as quickly as possible.
Our teaser trailer (below) highlights several of the components of the challenge, such as the office environment, the target fruit, the perception pipeline, and our idealized robot's physical characteristics.

[![GOSEEK Teaser Trailer](https://img.youtube.com/vi/KXTag0xsg28/0.jpg)](https://www.youtube.com/watch?v=KXTag0xsg28)

More specifically, the agent can select from one of four actions at each decision epoch: move forward 0.5 meters, turn left 8 degrees, turn right 8 degrees, and collect fruit within 2.0 meters of the agent's current position.
Our robot is equipped with stereo cameras and an Inertial Measurement Unit (IMU), from which a state-of-the-art perception pipeline estimates three pieces of information that make up the agent's observation at each decision epoch: localization information (position and heading relative to start position), pixel-wise semantic labels for objects in the robot's field of view, and pixel-wise depth in the robot's field of view.

### Data Sources

We provide two data sources for training:

1. __Ground Truth__: The agent observes ground truth (i.e., error free) information that is provided directly from the simulator.
2. __Perception Pipeline__: The agent observes output of [Kimera](http://web.mit.edu/sparklab/2019/10/13/Kimera__an_Open-Source_Library_for_Real-Time_Metric-Semantic_Localization_and_Mapping.html), which is an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM).
Note that the types (and dimensions) of observations provided are the same as before; however, the error characteristics are now representative of a real perception system.

Participants can use either or both of these sources for training their agents.
Agent interfaces are identical between the two sources.
We'll accept online submissions against either source (see [below](#online-submission) for details) and maintain a leaderboard for both.
However, only evaluations against the __Perception Pipeline__ will be used to declare an overall competition winner.

### Evaluation

Agents are evaluated on the following criteria for each episode:

1. `r`: recall of finding target fruit when the agents selects the collect action,
1. `p`: precision of finding target fruit when the agent selects the collect action,
1. `c`: number of collisions with objects in the scene, and
1. `a`: actions taken in the episode before all target fruit are collected or time expires.

A single episode score is:
```
r + 0.1p - 0.1c/l - 0.1a/l
```
where `l` is the maximum episode length (400). Note that an episode terminates early if all fruit are collected.

We use Monte Carlo evaluations to estimate an average episode score for the competition.
Note that evaluations occur on withheld office scenes.

## Logistics

### Timeline

The timeline for the competition is as follows:

- __Now until Mid-March__: Competition software available for local testing and training by participants with __Ground Truth__ data source.
- __Mid-March__: __Perception Pipeline__ data source provided to participants. Instructions for online submissions also made available.
- __April 30__: Online submission period ends.
- __May 31__: Workshop date. Competition winner invited to provide keynote presentation.

### Announcements

Over the course of the competition, any important announcements or updates will be listed in this section.
We recommend that you follow this repository to be alerted to these announcements.

## Getting Started

Complete installation instructions can be found [here](Instructions.md), which lays out prerequisites, provides a link to download the competition simulator, and describes steps to install all required competition software.
Users can also find an example for training an RL agent here, as well.

## Participation

Participants will upload docker containers with their agents to EvalAI in order to be evaluated for the competition.
The number of submissions is limited for each user, so we highly recommend performing local evaluations prior to submitting online solutions.
This sections describes how to evaluate your agent locally, then submit online for a score.

Before proceeding, we recommend that you have read through and completed [these instructions](Instructions.md).

### Prepare submission

1. Modify `Dockerfile` as appropriate for your agent.
See [these instructions](Instructions.md#prepare-docker-submission) for modification details.
The example we've provided runs an agent that randomly selects actions at each step.

2. Build the docker image. Here we are naming the image `submission`.
```
docker build -t submission .
```

### Test locally

Use `test_locally.py` for local testing.

Assume you've named your docker image `submission` as above, then evaluate your agent with __Ground Truth__ data as follows.
```sh
python test_locally.py -s simulator/goseek-v0.1.0.x86_64 -i submission -g
```

__NOTE__: Instructions for testing your agent with the __Perception Pipeline__ will be posted shortly.

### Submit online.

__NOTE__: Instructions for submitting agents online will be available according to the competition timeline [above](#timeline).

## Acknowledgements

First, we would like to thank Rishabh Jain and the rest of the team at [EvalAI](https://evalai.cloudcv.org/) for providing their infrastructure and personal time to support this challenge. We must also acknowledge the team behind [The Habitat challenge](https://github.com/facebookresearch/habitat-challenge) for being pathfinders of RL challenges with online submissions. Their challenge and associated infrastructure was inspiration for many of our own decisions.

## Disclaimer

DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.

This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Under Secretary of Defense for Research and Engineering.

(c) 2020 Massachusetts Institute of Technology.

MIT Proprietary, Subject to FAR52.227-11 Patent Rights - Ownership by the contractor (May 2014)

The software/firmware is provided to you on an As-Is basis

Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work other than as specifically authorized by the U.S. Government may violate any copyrights that exist in this work.
