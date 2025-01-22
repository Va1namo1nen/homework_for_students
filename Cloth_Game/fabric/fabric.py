from fabric.physics import Node, SubSpring

class Fabric:
    def __init__(self, height,
                 width,
                 spacing,
                 stiffness,
                 damping,
                 segment_count=5,
                 density=1):

        self.nodes = []
        self.subsprings = []


        for y in range(height):
            row = []
            for x in range(width):
                is_fixed = (y == 0)
                node = Node(x * spacing, y * spacing, fixed=is_fixed)
                row.append(node)
            self.nodes.append(row)


        for y in range(height):
            for x in range(width):
                if x < width - 1:
                    self.subsprings.append(
                        SubSpring(self.nodes[y][x],
                                  self.nodes[y][x + 1],
                                  segment_count,
                                  stiffness,
                                  damping,
                                  density)
                    )
                if y < height - 1:
                    self.subsprings.append(
                        SubSpring(self.nodes[y][x],
                                  self.nodes[y + 1][x],
                                  segment_count,
                                  stiffness,
                                  damping,
                                  density)
                    )

    def apply_gravity(self, g=9.81):
        # Gravity force to Nodes
        for row in self.nodes:
            for node in row:
                if not node.fixed:
                    node.apply_force(0, g * node.mass)
        # Gravity force to SubNodes
        for subspring in self.subsprings:
            for node in subspring.nodes:
                if not node.fixed:
                    node.apply_force(0, g * node.mass)

    def update(self, dt):
        # Forces to SubSprings
        for subspring in self.subsprings:
            subspring.apply_forces()
        # Update Nodes
        for row in self.nodes:
            for node in row:
                node.update(dt)
        # Update SubNodes
        for subspring in self.subsprings:
            subspring.update(dt)
