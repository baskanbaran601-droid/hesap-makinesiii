from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HesapMakinesi(App):
    def build(self):
        ana_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Yapımcılar
        yapimcilar = Label(
            text="Yapımcılar: Semih ve Baran",
            size_hint_y=None,
            height=100,
            color=(0, 1, 1, 1),
            font_size=24
        )
        ana_layout.add_widget(yapimcilar)

        # Uygulama Ekranı
        ekran = Label(text="Hesap Makinesi Hazır", font_size=32)
        ana_layout.add_widget(ekran)
        
        return ana_layout

if __name__ == '__main__':
    HesapMakinesi().run()
    
