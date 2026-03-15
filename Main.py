from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty
from kivy.animation import Animation

class RenkliYuvarlakButon(Button):
    bg_color = ListProperty([0, 0, 0, 1])
    def __init__(self, bg_hex, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.normal_color = get_color_from_hex(bg_hex)
        self.bg_color = self.normal_color
        self.bind(pos=self.ciz, size=self.ciz)

    def ciz(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[45,])

class HesapMakinesi(App):
    def build(self):
        ana_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        yapimcilar = Label(text="Yapimcılar: Semih ve Baran", size_hint_y=0.05, color=get_color_from_hex('#FF9500'), bold=True)
        ana_layout.add_widget(yapimcilar)

        self.ekran = Label(text="0", font_size=80, size_hint_y=0.25, halign='right', valign='bottom')
        self.ekran.bind(size=self.ekran.setter('text_size'))
        ana_layout.add_widget(self.ekran)

        tuslar = GridLayout(cols=4, spacing=15, size_hint_y=0.65)
        # RENKLER: Gri (#A5A5A5), Koyu Gri (#333333), Turuncu (#FF9500)
        buton_yapisi = [
            ('C', '#A5A5A5'), ('+/-', '#A5A5A5'), ('%', '#A5A5A5'), ('÷', '#FF9500'),
            ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('x', '#FF9500'),
            ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('-', '#FF9500'),
            ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('+', '#FF9500'),
            ('0', '#333333'), (',', '#333333'), ('del', '#333333'), ('=', '#FF9500')
        ]

        for metin, renk_kodu in buton_yapisi:
            btn = RenkliYuvarlakButon(text=metin, font_size=35, bold=True, bg_hex=renk_kodu)
            btn.bind(on_press=self.tusa_basildi)
            tuslar.add_widget(btn)

        ana_layout.add_widget(tuslar)
        return ana_layout

    def tusa_basildi(self, instance):
        if instance.text == 'C': self.ekran.text = '0'
        elif instance.text == 'del': self.ekran.text = self.ekran.text[:-1] if len(self.ekran.text) > 1 else '0'
        elif instance.text == '=':
            try: self.ekran.text = str(eval(self.ekran.text.replace('x','*').replace('÷','/')))
            except: self.ekran.text = "Hata"
        else:
            self.ekran.text = instance.text if self.ekran.text == '0' else self.ekran.text + instance.text

if __name__ == '__main__':
    HesapMakinesi().run()
            
