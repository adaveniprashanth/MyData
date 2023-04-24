from kivy.app import App
from kivy.uix.image import Image


# For ref --> https://realpython.com/mobile-app-kivy-python/#packaging-your-app-for-android

class MainApp(App):
    def build(self):
        img = Image(source='images.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})#pos_hint will adjust data/data position
        return img


from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=40,spacing=10,orientation='vertical')
        colors = [red, green, blue, purple]

        for i in range(4):
            btn = Button(text="Button #%s" % (i+1),background_color=colors[i])

            layout.add_widget(btn)
        return layout


class MainApp1(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.09, .09),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('You pressed the button!')



from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class Calculator(App):
    def build(self):
        self.operators = ["+","-","*","/"]
        self.last_pressed_button = None

        # creating the main layout i.e full area of screen
        main_layout = BoxLayout(orientation='vertical')

        #creating the text input area to display the details
        self.solution = TextInput(multiline=False,readonly=True,halign='right',font_size=55)

        #adding the textinput to display in main layout
        main_layout.add_widget(self.solution)

        buttons = [["7", "8", "9", "/"],
                   ["4", "5", "6", "*"],
                   ["1", "2", "3", "-"],
                   [".", "0", "C", "+"],]

        for row in buttons:
            # creating a layout
            h_layout = BoxLayout()
            for label in row:
                # creating the button for each item
                button = Button(text=label,pos_hint={"center_x": 0.5, "center_y": 0.5})
                # making the button activate
                button.bind(on_press=self.on_button_press)
                # adding the button to layout(horizontal layout) which overlapped main layout
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)


        equal_button = Button(text='=',size_hint=(.5,1),pos_hint={"center_x": 0.25, "center_y": 0.5})
        equal_button.bind(on_press=self.on_solution)
        h_layout=BoxLayout(orientation='horizontal')
        # add the button to layout
        h_layout.add_widget(equal_button)
        close_button = Button(text='close app',size_hint=(.5,1),pos_hint={"center_x": 0.25, "center_y": 0.5})
        close_button.bind(on_press=self.on_close)
        h_layout.add_widget(close_button)
        # adding the horizontal layout to main layout
        main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self,instance):
        pressed_button = instance.text
        if pressed_button == "C":
            # clearing the data
            self.solution.text = ""
        else:
            if self.solution.text and (self.last_pressed_button and pressed_button in self.operators):
                # we cannot use 2 operators next to each other
                return
            elif self.solution.text == "" and pressed_button in self.operators:
                # we can not use operator as first character
                return
            else:
                self.solution.text = self.solution.text +pressed_button #adding the previous data and current pressed data

        self.last_pressed_button = pressed_button in self.operators #true if pressed button is an operator

    def on_solution(self,instance):
        text = self.solution.text
        if text:
            if text[-1] in self.operators:
                self.solution.text = text
            else:
                result = self.solution.text
                try:
                    result = str(eval(text))
                except Exception:
                    self.solution.text = text
                self.solution.text = result
    def on_close(self,instance):
        app.stop()
        Window.close()








if __name__ == '__main__':
    # app = MainApp()
    # app = HBoxLayoutExample()
    # app = MainApp1()
    app = Calculator()
    app.run()