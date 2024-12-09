import pygame 
import sys 

pygame.init() 
clock = pygame.time.Clock()  
screen = pygame.display.set_mode([600, 500]) 
base_font = pygame.font.Font(None, 32) 
user_text = '' 
input_rect = pygame.Rect(200, 200, 140, 32) 
color_active = pygame.Color('cornsilk1') 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
active = False
while True: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			pygame.quit() 
			sys.exit() 

		if event.type == pygame.MOUSEBUTTONDOWN: 
			if input_rect.collidepoint(event.pos): 
				active = True
			else: 
				active = False

		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_BACKSPACE: 
				user_text = user_text[:-1]
			else: 
				user_text += event.unicode
	screen.fill((20, 20, 20)) 

	if active: 
		color = color_active 
	else: 
		color = color_passive 
	pygame.draw.rect(screen, color, input_rect) 

	text_surface = base_font.render(user_text, True, (0, 0, 0)) 
	screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
	input_rect.w = max(100, text_surface.get_width()+10) 
	pygame.display.flip() 
	clock.tick(60) 
