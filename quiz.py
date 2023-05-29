
from tkinter import *
from tkinter import messagebox as mb
import json
class Quiz:
	def __init__(self):
		
		
		self.q_no=0
		self.display_title()
		self.display_question()
		
		
		self.opt_selected=IntVar()# opt_selected holds an integer value which is used for
		# selected option in a question.
		
		
		self.opts=self.radio_buttons()  # displaying radio button for the current question and used to
		# display options for the current question
		
		
		self.display_options()# display options for the current question
		
		
		self.buttons()# displays the button for next and exit.
		
		
		self.data_size=len(question)# no of questions
		
		
		self.correct=0# keep a counter of correct answers


	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True
	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			
			self.correct += 1
		

		self.q_no += 1
		if self.q_no==self.data_size:
			
			self.display_result()
			
			
			root.destroy()
		else:
			
			self.display_question()
			self.display_options()
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(root, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("impact",16,))
		
		# placing the button on the screen
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(root, text="Quit The Game", command=root.destroy,
		width=15,bg="blue", fg="white",font=("impact",14,))
		
		# placing the Quit button on the screen
		quit_button.place(x=600,y=2)
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question on the screen
	def display_question(self):
		
		# setting the Question properties
		q_no = Label(root, text=question[self.q_no], width=60,
		font=( 'impact' ,16, ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(root, text="M.sheharayar QUIZ GAME",
		width=50, bg="black",fg="white", font=("impact", 20, ))
		
		# place of the title
		title.place(x=0, y=2)


	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(root,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list

# Create a GUI Window
root = Tk()
root.geometry("800x450")
root.title("Quiz game")# set the title of the Window


with open('Data.json') as f:
	data = json.load(f)# get the data from the json file

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

quiz = Quiz()
root.mainloop()
