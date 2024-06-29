from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

main_wind = QWidget()
main_wind.resize(600,500)
main_wind.move(300,300)
main_wind.setWindowTitle('Memory Card')

#Створюємо потрібні віджети(Кнопки - таймер - надпис)

btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
btn_Ok = QPushButton("Відповісти")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
lb_Question = QLabel("")

#Створюємо панель - із варіантами відповідей - групуємо

RadioGroupBox = QGroupBox("Варіанти відповідей:") #рамка для блоку кнопок
RadioGroup = QButtonGroup()                       #всі кнопки в один віджет

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_answer1 = QHBoxLayout() #Розміщення варіантів відповідей по макетах(Leyout)
layout_answer2 = QVBoxLayout() #Вертикальні в середині горизонтального
layout_answer3 = QVBoxLayout()

layout_answer2.addWidget(rbtn_1) #перші 2 вілповіді на 1 шу вертик.лінію
layout_answer2.addWidget(rbtn_2)
layout_answer3.addWidget(rbtn_3)
layout_answer3.addWidget(rbtn_4)

layout_answer1.addLayout(layout_answer2) #Привязуємо всі перемикачі до однієї горизонтальної лінії
layout_answer1.addLayout(layout_answer3)
RadioGroupBox.setLayout(layout_answer1) #Додаємо до рамки (лінії з віджетами)

#Створюємо панель(рамку) із рамками тесту:

AnswerGroupBox = QGroupBox("Результат тесту:")
lb_Resoult = QLabel('') #Надпис - перекладу - результату
lb_Correct = QLabel('') #Чи вірно чи ні

#Розміщуємо їх на рамці

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Resoult, alignment=(Qt.Alignment | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, strech=2)
AnswerGroupBox.setLayout(layout_res)
AnswerGroupBox.hide()

#Розміщуємо всіх віджети у вікні

layout_lin1 = QHBoxLayout()
layout_lin2 = QHBoxLayout()
layout_lin3 = QHBoxLayout()
layout_lin4 = QHBoxLayout()

#Розміщуємо на 1 шій лінії(кнопки меню, сну, і надпис)
layout_lin1.addWidget(btn_Menu)
layout_lin1.addStretch(1)
layout_lin1.addWidget(btn_Sleep)
layout_lin1.addWidget(box_Minutes)
layout_lin1.addWidget(QLabel("хвилин"))

layout_lin2.addWidget(lb_Question,alignment=(Qt.AlignCenter | Qt.AlignVCenter))

layout_lin3.addWidget(RadioGroupBox)
layout_lin3.addWidget(AnswerGroupBox)

layout_lin4.addStretch(1)
layout_lin4.addWidget(btn_Ok,stretch=2)
layout_lin4.addStretch(1)

# 4 горизонтальні на 1 вертикальну
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_lin1, stretch=1)
layout_cards.addLayout(layout_lin2, stretch=2)
layout_cards.addLayout(layout_lin3, stretch=8)

layout_cards.addStretch(1)
layout_cards.addLayout(layout_lin4, stretch=1)
layout_cards.addStretch(1)
layout_cards.setSpacing(5)

main_wind.setLayout(layout_cards)
main_wind.show()

app.exec_()