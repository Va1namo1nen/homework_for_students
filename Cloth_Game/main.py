if __name__ == "__main__":
    from fabric.fabric import Fabric
    from fabric.visualizer import FabricVisualizer

    # Создаём ткань
    fabric = Fabric(
        height=10, width=15, spacing=20, stiffness=10, damping=1, segment_count=5, density=0.1
    )

    # Запускаем визуализацию
    visualizer = FabricVisualizer(fabric)
    visualizer.run()