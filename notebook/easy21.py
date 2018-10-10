
# coding: utf-8

# # Construct *Easy21* Game Environment

# In[1]:


import random


# In[2]:


# CONSTANTS #
PROB_RED = 1.0 / 3.0
PROB_BLACK = 1.0 - PROB_RED
DEALER_THRESHOLD = 17
MINNUM = 1
MAXNUM = 10
BUST = 0

# condictions for "bust"
UPPER_BOUND = 21
LOWER_BOUND = 1

# rewards
WIN = 1.0
DRAW = 0.0
LOSE = -1.0
UNFINISH = 0.0

# action alias
STICK = 0
HIT = 1


# In[3]:


def _draw():
    if random.random() < PROB_RED:
        return _draw_red()
    else:
        return _draw_black()

def _draw_black():
    return random.randint(MINNUM, MAXNUM)

def _draw_red():
    return -random.randint(MINNUM, MAXNUM)


# In[4]:


def _init():
    player = _draw_black()
    dealer = _draw_black()
    return player, dealer


# In[5]:


def _bust(sum_):
    return sum_ < LOWER_BOUND or sum_ > UPPER_BOUND
    
def _hit(state):
    player, dealer = state
    # draw new card
    player += _draw()
    if _bust(player):
        reward = LOSE
        player = BUST
        done = True
    else:
        reward = UNFINISH
        done = False
    return (player, dealer), reward, done
    
def _stick(state):
    player, dealer = state
    # dealer draws
    while dealer < DEALER_THRESHOLD:
        dealer += _draw()
        if _bust(dealer):
            # player wins
            dealer = BUST
            return (player, dealer), WIN, True
            
    if player > dealer:
        reward = WIN
    elif player < dealer:
        reward = LOSE
    else:
        reward = DRAW
    return (player, dealer), reward, True


# In[6]:


class Easy21:
    def __init__(self):
        self.state = None
        self.num_actions = 2
        self.reset()
        
    def reset(self):
        self.state = _init()
        return self.state
    
    def step(self, action):
        if action == HIT:
            s, r, d = _hit(self.state)
        else:
            s, r, d = _stick(self.state)
        self.state = s
        return s, r, d, {}
    
    def render(self):
        print("Player: %d, Dealer: %d" % self.state)


# In[7]:


## quick test
env = Easy21()
s = env.reset()
assert s[0] >= MINNUM and s[1] >= MINNUM and s[0] <= MAXNUM and s[1] <= MAXNUM

s, r, d, _ = env.step(HIT)
assert s[0] == BUST or (s[0] >= LOWER_BOUND and s[0] <= UPPER_BOUND)
assert (s[1] >= MINNUM and s[1] <= MAXNUM)
assert r in [WIN, LOSE, UNFINISH, DRAW]
assert d in [True, False]

s, r, d, _ = env.step(STICK)
assert s[0] == BUST or (s[0] >= LOWER_BOUND and s[0] <= UPPER_BOUND)
assert s[1] == BUST or (s[1] >= LOWER_BOUND and s[1] <= UPPER_BOUND)
assert r in [WIN, LOSE, UNFINISH, DRAW]
assert d in [True, False]


# In[8]:


# Export this notebook as a .py file and use by other notebooks.
# if __name__ == '__main__' is a trick to skip the line when importing by other files
if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert 2_easy21-environment.ipynb --to=python --output=easy21.py')

