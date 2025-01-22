import pygame
import sys

class FabricVisualizer:
    def __init__(self, fabric, screen_size=(1920, 1080), scale=10):
        self.fabric = fabric
        self.screen_size = screen_size
        self.scale = scale
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Fabric Visualizer')
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((255, 255, 255))

        for subspring in self.fabric.subsprings:
            for spring in subspring.springs:
                start = (int(spring.node_a.x * self.scale), int(spring.node_a.y * self.scale))
                end = (int(spring.node_b.x * self.scale), int(spring.node_b.y * self.scale))
                pygame.draw.line(self.screen, (0, 0, 0), start, end, 1)

        for row in self.fabric.nodes:
            for node in row:
                x = int(node.x * self.scale)
                y = int(node.y * self.scale)
                pygame.draw.circle(self.screen, (0, 0, 255), (x, y), 3)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.fabric.apply_gravity()
            self.fabric.update(0.016)
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()