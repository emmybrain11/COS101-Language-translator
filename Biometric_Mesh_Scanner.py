import cv2
import mediapipe as mp
import math
import random


class BiometricMeshScanner:
    def __init__(self):
        # Initialize video capture interface
        self.cap = cv2.VideoCapture(0)

        # Initialize MediaPipe Face Mesh solutions
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,  # Activates high-fidelity iris and lip tracking
            min_detection_confidence=0.6,  # Strictness threshold for initial detection
            min_tracking_confidence=0.6  # Strictness threshold for frame-to-frame tracking
        )

        # Setup telemetry animation tracking variables
        self.frame_count = 0
        self.system_status = "INITIALIZING SYSTEM..."
        self.biometric_match_pct = 0.0

    def run(self):
        print("[+] Accessing Biometric Interface Engine...")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("[-] Hardware Fault: Unable to fetch video buffer.")
                break

            self.frame_count += 1
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape

            # Convert color space from BGR to RGB (MediaPipe pipeline requirement)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_frame)

            # Draw persistent HUD overlay boundary
            cv2.rectangle(frame, (20, 20), (width - 20, height - 20), (0, 85, 0), 1)

            if results.multi_face_landmarks:
                # Update biometric telemetry data
                self.system_status = "SCANNING BIOMETRIC PROFILE..."
                if self.frame_count % 5 == 0 and self.biometric_match_pct < 99.4:
                    self.biometric_match_pct += random.uniform(1.5, 4.2)
                    if self.biometric_match_pct > 100.0: self.biometric_match_pct = 100.0

                for face_landmarks in results.multi_face_landmarks:
                    # Extract raw coordinates list for vector operations
                    landmarks = face_landmarks.landmark

                    # 1. Manually iterate and draw the interconnected mesh graph topology
                    # FACEMESH_TESSELLATION defines exactly how the 468+ points link together to form triangles
                    for connection in self.mp_face_mesh.FACEMESH_TESSELLATION:
                        start_idx = connection[0]
                        end_idx = connection[1]

                        # Convert normalized 0.0-1.0 coordinates to pixel integers
                        pt1 = (int(landmarks[start_idx].x * width), int(landmarks[start_idx].y * height))
                        pt2 = (int(landmarks[end_idx].x * width), int(landmarks[end_idx].y * height))

                        # Draw thin cybernetic neon-green interconnecting wireframe lines
                        cv2.line(frame, pt1, pt2, (0, 255, 68), 1)

                    # 2. Draw high-density node points on crucial structural intersections (Contour mapping)
                    for connection in self.mp_face_mesh.FACEMESH_CONTOURS:
                        idx = connection[0]
                        pt = (int(landmarks[idx].x * width), int(landmarks[idx].y * height))
                        cv2.circle(frame, pt, 1, (0, 255, 255), -1)

                    # 3. Dynamic Cinematic Scanning Plane Matrix
                    # Generates a linear gradient sweeping bar using standard sine interpolation
                    scan_y = int((math.sin(self.frame_count * 0.08) + 1) * 0.5 * height)
                    cv2.line(frame, (25, scan_y), (width - 25, scan_y), (0, 255, 255), 2)

            else:
                # Fallback state when face leaves the sensor bounds
                self.system_status = "TARGET ACQUISITION LOST - SCANNING..."
                self.biometric_match_pct = max(0.0, self.biometric_match_pct - 10.0)

            # Render Cinematic HUD Metrics Telemetry Text
            cv2.putText(frame, f"STATUS: {self.system_status}", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"VECTOR GRAPH MATCH: {self.biometric_match_pct:.2f}%", (40, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"NODES MAPPED: 478/478 REAL-TIME", (40, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 255), 1)

            cv2.imshow("Biometric Mesh Core Engine", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    scanner = BiometricMeshScanner()
    scanner.run()