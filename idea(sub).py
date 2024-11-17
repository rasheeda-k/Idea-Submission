import random
from geopy.distance import geodesic
from datetime import datetime, timedelta
import time
# Simulated Health Monitoring System
class HealthMonitor:
    def __init__(self, heart_rate_threshold=120, anomaly_duration_threshold=5):
        self.heart_rate_threshold = heart_rate_threshold
        self.anomaly_start_time = None
        self.anomaly_duration_threshold = anomaly_duration_threshold  # In seconds
    def get_vital_signs(self):
        """Simulate fetching real-time health data."""
        return {
            "heart_rate": random.randint(60, 160),  # Random heart rate
            "timestamp": datetime.now()
        }
    def detect_anomaly(self, vital_signs):
        """Detect if health anomaly occurs based on vital signs."""
        if vital_signs["heart_rate"] > self.heart_rate_threshold:
            if not self.anomaly_start_time:
                self.anomaly_start_time = vital_signs["timestamp"]
            elif (vital_signs["timestamp"] - self.anomaly_start_time).seconds >= self.anomaly_duration_threshold:
                return True
        else:
            self.anomaly_start_time = None
        return False
    # Emergency Navigation System
class EmergencyNavigation:
    def __init__(self, current_location):
        self.current_location = current_location  # Current GPS location
        self.hospitals = [
            {"name": "General Hospital", "location": (40.7580, -73.9855)},
            {"name": "City Medical Center", "location": (40.7610, -73.9755)},
        ]
    def find_nearest_hospital(self):
        """Find the nearest hospital based on geodesic distance."""
        distances = [
            (hospital, geodesic(self.current_location, hospital["location"]).miles)
            for hospital in self.hospitals
        ]
        nearest_hospital = min(distances, key=lambda x: x[1])
        return nearest_hospital
    def navigate_to(self, destination):
        """Simulate navigation to the destination."""
        print(f"🗺️ Navigating to {destination['name']} located at {destination['location']}...")
        for _ in range(3):  # Simulating updates during navigation
            time.sleep(2)
            print("📍 Updating route based on traffic...")

# Notification System
class NotificationSystem:
    def __init__(self, emergency_contacts):
        self.emergency_contacts = emergency_contacts
    def notify_emergency_services(self, location):
        """Simulate notifying emergency services."""
        print(f"🚨 Alerting emergency services! Vehicle located at {location}.")
    def notify_family(self, location):
        """Simulate notifying family members."""
        for contact in self.emergency_contacts:
            print(f"📢 Notifying {contact}: Vehicle is at {location}.")
# Safe Parking System
class SafeParkingSystem:
    def activate_hazard_lights(self):
        """Simulate activating hazard lights."""
        print("⚠️ Hazard lights activated.")
    def park_vehicle(self):
        """Simulate parking the vehicle safely."""
        print("🚗 Vehicle safely parked.")
# Main Automated Emergency System
class AutomatedEmergencyNavigationSystem:
    def __init__(self, initial_location, emergency_contacts):
        self.health_monitor = HealthMonitor()
        self.navigation = EmergencyNavigation(current_location=initial_location)
        self.notifications = NotificationSystem(emergency_contacts)
        self.safe_parking = SafeParkingSystem()
    def start_monitoring(self):
        """Start monitoring health and handle emergencies if detected."""
        print("🚗 Automated Emergency Navigation System is active.")
        while True:
            vital_signs = self.health_monitor.get_vital_signs()
            print(f"[{vital_signs['timestamp']}] Heart Rate: {vital_signs['heart_rate']} BPM")

            if self.health_monitor.detect_anomaly(vital_signs):
                print("⚠️ Health anomaly detected! Activating Emergency Protocol...")
                self.handle_emergency()
                break
            time.sleep(2)  # Simulate real-time monitoring delay
    def handle_emergency(self):
        """Handle emergency by navigating to safety and notifying contacts."""
        nearest_hospital, distance = self.navigation.find_nearest_hospital()
        print(f"🚑 Nearest hospital: {nearest_hospital['name']} ({distance:.2f} miles away)")
        # Navigate to hospital
        self.navigation.navigate_to(nearest_hospital)
        # Notify emergency services and family
        self.notifications.notify_emergency_services(self.navigation.current_location)
        self.notifications.notify_family(self.navigation.current_location)
        # Simulate safe parking
        self.safe_parking.activate_hazard_lights()
        self.safe_parking.park_vehicle()

        print("✅ Emergency Protocol Completed.")

# Example Usage
if __name__ == "__main__":
    # Initial vehicle location (Example: New York City coordinates)
    vehicle_location = (40.730610, -73.935242)
    emergency_contacts = ["Alice", "Bob"]
    # Initialize the system
    emergency_system = AutomatedEmergencyNavigationSystem(vehicle_location, emergency_contacts)
        # Start monitoring
    emergency_system.start_monitoring()