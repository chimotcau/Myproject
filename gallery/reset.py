# restarting game
def reset_game(pipe_group, flappy, y):
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(y / 2)
    score = 0
    return score
