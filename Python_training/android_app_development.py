from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

#For reference:- https://readthedocs.org/projects/pythonic-cs1-build-a-mobile-app/downloads/pdf/latest/

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        
        s = Scatter()
        l = Label(text="Hello!",
                  font_size=50)

        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == "__main__":
    TutorialApp().run()