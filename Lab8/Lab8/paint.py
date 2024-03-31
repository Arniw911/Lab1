import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((840, 580))
    clock = pygame.time.Clock()

    radius = 5
    mode = 'black'
    lines = []
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
                        lines.append({'points': [(event.pos, mode)]})  # Add color to each point
                    elif draw_shape in ('rectangle', 'circle'):
                        lines.append({'shape': draw_shape, 'start': event.pos, 'end': event.pos, 'color': mode})
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    if draw_shape == 'line':
                        lines[-1]['points'].append((event.pos, mode))
                    elif draw_shape in ('rectangle', 'circle'):
                        lines[-1]['end'] = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:    # Red
                    mode = 'red'
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

        screen.fill((255, 255, 255))

        for line in lines:
            if 'points' in line:
                for i in range(len(line['points']) - 1):
                    drawLineBetween(screen, line['points'][i][0], line['points'][i + 1][0], radius, line['points'][i][1])
            elif 'shape' in line:
                if line['shape'] == 'rectangle':
                    pygame.draw.rect(screen, getColor(line['color']), pygame.Rect(line['start'], (line['end'][0] - line['start'][0], line['end'][1] - line['start'][1])))
                elif line['shape'] == 'circle':
                    center = line['start']
                    radius = int(((line['end'][0] - line['start'][0]) ** 2 + (line['end'][1] - line['start'][1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, getColor(line['color']), center, radius)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, start, end, width, color_mode):
    color = getColor(color_mode)
    pygame.draw.line(screen, color, start, end, width)

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

main()