
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class HesapMakinesi(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Yapimcılar: Semih ve Baran")
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    HesapMakinesi().run()
    
