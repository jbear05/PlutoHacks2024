from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from test import main

# Set the window size
Window.size = (400, 400)

class BarcodeScannerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Set the background color to tan
        with self.layout.canvas.before:
            Color(0.82, 0.70, 0.55, 1)  # Tan color (RGB)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Add an image at the top
        self.logo = Image(source='man-throwing-paper-in-recycle-container.png', size_hint=(1, 0.4))  # Adjust size_hint for image height
        self.layout.add_widget(self.logo)

        # Create a label to display scanned barcode
        self.scanned_label = Label(
            text='Scan a barcode',
            font_size='24sp',
            color=(0, 0, 0, 1),  # Black color
            halign='center',
            valign='middle'
        )
        self.scanned_label.bind(size=self.scanned_label.setter('text_size'))
        self.layout.add_widget(self.scanned_label)

        # Text input for scanned barcode (for manual input)
        self.input_barcode = TextInput(
            hint_text='Enter barcode manually',
            multiline=False,
            font_size='18sp',
            size_hint_y=None,
            height=60,  # Increased height
            background_color=(1, 1, 1, 1),  # White background
            foreground_color=(0, 0, 0, 1),  # Black text
            padding=(10, 10)
        )
        self.layout.add_widget(self.input_barcode)

        # Button to simulate scanning with a lighter green color
        self.scan_button = Button(
            text='Scan Barcode',
            size_hint=(1, 0.2),
            background_color=(0.4, 0.8, 0.4, 1),  # Lighter green background
            color=(0, 0, 0, 1),  # Black text
            font_size='20sp'
        )
        self.scan_button.bind(on_press=self.scan_barcode)
        self.layout.add_widget(self.scan_button)

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def scan_barcode(self, instance):
        # Replace with actual barcode scanning logic
        materials, info, barcode = main()
        self.scanned_label.text = f"Barcode: {barcode}\n{"\n".join(materials)}\n{"\n".join(info)}"
        

if __name__ == '__main__':
    BarcodeScannerApp().run()
