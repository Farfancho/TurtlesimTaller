import sys
import rclpy

from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SetPen, TeleportRelative, TeleportAbsolute

def clear_request(node, cli, req):
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node,future)
    return None

def spawn_request(node, cli, req, x, y, theta, name):
    req.x = x
    req.y = y
    req.theta = theta
    req.name = name
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    return None

def SetPen_request(node, cli, req, r, g, b, width, off):
    req.r = r
    req.g = g
    req.b = b
    req.width = width
    req.off = off
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    return None

def TeleportAbsolute_request(node, cli, req, x, y, theta):
    req.x = x
    req.y = y
    req.theta = theta
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    return None

def TeleportRelative_request(node, cli, req, linear, angular):
    req.linear = linear
    req.angular = angular
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    return None

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('taller_tortuga')

    # Punto 1
    cli = node.create_client(Empty, 'clear')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = Empty.Request()
    response = clear_request(node, cli, req)

    # Punto 2
    x = 5
    y = 0
    theta = 1
    name = "Yepes"
    cli = node.create_client(Spawn, 'spawn')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = Spawn.Request()
    response = spawn_request(node, cli, req, float(x), float(y), float(theta), str(name))
    
    # Punto 3
    r = 255
    g = 0
    b = 0
    width = 10
    off = 0
    cli = node.create_client(SetPen, 'Yepes/set_pen')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = SetPen.Request()
    response = SetPen_request(node, cli, req, int(r), int(g), int(b), int(width), int(off))
    
    # Punto 4
    x = 0
    y = 0
    theta = 0
    cli = node.create_client(TeleportAbsolute, 'Yepes/teleport_absolute')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = TeleportAbsolute.Request()
    response = TeleportAbsolute_request(node, cli, req, float(x), float(y), float(theta))   

    # Punto 5
    linear = 2
    angular = 0
    cli = node.create_client(TeleportRelative, 'Yepes/teleport_relative')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = TeleportRelative.Request()
    response = TeleportRelative_request(node, cli, req, float(linear), float(angular))

    # Punto 6
    x = 2
    y = 2
    theta = 0
    name = "Ryuk"
    cli = node.create_client(Spawn, 'spawn')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = Spawn.Request()
    response = spawn_request(node, cli, req, float(x), float(y), float(theta), str(name))
    
    # Punto 7
    r = 0
    g = 0
    b = 0
    width = 10
    off = 1
    cli = node.create_client(SetPen, 'Ryuk/set_pen')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = SetPen.Request()
    response = SetPen_request(node, cli, req, int(r), int(g), int(b), int(width), int(off))
    
    # Punto 8
    x = 5
    y = 5
    theta = 0
    cli = node.create_client(TeleportAbsolute, 'Ryuk/teleport_absolute')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = TeleportAbsolute.Request()
    response = TeleportAbsolute_request(node, cli, req, float(x), float(y), float(theta))   

    # Punto 9
    linear = 0
    angular = 2
    cli = node.create_client(TeleportRelative, 'Ryuk/teleport_relative')
    while not cli.wait_for_service(timeout_sec=1.0):
        print("Waiting...")
    req = TeleportRelative.Request()
    response = TeleportRelative_request(node, cli, req, float(linear), float(angular))

    node.destroy_node()
    rclpy.shutdown()

if '__name__' == '__main__':
    main()
