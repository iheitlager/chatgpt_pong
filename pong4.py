import pygame
import random

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the dimensions of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Set up the dimensions of the paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60

# Set up the dimensions of the ball
BALL_WIDTH = 15
BALL_HEIGHT = 15

# Set up the speed of the ball
BALL_X_SPEED = 5
BALL_Y_SPEED = 5

class PongGame:
    def __init__(self):
        pygame.init()
        
        # Set up the dimensions of the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        
        # Set up the clock
        self.clock = pygame.time.Clock()
        
        # Set up the font
        self.font = pygame.font.Font(None, 36)
        
        # Set up the paddles
        self.left_paddle = pygame.Rect(50, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        
        # Set up the ball
        self.ball = pygame.Rect(SCREEN_WIDTH / 2 - BALL_WIDTH / 2, SCREEN_HEIGHT / 2 - BALL_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)
        self.ball_x_speed = BALL_X_SPEED
        self.ball_y_speed = BALL_Y_SPEED
        
        # Set up the score
        self.left_score = 0
        self.right_score = 0
        
        # Set up the paddle color
        self.paddle_color = WHITE
    
    def print_score(self):
        score_text = self.font.render(str(self.left_score) + " - " + str(self.right_score), True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 10))
        
    def move_right_paddle(self):
        if random.randint(0, 9) >= 1:
            if self.right_paddle.centery < self.ball.centery:
                self.right_paddle.top += 5
            elif self.right_paddle.centery > self.ball.centery:
                self.right_paddle.top -= 5
    
    def draw_screen(self):
        # Draw the screen
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, self.paddle_color, self.left_paddle)
        pygame.draw.rect(self.screen, self.paddle_color, self.right_paddle)
        pygame.draw.ellipse(self.screen, WHITE, self.ball)

    def update_paddle_color(self):
        self.paddle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def game_loop(self):
        game_over = False
            
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                
            # Move the left paddle
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.left_paddle.top -= 5
            elif keys[pygame.K_DOWN]:
                self.left_paddle.top += 5
            elif keys[pygame.K_x]:
                game_over = True
            elif keys[pygame.K_r]:
                self.right_score = 0
                self.left_score = 0
                
            # Move the right paddle
            self.move_right_paddle()
                
            # Move the ball
            self.ball.left += self.ball_x_speed
            self.ball.top += self.ball_y_speed
                
            # Check if the ball has hit the top or bottom of the screen
            if self.ball.top <= 0 or self.ball.top >= SCREEN_HEIGHT - BALL_HEIGHT:
                self.ball_y_speed = -self.ball_y_speed
                
            # Check if the ball has hit the left or right paddle
            if self.ball.colliderect(self.left_paddle):
                self.ball_x_speed = -self.ball_x_speed
                self.update_paddle_color()
            elif self.ball.colliderect(self.right_paddle):
                self.ball_x_speed = -self.ball_x_speed
                self.update_paddle_color()
                
            # Check if the ball has gone off the left or right of the screen
            if self.ball.left <= 0:
                self.right_score += 1
                self.ball.left = SCREEN_WIDTH / 2 - BALL_WIDTH / 2
                self.ball.top = SCREEN_HEIGHT / 2 - BALL_HEIGHT / 2
                self.ball_x_speed = BALL_X_SPEED
                self.ball_y_speed = BALL_Y_SPEED
            elif self.ball.left >= SCREEN_WIDTH - PADDLE_WIDTH:
                self.left_score += 1
                self.ball.left = SCREEN_WIDTH / 2 - BALL_WIDTH / 2
                self.ball.top = SCREEN_HEIGHT / 2 - BALL_HEIGHT / 2
                self.ball_x_speed = -BALL_X_SPEED
                self.ball_y_speed = BALL_Y_SPEED
                
            self.draw_screen()
            self.print_score()
            pygame.display.update()
            
            # Slow down the game
            self.clock.tick(30)




if __name__ == '__main__':
    pygame.init()
    game = PongGame()
    game.game_loop()
    pygame.quit()
