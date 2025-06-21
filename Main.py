from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class EggClickerApp(App):
    def build(self):
        self.count = 0
        self.level = 1
        self.clicks_to_hatch = 100

        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        self.label = Label(text=f'Level {self.level} - Klikni na vajíčko {self.clicks_to_hatch}x', font_size=24)
        self.layout.add_widget(self.label)

        self.button = Button(text='🥚', font_size=80, size_hint=(1, .6))
        self.button.bind(on_press=self.on_click)
        self.layout.add_widget(self.button)

        return self.layout

    def on_click(self, instance):
        self.count += 1
        if self.count >= self.clicks_to_hatch:
            self.level += 1
            self.count = 0
            self.clicks_to_hatch += 50
            self.label.text = f'Gratuluješ! Level {self.level} - Klikni na vajíčko {self.clicks_to_hatch}x'
        else:
            self.label.text = f'Level {self.level} - Kliknuto: {self.count}/{self.clicks_to_hatch}'

if __name__ == '__main__':
    EggClickerApp().run()
