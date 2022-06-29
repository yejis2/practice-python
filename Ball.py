class Ball:
    def __init__(self, size, color, direction):
        self.size = size
        self.color = color
        self.direction = direction

    def __str__(self):
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball:)"
        return msg

    # method
    def bounce(self):
        if self.direction == 'down':
            self.direction == 'up'
        else:
            self.direction = 'down'
        print("Bounce to", self.direction)


# 객체 생성
myBall = Ball('small', 'Red', 'down')
yourBall = Ball('small', 'Red', 'up')

# 공 튕기기
for i in range(0, 3):
    myBall.bounce()
    yourBall.bounce()

print(myBall)
