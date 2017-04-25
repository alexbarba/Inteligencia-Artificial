from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
		layout = FloatLayout()
		for i in range(10):
			layout.add_widget(Button(pos_hint={'x': i/float(10), 'y': .9}, size_hint=(.1, .1),text= str(i)))
		return layout
        

TestApp().run()
