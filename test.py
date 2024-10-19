# import kivy
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
# from kivy.graphics import Rectangle
# import cv2
# from pyzbar import pyzbar
# import sys
# import os

# # Redirect stderr to devnull to suppress warnings
# sys.stderr = open(os.devnull, 'w')

# class BarcodeScannerApp(App):
#     def build(self):
#         self.capture = cv2.VideoCapture(0)
#         self.layout = BoxLayout(orientation='vertical')
#         self.label = Label(text="Scanning for barcodes...")
#         self.layout.add_widget(self.label)
#         self.button = Button(text="Stop Scanning", size_hint=(1, 0.1))
#         self.button.bind(on_press=self.stop_scanning)
#         self.layout.add_widget(self.button)
#         Clock.schedule_interval(self.update, 1.0 / 30.0)
#         return self.layout

#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             # Convert the frame to texture
#             buf = cv2.flip(frame, 0).tostring()
#             texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#             # Decode barcodes
#             barcodes = pyzbar.decode(frame)
#             for barcode in barcodes:
#                 barcode_data = barcode.data.decode("utf-8")
#                 self.label.text = f"Barcode: {barcode_data}"
#                 print(f"Barcode: {barcode_data}")  # Debugging output
#                 break  # Stop after the first barcode is found
#             # Display the frame in the kivy window
#             self.layout.canvas.clear()
#             with self.layout.canvas:
#                 Rectangle(texture=texture, pos=self.layout.pos, size=(frame.shape[1], frame.shape[0]))

#     def stop_scanning(self, instance):
#         self.capture.release()
#         self.label.text = "Scanning stopped."
#         Clock.unschedule(self.update)

# if __name__ == '__main__':
#     BarcodeScannerApp().run()

# test.py
import cv2
from pyzbar import pyzbar
from api import fetch_product_data, extract_and_print_data

def capture_barcode():
    cap = cv2.VideoCapture(0)
    barcode_data = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (barcode.rect.left, barcode.rect.top), 
                          (barcode.rect.left + barcode.rect.width, barcode.rect.top + barcode.rect.height), 
                          (0, 255, 0), 2)
            cv2.putText(frame, barcode_data, (barcode.rect.left, barcode.rect.top - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Barcode Scanner', frame)
        if barcode_data or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return barcode_data

def main():
    barcode = capture_barcode()
    if barcode:
        print(f"Barcode: {barcode}")
        data = fetch_product_data(barcode)
        extract_and_print_data(data)
    else:
        print("No barcode detected.")

if __name__ == "__main__":
    main()