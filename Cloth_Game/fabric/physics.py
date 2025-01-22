import math

class Node:
    def __init__(self, x, y, mass=1, fixed=True):
        # Positions
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        # Mass
        self.mass = mass
        # Fixed
        self.fixed = fixed
        # Velocities
        self.vx = 0
        self.vy = 0
        # Accelerations
        self.ax = 0
        self.ay = 0

    def apply_force(self, fx, fy):
        if not self.fixed:
            self.ax += fx / self.mass
            self.ay += fy / self.mass

    def update(self, dt):
        if not self.fixed:
            # Velocity update
            self.vx += self.ax * dt
            self.vy += self.ay * dt
            # Position update
            self.x += self.vx * dt
            self.y += self.vy * dt
        else:
            self.x = self.initial_x
            self.y = self.initial_y

        self.ax, self.ay = 0, 0


class Spring:
    def __init__(self, node_a, node_b, rest_length, stiffness, damping=1):
        # Nodes
        self.node_a = node_a
        self.node_b = node_b
        self.rest_length = rest_length
        self.stiffness = stiffness
        self.damping = damping

    def apply_spring_force(self):
        dx = self.node_b.x - self.node_a.x
        dy = self.node_b.y - self.node_a.y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance == 0:
            return
        # Forces
        force_magnitude = self.stiffness * (distance - self.rest_length)
        fx = force_magnitude * (dx / distance)
        fy = force_magnitude * (dy / distance)
        # Relative velocities
        relative_vx = self.node_b.vx - self.node_a.vx
        relative_vy = self.node_b.vy - self.node_a.vy
        # Damping forces
        damping_force_x = -self.damping * relative_vx
        damping_force_y = -self.damping * relative_vy
        # Resulting forces
        fx += damping_force_x
        fy += damping_force_y
        # Force apply
        self.node_a.apply_force(fx, fy)
        self.node_b.apply_force(fx, fy)

class SubSpring:
    def __init__(self, start_node, end_node, segment_count, stiffness, damping, density):
        self.nodes = []
        self.springs = []
        segment_length = math.sqrt((end_node.x - start_node.x)**2 + (end_node.y - start_node.y)**2) / segment_count

        # Node creation
        for i in range(segment_count + 1):
            t = i / segment_count
            x = start_node.x * (1 - t) + end_node.x * t
            y = start_node.y * (1 - t) + end_node.y * t
            node = Node(x, y, mass=density * segment_length)
            self.nodes.append(node)

        # Fixation
        is_fixed = start_node.fixed or end_node.fixed
        node = Node(x, y, mass=density * segment_length, fixed=is_fixed)
        self.nodes.append(node)

        # Spring creation
        for i in range(segment_count):
            self.springs.append(Spring(self.nodes[i], self.nodes[i + 1], segment_length, stiffness, damping))

    def apply_forces(self):
        for spring in self.springs:
            spring.apply_spring_force()

    def update(self, dt):
        for node in self.nodes:
            node.update(dt)