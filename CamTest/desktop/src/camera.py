import cv2

class CameraTester:
    def list_cameras(self):
        """List all available cameras."""
        index = 0
        cameras = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.isOpened():
                break
            cameras.append(f"Camera {index}")
            cap.release()
            index += 1
        return cameras

    def test_camera(self, index):
        """Test a specific camera and return metadata."""
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            return {"status": "Failed to open camera"}
        
        # Get metadata
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        cap.release()
        return {
            "status": "Success",
            "resolution": f"{width}x{height}",
            "frame_rate": fps
        }