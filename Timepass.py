import time
import kivy
from kivy.uix.label import Label
from kivy.app import  App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import  Button
import turtle

class Grid_layout(GridLayout):
	def  layout(self,**kwargs):
		super(Grid_layout,self).__init__()
		self.cols = 2
		self.add_widget(Label(text="Name of the Person : "))
		self.p_name = TextInput(multiline = False)
		self.add_widget(self.p_name)
		
		self.add_widget(Label(text="Enter ur age : "))
		self.p_age = TextInput(multiline= False)
		self.add_widget(self.p_age)
		
		self.add_widget(Label(text="What Shape u want to see(circle,square,star) :  "))
		self.p_shape = TextInput(multiline= False)
		self.add_widget(self.p_shape)
		
		self.press= Button(text= "Clich here to continue")
		self.press.bind(on_press = self.button)
		self.add_widget(self.press)
		
	def button(self,instance):
		print("Submitted")
	
class Shape(Grid_layout):
		def shape_check(self,instance):
			if self.p_shape =='circle':
				circle = turtle.Turtle()
				circle.color('red','black')
				circle.speed(100)
				circle.begin_fill()
				for i in range(200):
					circle.forward(15)
					circle.right(3.6)
				circle.end_fill()	
				turtle.done()
			elif self.p_shape =='square':
				square= turtle.Turtle()
				square.color('blue','white')
				square.speed(100)
				square.begin_fill()
				for i in range(10):
					square.forward(100)
					square.left(90)
				square.end_fill()
				turtle.done()
			
			elif self.p_shape =='star':
				star = turtle.Turtle()
				star.color('yellow','red')
				star.speed(100)
				for i in range(100):
					star.forward(100)
					star.right(135)
				star.end_fill()
				turtle.done()
				
				
		
class Main(App):
	def main(self):
		return Grid_layout()
		
if __name__=="__main__":
		Main().run()
		