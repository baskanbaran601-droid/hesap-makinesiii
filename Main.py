from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class HesapApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        buttons = [["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"], [".", "0", "C", "+"]]
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equals_button = Button(text="=", background_color=(0, 1, 0, 1))
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout

    def on_button_press(self, instance):
        if instance.text == "C": self.solution.text = ""
        else: self.solution.text += instance.text

    def on_solution(self, instance):
        if self.solution.text:
            try: self.solution.text = str(eval(self.solution.text))
            except: self.solution.text = "Hata"

if __name__ == "__main__":
    HesapApp().run()
  
