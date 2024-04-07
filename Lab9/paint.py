import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((840, 580))
    clock = pygame.time.Clock()

    radius = 5
    mode = 'black'
    shapes = []
    is_drawing = False
    draw_shape = 'line'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_drawing = True
                    if draw_shape == 'line':
                        shapes.append({'points': [(event.pos, mode)]})  # Add color to each point
                    else:
                        shapes.append({'shape': draw_shape, 'start': event.pos, 'end': event.pos, 'color': mode})
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    if draw_shape == 'line':
                        shapes[-1]['points'].append((event.pos, mode))
                    else:
                        shapes[-1]['end'] = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:    # Red
                    mode = 'red'
                elif event.key == pygame.K_1:  # Black
                    mode = 'black'
                elif event.key == pygame.K_g:  # Green
                    mode = 'green'
                elif event.key == pygame.K_b:  # Blue
                    mode = 'blue'
                elif event.key == pygame.K_e:  # Eraser
                    mode = 'eraser'
                elif event.key == pygame.K_l:  # Line
                    draw_shape = 'line'
                elif event.key == pygame.K_c:  # Circle
                    draw_shape = 'circle'
                elif event.key == pygame.K_t:  # Rectangle
                    draw_shape = 'rectangle'
                elif event.key == pygame.K_s:  # Square
                    draw_shape = 'square'
                elif event.key == pygame.K_y:  # Right triangle
                    draw_shape = 'right_triangle'
                elif event.key == pygame.K_q:  # Equilateral triangle
                    draw_shape = 'equilateral_triangle'
                elif event.key == pygame.K_m:  # Rhombus
                    draw_shape = 'rhombus'

        screen.fill((255, 255, 255))

        for shape in shapes:
            if 'points' in shape:
                for i in range(len(shape['points']) - 1):
                    drawLineBetween(screen, shape['points'][i][0], shape['points'][i + 1][0], radius, shape['points'][i][1])
            elif 'shape' in shape:
                drawShape(screen, shape)

        displayInstructions(screen)
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, start, end, width, color_mode):
    color = getColor(color_mode)
    pygame.draw.line(screen, color, start, end, width)

def drawShape(screen, shape):
    color = getColor(shape['color'])
    if shape['shape'] == 'rectangle':
        pygame.draw.rect(screen, color, pygame.Rect(shape['start'], (shape['end'][0] - shape['start'][0], shape['end'][1] - shape['start'][1])))
    elif shape['shape'] == 'circle':
        center = shape['start']
        radius = int(((shape['end'][0] - shape['start'][0]) ** 2 + (shape['end'][1] - shape['start'][1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, center, radius)
    elif shape['shape'] == 'square':
        side = max(abs(shape['end'][0] - shape['start'][0]), abs(shape['end'][1] - shape['start'][1]))
        pygame.draw.rect(screen, color, pygame.Rect(shape['start'], (side, side)))
    elif shape['shape'] == 'right_triangle':
        points = [shape['start'], shape['end'], (shape['start'][0], shape['end'][1])]
        pygame.draw.polygon(screen, color, points)
    elif shape['shape'] == 'equilateral_triangle':
        height = abs(shape['end'][1] - shape['start'][1])
        width = int(height / (math.sqrt(3)/2))
        points = [shape['start'], (shape['start'][0] + width // 2, shape['end'][1]), (shape['start'][0] - width // 2, shape['end'][1])]
        pygame.draw.polygon(screen, color, points)
    elif shape['shape'] == 'rhombus':
        dx = (shape['end'][0] - shape['start'][0]) // 2
        dy = (shape['end'][1] - shape['start'][1]) // 2
        points = [(shape['start'][0], shape['start'][1] + dy), (shape['start'][0] + dx, shape['start'][1]), (shape['start'][0], shape['start'][1] - dy), (shape['start'][0] - dx, shape['start'][1])]
        pygame.draw.polygon(screen, color, points)

def getColor(color_mode):
    if color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'black':
        return (0, 0, 0)
    elif color_mode == 'eraser':
        return (255, 255, 255)
    else:
        return (0, 0, 0)

def displayInstructions(screen):
    font = pygame.font.SysFont('Arial', 20)
    instructions = [
        "Press 'L' for Line",
        "Press 'C' for Circle",
        "Press 'T' for Rectangle",
        "Press 'S' for Square",
        "Press 'Y' for Right Triangle",
        "Press 'Q' for Equilateral Triangle",
        "Press 'M' for Rhombus",
        "Press 'R' for Red",
        "Press 'G' for Green",
        "Press 'B' for Blue",
        "Press '1' for Black",
        "Press 'E' for Eraser",
    ]
    y = 10
    for instruction in instructions:
        text = font.render(instruction, True, (0, 0, 0))
        screen.blit(text, (10, y))
        y += 25

if __name__ == '__main__':
    main()

