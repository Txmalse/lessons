from memo_card_layout import (
   app, layout_card,box_Minutes,btn_Sleep,btn_Menu,
   lb_Question, lb_Correct, lb_Result,
   rbtn_1, rbtn_2, rbtn_3, rbtn_4,
   btn_OK, show_question, show_result
)
from PyQt5.QtWidgets import QWidget, QApplication
from random import choice, shuffle # перемішуватимемо відповіді у картці питання
from time import sleep
from memo_menu_window import*



class Question():
   def __init__(self, question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3, correct = 0, attempts = 0 ):
      self.question = question
      self.answer = answer
      self.wrong_answer_1 = wrong_answer_1
      self.wrong_answer_2 = wrong_answer_2
      self.wrong_answer_3 = wrong_answer_3
      self.correct = correct
      self.attempts = attempts
    
   def got_right(self):
      print("Це правильна відповідь!")
      self.correct += 1
      self.attempts += 1
    
   def got_wrong(self):
      print("Відповідь невірна!")
      self.attempts += 1


q1 = Question('Яблоко','apple','application','building','caterpillar')
q2 = Question('Дім','house','horse','hour','harry')
q3 = Question('Миша','mouse','mouth','miracle','museum')
q4 = Question('Число','number','plus','minus','amount')


question = [q1,q2,q3,q4]

def new_question():
   global cur_q
   cur_q = choice(question)
   lb_Question.setText(cur_q.question)
   





card_width, card_height = 600, 500 # початкові розміри вікна "картка"
text_wrong = 'Неправильно'
text_correct = 'Правильно'

# у цій версії напишемо в коді одне запитання та відповіді до нього
# відповідні змінні поля майбутнього об'єкта "form" (тобто. анкета)
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'


# Тепер нам потрібно показати ці дані,
# причому відповіді розподілити випадково між радіокнопками, і пам'ятати кнопку з правильною відповіддю.
# Для цього створимо набір посилань на радіокнопки та перемішаємо його
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0] # ми не знаємо, який це з радіобаттонів, але можемо покласти сюди правильну відповідь і запам'ятати це
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]


def show_data():
   ''' показує потрібну інформацію на екрані '''
   # об'єднаємо у функцію схожі дії
   lb_Question.setText(frm_question)
   lb_Correct.setText(frm_right)
   answer.setText(frm_right)
   wrong_answer1.setText(frm_wrong1)
   wrong_answer2.setText(frm_wrong2)
   wrong_answer3.setText(frm_wrong3)


def check_result():
   correct = answer.isChecked()
   if correct:
      lb_Result.setText(text_correct)
      show_result()
   else:
      incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
      lb_Result.setText(text_wrong)
      show_result()


def click_OK(self):
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if btn_OK.text() != 'Наступне питання':
      check_result()


def rest():
   win_card.hide()
   n = box_Minutes.value() * 60
   sleep(n)
   win_card.show()

btn_Sleep.clicked.connect(rest)



####################
def menu_generation():
   menu_win.show()
   win_card.hide()


btn_Menu.clicked.connect(menu_generation)
#

def back_menu():
   menu_win.hide()
   win_card.show()
btn_back.clicked.connect(back_menu)


win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')


win_card.setLayout(layout_card)
show_data()
show_question()
btn_OK.clicked.connect(click_OK)


win_card.show()
app.exec_()
