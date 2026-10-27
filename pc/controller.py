import pygame
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.241", 5000))

running = True
pygame.init()
pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

previous_action = None


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        client.sendall(b"Stop\ns")
        break


    keys = pygame.key.get_pressed()

    if not pygame.key.get_focused():
        action = "Stop"
    elif keys[pygame.K_w] and keys[pygame.K_s]:
        action = "Stop"
    elif keys[pygame.K_a] and keys[pygame.K_d]:
        action = "Stop"
    elif keys[pygame.K_w] and keys[pygame.K_d]:
       action = "Forward Right"
    elif keys[pygame.K_w] and keys[pygame.K_a]:
        action = "Forward Left"
    elif keys[pygame.K_s] and keys[pygame.K_d]:
       action = "Backward Right"
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        action = "Backward Left"
    elif keys[pygame.K_w]:
       action = "Forward"
    elif keys[pygame.K_s]:
       action = "Backward"
    elif keys[pygame.K_a]:
       action = "Left"
    elif keys[pygame.K_d]:
       action = "Right"
    else:
        action = "Stop"


    if action != previous_action:
        print(action)
        previous_action = action

    message = (action + "\n").encode()
    client.sendall(message)

    clock.tick(20)

pygame.quit()
client.close()