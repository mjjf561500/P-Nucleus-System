```python
# swarm_interaction.py: P-Nucleus Wireless Collaboration (5G/V2X)
import paho.mqtt.client as mqtt
import json
import time

class SwarmInteraction:
    """Handles P-Nucleus collaboration via wireless protocols."""
    
    def __init__(self, nucleus_id, broker="broker.hivemq.com", port=1883):
        """Initialize MQTT client for swarm interaction."""
        self.nucleus_id = nucleus_id
        self.client = mqtt.Client(nucleus_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(broker, port)
        self.client.loop_start()

    def _on_connect(self, client, userdata, flags, rc):
        """Callback for connection."""
        print(f"Nucleus {self.nucleus_id} connected with code {rc}")
        self.client.subscribe("pnucleus/swarm")

    def _on_message(self, client, userdata, msg):
        """Callback for received messages."""
        try:
            payload = json.loads(msg.payload.decode())
            print(f"Nucleus {self.nucleus_id} received: {payload}")
        except json.JSONDecodeError:
            print(f"Invalid message: {msg.payload}")

    def publish(self, topic, message):
        """Publish message to swarm."""
        payload = json.dumps({
            "nucleus_id": self.nucleus_id,
            "timestamp": time.time(),
            "data": message
        })
        self.client.publish(topic, payload)
        print(f"Nucleus {self.nucleus_id} published: {message}")

    def subscribe(self, topic):
        """Subscribe to swarm topic."""
        self.client.subscribe(topic)

# Demo
if __name__ == "__main__":
    swarm = SwarmInteraction("nucleus_1")
    swarm.publish("pnucleus/swarm", "Optimize Robotaxi route: Shanghai to Beijing")
    swarm.subscribe("pnucleus/swarm")
    time.sleep(5)  # Wait for messages
    swarm.client.loop_stop()
```