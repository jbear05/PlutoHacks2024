from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.app import App
from kivy.graphics import Color, Rectangle
from test import main

class BarcodeScannerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Set background color
        with layout.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Light grey background
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)

        # Add an image/logo
        layout.add_widget(Image(source='man-throwing-paper-in-recycle-container.png', size_hint=(1, 0.2)))

        self.result_label = Label(text='Scan Result:', font_size='20sp', color=(0, 0, 0, 1))
        layout.add_widget(self.result_label)

        self.scan_button = Button(
            text='Scan Barcode',
            background_color=(0.1, 0.8, 0.1, 1),  # Green button color
            color=(1, 1, 1, 1),  # Text color
            size_hint_y=None,
            height='50dp'
        )
        self.scan_button.bind(on_press=self.scan_barcode)
        layout.add_widget(self.scan_button)

        self.input_field = TextInput(hint_text='Enter barcode manually', multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.input_field)

        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def scan_barcode(self, instance):
        result = main()  # Replace with actual scanning logic
        self.result_label.text = f'Scan Result: {result}'

if __name__ == '__main__':
    BarcodeScannerApp().run()
