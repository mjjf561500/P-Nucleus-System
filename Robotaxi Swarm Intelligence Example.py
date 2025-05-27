```python
# robotaxi_swarm.py: P-Nucleus Swarm Intelligence for Robotaxi Route Optimization
import time
from typing import Dict, List
from src.pnucleus_core import PNucleus
from src.swarm_interaction import SwarmInteraction

class RobotaxiSwarm:
    """Simulates P-Nucleus swarm for Robotaxi route optimization."""
    
    def __init__(self, num_vehicles: int, city: str = "Chicago"):
        """Initialize swarm with P-Nuclei and communication."""
        self.vehicles = [
            {
                "nucleus": PNucleus(db_path=f"data/vehicle_{i}.db"),
                "swarm": SwarmInteraction(f"vehicle_{i}")
            }
            for i in range(num_vehicles)
        ]
        self.city = city

    def optimize_routes(self, traffic_data: str) -> List[Dict]:
        """
        Optimize routes for all Robotaxis via nuclear resonance.
        
        Args:
            traffic_data: Description of traffic conditions.
        
        Returns:
            List of optimized routes and vehicle metadata.
        """
        results = []
        
        for vehicle in self.vehicles:
            nucleus = vehicle["nucleus"]
            swarm = vehicle["swarm"]
            
            # Generate route suggestion
            prompt = f"Optimize Robotaxi route in {self.city} under {traffic_data}"
            route = nucleus.inference(prompt, max_length=50)
            
            # Share with swarm
            swarm_data = {
                "vehicle_id": swarm.nucleus_id,
                "route": route,
                "traffic": traffic_data
            }
            swarm.publish("robotaxi/swarm", swarm_data)
            
            # Update personality based on mock feedback
            feedback = {"empathy": 0.05, "creativity": 0.02}
            personality = nucleus.update_personality(feedback": feedback})
            
            results.append({
                "vehicle_id": swarm.nucleus_id,
                "route": route,
                "personality": personality
            })
            
            time.sleep(0.5)  # Simulate network latency
        
        # Mock resonance: Aggregate routes
        final_route = self._aggregate_routes(results)
        results.append({"vehicle_id": "swarm", "route": final_route})
        
        return results

    def _aggregate_routes(self, results: List[Dict]) -> str:
        """Aggregate routes for optimal swarm path (simplified)."""
        routes = [r["route"] for r in results]
        return f"Swarm-Optimized Route: {' -> '.join(routes[:2])}"

# Demo
if __name__ == "__main__":
    swarm = RobotaxiSwarm(num_vehicles=3, city="Chicago")
    traffic = "Heavy traffic on Michigan Ave, accidents on I-90"
    results = swarm.optimize_routes(traffic)
    for result in results:
        print(f"Vehicle {result['vehicle_id']}: {result['route']}")
```