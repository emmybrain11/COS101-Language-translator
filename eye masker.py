import cv2
import numpy as np  # Import numpy for matrix operations


class EyeMaskerApp:
    def __init__(self, hacker_image_path="cyber_eye_mask.png"):
        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # Load both Face and Eye Haar Cascades
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

        # Load the hacker image (must be a square image with an alpha channel for transparency, or a standard JPG)
        self.hacker_mask_img = cv2.imread(hacker_image_path, cv2.IMREAD_UNCHANGED)

        if self.face_cascade.empty() or self.eye_cascade.empty():
            raise IOError("Unable to load one or more cascade classifier XML files.")

        if self.hacker_mask_img is None:
            raise IOError(
                f"Unable to load hacker image file: {hacker_image_path}. Please place a PNG (with alpha) or JPG with this name in the script directory.")

    def run(self):
        print("Hacker Eye Masker Started.")
        print("Press 'q' to Quit")  # Changed to 'q' for better convention, matching the waitKey

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

            for (x, y, w, h) in faces:
                # Isolate the Regions of Interest (ROI) for the face
                roi_gray = gray[y: y + h, x: x + w]
                roi_color = frame[y: y + h, x: x + w]

                # 2. Detect eyes within the face region
                eyes = self.eye_cascade.detectMultiScale(
                    roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15)
                )

                for (ex, ey, ew, eh) in eyes:
                    # --- NEW IMAGE OVERLAY LOGIC ---

                    # Calculate radius for the mask (increased slightly to fully cover the eye)
                    radius = int(max(ew, eh) * 0.75)

                    # Determine target dimensions for the mask (double radius for a square mask over the eye)
                    mask_size = (radius * 2, radius * 2)

                    # Resize the hacker image to fit the eye size
                    resized_mask = cv2.resize(self.hacker_mask_img, mask_size, interpolation=cv2.INTER_AREA)

                    # Calculate the top-left coordinate for the overlay
                    overlay_y = ey + (eh // 2) - radius
                    overlay_x = ex + (ew // 2) - radius

                    # Handle alpha channel blending for transparency
                    if resized_mask.shape[2] == 4:  # If it's a 4-channel PNG with alpha
                        # Split channels and normalize alpha mask
                        h_patch, w_patch = mask_size
                        mask_bgr = resized_mask[:, :, :3]
                        mask_alpha = resized_mask[:, :, 3] / 255.0
                        roi_alpha = 1.0 - mask_alpha

                        # Overlay with transparency on the color ROI
                        for c in range(3):  # For B, G, R channels
                            # Robust slicing to handle edge cases where mask extends beyond ROI
                            # (Though face detection makes this rare)
                            if (overlay_y + h_patch <= roi_color.shape[0] and
                                    overlay_x + w_patch <= roi_color.shape[1] and
                                    overlay_y >= 0 and overlay_x >= 0):
                                # Blend the current color channel
                                roi_color[overlay_y: overlay_y + h_patch, overlay_x: overlay_x + w_patch, c] = (
                                    (mask_alpha * mask_bgr[:, :, c] + roi_alpha * roi_color[
                                                                                  overlay_y: overlay_y + h_patch,
                                                                                  overlay_x: overlay_x + w_patch, c])
                                ).astype(np.uint8)
                    else:  # If it's a non-transparent image (e.g., JPG)
                        # Create robust slicing and overlay
                        if (overlay_y + mask_size[1] <= roi_color.shape[0] and
                                overlay_x + mask_size[0] <= roi_color.shape[1] and
                                overlay_y >= 0 and overlay_x >= 0):
                            roi_color[overlay_y: overlay_y + mask_size[1],
                            overlay_x: overlay_x + mask_size[0]] = resized_mask
                    # --- END IMAGE OVERLAY LOGIC ---

            # Display the result (changed title for context)
            cv2.imshow("Hacker Eye Masker", frame)

            # Check for quit key
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Specify the name of your hacker picture here
    app = EyeMaskerApp(hacker_image_path="cyber_eye_mask.png")
    app.run()