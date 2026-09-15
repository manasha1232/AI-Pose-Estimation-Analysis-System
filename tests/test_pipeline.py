from src.pose_pipeline import PoseEstimationPipeline

def test_pipeline():
    pipeline = PoseEstimationPipeline()
    assert pipeline is not None
