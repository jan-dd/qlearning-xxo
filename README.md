# qlearning-xxo

A neural network trained to play xxo by playing against scripted agents, using reinforcement learning with keras and qlearning4k.

Just run

    learn-and-play-xxo.py

which will first train the network and then you can play against it.

qlearning4k can be found here:
https://github.com/farizrahman4u/qlearning4k

qlearning-xxo works fine with older keras versions. With python3, qlearning4k throws an error with certain (newer) keras versions, see also: https://github.com/farizrahman4u/qlearning4k/issues/22
I added a file

    learn-and-play-xxo-safe.py

which catches the exceptions, and overrides one compatibility check, but hopefully, this file is not needed for future versions of qlearning4k.
