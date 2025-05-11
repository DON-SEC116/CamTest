import cv2
import sqlite3
import platform
from camera import CameraTester
from logger import Logger

def main():
    # Initialize logger
    logger = Logger(db_path="camtest.db")
    
    # Initialize camera tester
    tester = CameraTester()
    
    # Detect OS
    os_type = platform.system()
    print(f"Running on {os_type}")
    
    # Test all available cameras
    cameras = tester.list_cameras()
    for idx, cam in enumerate(cameras):
        print(f"Testing Camera {idx}: {cam}")
        metadata = tester.test_camera(idx)
        logger.log_result({
            "camera_id": idx,
            "os": os_type,
            "resolution": metadata.get("resolution", "N/A"),
            "frame_rate": metadata.get("frame_rate", "N/A"),
            "status": metadata.get("status", "Unknown")
        })

if __name__ == "__main__":
    main()