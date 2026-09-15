import cv2
from src.geometry import calculate_angle

class YogaPoseClassifier:
    def classify(self, landmarks, width):
        # Classifies Tree Pose, Warrior Pose, T-Pose
        pass

    def predict_pose(self, knee_angle, arm_span, width):
        if knee_angle < 140: return "Tree Pose"
        elif arm_span > 0.3 * width: return "Warrior Pose"
        return "T Pose"
