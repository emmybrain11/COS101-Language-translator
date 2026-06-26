import cv2


class EyeMaskerApp:

    def __init__(self):
        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # Load both Face and Eye Haar Cascades
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

        # LOAD THE CYBER PICTURE HERE (Use a .jpg to avoid complex transparency code)
        self.cyber_img = cv2.imread("cyber.png")

        if self.face_cascade.empty() or self.eye_cascade.empty():
            raise IOError("Unable to load one or more cascade classifier XML files.")

        if self.cyber_img is None:
            raise IOError("Could not load 'cyber.png'. Ensure the image is in the same folder as this script.")

    def run(self):
        print("Eye Masker Started.")
        print("Press 'd' to Quit")  # Keeping your original 'd' quit key

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame from camera.")
                break

            # Mirror the frame for a natural feel
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 1. First, detect faces
            faces = self.face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100)
            )

            for x, y, w, h in faces:
                # Isolate the Regions of Interest (ROI) for the face
                roi_gray = gray[y: y + h, x: x + w]
                roi_color = frame[y: y + h, x: x + w]

                # 2. Detect eyes within the face region
                eyes = self.eye_cascade.detectMultiScale(
                    roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15)
                )

                for ex, ey, ew, eh in eyes:
                    # --- NO NUMPY IMAGE REPLACEMENT LOGIC ---

                    # 1. Resize the cyber picture to exactly match the width (ew) and height (eh) of the detected eye
                    resized_cyber_eye = cv2.resize(self.cyber_img, (ew, eh))

                    # 2. Paste the resized image directly over the eye coordinates in the color frame
                    roi_color[ey: ey + eh, ex: ex + ew] = resized_cyber_eye

            # Display the result
            cv2.imshow("Opaque Eye Masker", frame)

            # Check for quit key (Using 'd' as you wrote it)
            if cv2.waitKey(1) & 0xFF == ord("d"):
                break

        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()  # Fixed the 'AllWindaows' typo so the script doesn't crash when you press 'd'


if __name__ == "__main__":
    app = EyeMaskerApp()
    app.run()