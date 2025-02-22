from flask import Flask, send_file, jsonify, request
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Int64, Bool, String
import threading

app = Flask(__name__)

# Stockage des valeurs des capteurs
capteurs = {
    "temperature": 0.0,
    "luminosite": 0,
    "presence": False
}

class CapteursSubscriber(Node):
    def __init__(self):
        super().__init__('capteurs_listener')

        # Souscription aux topics ROS2
        self.create_subscription(Float32, 'data_temp', self.temperature_callback, 10)
        self.create_subscription(Float32, 'data_lum', self.luminosite_callback, 10)
        self.create_subscription(Bool, 'data_presence_portail', self.presence_callback, 10)

        # Publisher pour les commandes de contrôle
        self.clim_publisher = self.create_publisher(String, 'control_clim', 10)
        self.chauffage_publisher = self.create_publisher(String, 'control_chauffage', 10)
        self.volets_publisher = self.create_publisher(String, 'control_volets', 10) 

    def temperature_callback(self, msg):
        capteurs["temperature"] = msg.data

    def luminosite_callback(self, msg):
        capteurs["luminosite"] = msg.data

    def presence_callback(self, msg):
        capteurs["presence"] = msg.data

    def publish_clim_command(self, action):
        msg = String()
        msg.data = "ON" if action == "on" else "OFF"
        self.clim_publisher.publish(msg)

    def publish_chauffage_command(self, action):
        msg = String()
        msg.data = "ON" if action == "on" else "OFF"
        self.chauffage_publisher.publish(msg)

    def publish_volets_command(self, action):
        msg = String()
        msg.data = "OPEN" if action == "OPEN" else "CLOSE"  # Actions pour les volets
        self.volets_publisher.publish(msg)

# Créer une instance de CapteursSubscriber
capteurs_node = None

def start_ros2():
    global capteurs_node
    rclpy.init()
    capteurs_node = CapteursSubscriber()
    rclpy.spin(capteurs_node)
    rclpy.shutdown()

threading.Thread(target=start_ros2, daemon=True).start()

# 🖥 Route pour afficher la page HTML
@app.route('/')
def index():
    return send_file('index.html')

# 📡 API pour récupérer les valeurs des capteurs
@app.route('/data')
def get_data():
    return jsonify(capteurs)

# API pour contrôler la climatisation
@app.route('/toggle_clim', methods=['POST'])
def control_clim():
    data = request.get_json()
    action = data.get('action', 'on')  
    if capteurs_node:
        capteurs_node.publish_clim_command(action)
    return jsonify({"status": "success", "message": f"Climatisation {action}"})

# API pour contrôler le chauffage
@app.route('/toggle_chauffage', methods=['POST'])
def control_chauffage():
    data = request.get_json()
    action = data.get('action', 'on')  
    if capteurs_node:
        capteurs_node.publish_chauffage_command(action)
    return jsonify({"status": "success", "message": f"Chauffage {action}"})

# API pour contrôler les volets
@app.route('/toggle_volets', methods=['POST'])
def control_volets():
    data = request.get_json()
    action = data.get('action', 'OPEN')  
    if capteurs_node:
        capteurs_node.publish_volets_command(action)
    return jsonify({"status": "success", "message": f"Volets {action}"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
