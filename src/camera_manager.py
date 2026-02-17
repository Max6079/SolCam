import threading
import time

class CameraManager:
    def __init__(self, camera_list):
        self.cameras = camera_list
        self.capture_threads = []
        self.is_running = False

    def start_capturing(self):
        self.is_running = True
        for camera in self.cameras:
            thread = threading.Thread(target=self.capture_from_camera, args=(camera,))
            thread.start()
            self.capture_threads.append(thread)

    def stop_capturing(self):
        self.is_running = False
        for thread in self.capture_threads:
            thread.join()

    def capture_from_camera(self, camera):
        while self.is_running:
            try:
                # Simulate camera capture logic
                print(f"Capturing from {camera}")
                time.sleep(1)
            except Exception as e:
                print(f"Error capturing from {camera}: {e}")
                self.reconnect_camera(camera)

    def reconnect_camera(self, camera):
        print(f"Reconnecting to {camera}...")
        time.sleep(2)  # Simulate reconnect delay
        print(f"Reconnected to {camera}")