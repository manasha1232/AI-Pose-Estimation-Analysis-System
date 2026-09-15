import cv2
import numpy as np

def make_side_by_side(orig, annotated):
    # Pure side-by-side stack without header bar
    h1, w1 = orig.shape[:2]
    target_h = 500
    w1_new = int(w1 * (target_h / h1))
    w2_new = int(annotated.shape[1] * (target_h / annotated.shape[0]))
    return np.hstack((cv2.resize(orig, (w1_new, target_h)), cv2.resize(annotated, (w2_new, target_h))))
