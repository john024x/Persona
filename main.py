from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList,ThreeLineAvatarListItem,ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class PersonaProjectApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark';
        screen = Screen()
        scroll = ScrollView()
        listView = MDList()
        scroll.add_widget(listView)
        for i in range (1,6):
            img = ImageLeftWidget(source = str(i) + ".jpg")
            items = ThreeLineAvatarListItem(text='Persona ' + str(i),secondary_text = 'Persona', tertiary_text='Test')
            items.add_widget(img)
            listView.add_widget(items)
        screen.add_widget(scroll)
        return screen

PersonaProjectApp().run()