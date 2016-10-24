'''
Created on 24.10.2016

@author: yacoub
'''
ball_price = 0.9

for index  in range(1, 21):
    ball = ''
    if index ==1:
        ball = 'ball'
    else:
        ball = 'balls'
    print ("Price of %s %s is %1.1f Euro" % (index, ball ,round(index * ball_price ,1)))

