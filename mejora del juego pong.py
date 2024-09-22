difficulty = 'medium'  # Por defecto 'medium', se puede cambiar a 'easy', 'medium', 'hard'
difficulty_speeds = {
    'easy': 4,
    'medium': 6,
    'hard': 8
}


def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = difficulty_speeds[difficulty]  # Usar la velocidad según la dificultad
    ball_dy = py5.random(-3, 3)
    paddle1_y = py5.height / 2 - paddle_height / 2
    paddle2_y = py5.height / 2 - paddle_height / 2
    player1_score = 0
    player2_score = 0


def increase_ball_speed():
    global ball_dx, ball_dy
    if ball_dx > 0:
        ball_dx += 0.1  # Aumentar la velocidad en cada iteración
    else:
        ball_dx -= 0.1
    if ball_dy > 0:
        ball_dy += 0.05
    else:
        ball_dy -= 0.05


def draw():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score

    py5.background(0)

 
    py5.rect(30, paddle1_y, paddle_width, paddle_height)  # Pala izquierda
    py5.rect(py5.width - 30 - paddle_width, paddle2_y, paddle_width, paddle_height)  # Pala derecha


    py5.ellipse(ball_x, ball_y, ball_size, ball_size)


    py5.text_size(32)
    py5.text_align(py5.CENTER)
    py5.fill(255)
    py5.text(f"{player1_score} - {player2_score}", py5.width / 2, 40)


    ball_x += ball_dx
    ball_y += ball_dy


    increase_ball_speed()

 
    if ball_y <= ball_size / 2 or ball_y >= py5.height - ball_size / 2:
        ball_dy *= -1

 
    if ball_x - ball_size / 2 <= 30 + paddle_width:
        if paddle1_y < ball_y < paddle1_y + paddle_height:
            ball_dx *= -1
            ball_x = 30 + paddle_width + ball_size / 2
    if ball_x + ball_size / 2 >= py5.width - 30 - paddle_width:
        if paddle2_y < ball_y < paddle2_y + paddle_height:
            ball_dx *= -1
            ball_x = py5.width - 30 - paddle_width - ball_size / 2


    if ball_x < 0:
        player2_score += 1
        reset_ball()
    if ball_x > py5.width:
        player1_score += 1
        reset_ball()


    if 'w' in keys and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if 's' in keys and paddle1_y < py5.height - paddle_height:
        paddle1_y += paddle_speed
    if 'o' in keys and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if 'l' in keys and paddle2_y < py5.height - paddle_height:
        paddle2_y += paddle_speed
