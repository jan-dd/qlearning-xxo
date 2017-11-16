from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.optimizers import sgd
import xxo
from qlearning4k import Agent


class CompatibleAgent(Agent):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def check_game_compatibility(self, game):
        pass

hidden_size = 100

model = Sequential()
model.add(Flatten(input_shape=(1,27)))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(9))
model.compile(sgd(lr=.2), "mse")

game_rand = xxo.xxoboard(xxo.rand_opponent)
game_smart = xxo.xxoboard(xxo.smart_opponent)
game_int = xxo.xxoboard(xxo.int_opponent,drawmode=True)

agent = Agent(model)
cagent=CompatibleAgent(model)

for n in range(0,1):
    try:
        agent.train(game_rand,nb_epoch=300, batch_size=50, gamma=0.9, epsilon=[1, 0.1], epsilon_rate=0.5, reset_memory=False)
    except:
        print('An error occured in qlearning4k, but when the epochs ran through, the network will be trained.')
    try:
        agent.train(game_smart,nb_epoch=300, batch_size=50, gamma=0.9, epsilon=[0.2, 0.1], epsilon_rate=0.5, reset_memory=False)
    except:
        print('An error occured in qlearning4k, but when the epochs ran through, the network will be trained.')
        
cagent.play(game_int,visualize=False)
