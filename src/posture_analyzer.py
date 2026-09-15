import cv2
from src.geometry import calculate_angle

class ErgonomicPostureAnalyzer:
    def analyze(self, frame, landmarks):
        # Evaluates ear-shoulder-hip alignment
        pass

    def get_status(self, neck_angle, torso_angle):
        return "IMPROPER / SLOUCHED POSTURE!" if (neck_angle > 35 or torso_angle > 25) else "PROPER POSTURE"
