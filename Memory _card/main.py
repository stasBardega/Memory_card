# Підключення модулів
from menu_window import *
from main_window import *

from random import choice, shuffle #виб. ранд. ел.зі списку \ перемішує елементи списку
from time import sleep

wins = [main_win, menu_win]
for win in wins:
    win.setStyleSheet('''
                      color: black;   
                      background-color: lightgreen;
                      font-size: 20px;
                      border: 0.5px solid red;
                      ''')
    
lb_Result.setStyleSheet('margin: 20px;')

# колір тексту
# колір фону
# розмір тексту
# розмір і колір рамок

# клас Питання 
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question             # питання
        self.answer = answer                 # відповідь
        self.wrong_answer1 = wrong_answer1   # непр.відп.1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True  # чи актуальне питання
        self.attempts = 0   # кільк. спроб
        self.correct = 0    # кільк. прав.відп.

    def got_right(self):
        ''' змінює статистику, отримавши правильну відповідь'''
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        ''' змінює статистику, отримавши неправильну відповідь'''
        self.attempts += 1

# питання
q1 = Question('5x5', '25', '36', '35', '24')
q2 = Question('15x10', '150', '260', '1.5', '1500')
q3 = Question('87-19', '68', '78', '69', '72')
q4 = Question('34+297', '331', '329', '312', '321')
q5 = Question('567x2', '1134', '1231', '987', '1156')
q6 = Question('214-178', '32', '34', '52', '24')
q7 = Question('342:3', '114', '112', '111', '152')
q8 = Question('254+234', '488', '345', '338', '337')
q9 = Question('500-349', '151', '1511', '149', '141')
q10 = Question('33x11', '363', '354', '346', '353')
q11 = Question('Яке з наведених чисел є простим?', '17', '9', '15', '21')
q12 = Question('Який з наведених способів є правильним для перевірки, чи є число простим?', ' Поділити число на всі прості числа, менші за квадратний корінь з цього числа.', 'Поділити число на всі числа до його половини.', 'Поділити число на 2 та на 3.', 'Поділити число на 2, 3, 4 та так далі до самого числа.')
q13 = Question('Яке з наведених визначень правильне для графа?', 'Граф це множина точок, зєднаних лініями.', 'Граф це множина векторів в просторі.', ' Граф це множина чисел, повязаних функцією.', 'Граф це геометрична фігура з трьома сторонами.')

# список з перемикачів кнопок та питань
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]
#                                         (функція що обирає випадкове запитання зі списку та показує його на екрані)
def new_question():
    global cur_question
    cur_question = choice(questions)                   #вибирає рандомне запитання

    lb_Question.setText(cur_question.question)         #встановлює текст(відповіді та запитання) на віджети
    lb_Correct.setText(cur_question.answer)

    shuffle(radio_list)                                 #перемішує кнопки(щоб не на 1 шій була завжди прав.відпов.)- змінюючи позицію в списку
    
    radio_list[0].setText(cur_question.wrong_answer1)   #розмішюємо на них знову питання
    radio_list[1].setText(cur_question.wrong_answer2)
    radio_list[2].setText(cur_question.wrong_answer3)   #в новому порядку
    radio_list[3].setText(cur_question.answer)


#                                                   (функція для перевірки результату відповіді)
def check_result():
    for ans_btn in radio_list:
        if ans_btn.isChecked():                         # вибраний вірних перемикач?
            if ans_btn.text() == lb_Correct.text():     # чи збігається текст на вибр.кпонці та текст прав.відповіді?
                cur_question.got_right()                # збільшити кільк.спроб +1
                lb_Result.setText('Правильно!')
                update_statistics()        
                break
    else:
        cur_question.got_wrong()                 #якщо не вибр.прав.відп.
        lb_Result.setText('Неправильно! :)')     #змінити надпис на НЕПРАВИЛЬНО
        update_statistics()

#                                               (функцію-обробник кнопки “Відпочити”)
def rest():
    main_win.hide()                 # приховати головний віджет    
    n = box_Minutes.value() * 60    # бере знач.від корситвача і множить на кільк. секунд
    sleep(n)                        # спить
    main_win.show()                 # потім знову показує

# ----------------------------------------------------------
#  Функції для кнопок панелі - дод.питання та статистика
# ----------------------------------------------------------
def show_menu():      
    menu_win.show()
    main_win.hide()

def back_menu():
    menu_win.hide()
    main_win.show()

def clear():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

def add_question():
    newq = Question(txt_Question.text(), txt_Answer.text(), txt_Wrong1.text(), txt_Wrong2.text(), txt_Wrong3.text())
    questions.append(newq)
    clear()

#   функція зміни(запинать та надписів на кнопках)
def switch_screen():
    if btn_OK.text() == 'Відповісти':
        check_result()   #
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        new_question() #
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
                                            # скинути вибрану радіо-кнопку
        RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана

# ----------------------------------------------------------
# Функція для оновлення статистики і вкиликати в перевірці
# ----------------------------------------------------------
def update_statistics():
    total_attempts = sum(q.attempts for q in questions)
    total_correct = sum(q.correct for q in questions)
    lbl_statistics.setText(f"Статистика:\nПравильних відповідей: {total_correct}\nЗагальна кількість спроб: {total_attempts}")

# ----------------------------------------------------------
#  Пікючення виклику функції - до кнопок
# ----------------------------------------------------------

new_question()

btn_Menu.clicked.connect(show_menu)
btn_back.clicked.connect(back_menu)
btn_clear.clicked.connect(clear)
btn_Sleep.clicked.connect(rest)
btn_OK.clicked.connect(switch_screen)
btn_add_q.clicked.connect(add_question)

main_win.show()
app.exec_()




