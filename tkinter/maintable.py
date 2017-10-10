from imagebtn import *
from tkinter import *

from random import *
import time

from tkinter import *

class Maintable(Frame):
    n=0
    selected_image=0
    
    def __init__(self, master, picture, alphabet, width):
        super(Maintable, self).__init__()
        self.image_number_list = []  # 셔플된 이미지의 번호를 저장하기 위한 리스트. 16개 : 셔플할 때 쓰는거
        self.master = master # maintable frame의 parent 설정
        self.width = width # maintable의 넓이. = 4
        self.n = width * width # maintable에 추가될 이미지 수. = 16
        self.picture = picture # app.py에서 생성한 이미지 받아와서 저장
        self.alphabet = alphabet

        # 숨겨진 이미지 셔플링 : 알파벳과 도형을 랜덤하게 매칭
        self.random_shuffle()

        # TODO
        # ImageButton widget 생성하고 각 widget에 숨겨진 이미지 추가
        # 아래에서처럼 A에 덮어쓰는형식으로 for문을 돌려도 grid때문에 다른 좌표에 있는 것이기 때문에 문제 없음.
        # count는 0~15까지의 리스트의 인덱스를 가져오기위해서 설정해줌.
        count = 0
        for i in range(0,self.width):
            for j in range(0,self.width):
                A = ImageButton(self, image=alphabet[count]) # 그림숨기고 게임에서 알파벳이 보이는 부분
                # A = ImageButton(self, image=self.picture[self.image_number_list[count]])
                # 게임 test하기 위해선 바로 윗줄 코드를 활성화 시켜주면된다

                # imagebtn.py의 add_hidden을 통해서 이미지를 버튼에 삽입한다.
                A.add_hidden(alphabet[count], self.picture[self.image_number_list[count]]) # 눌렀을때 그림이미지 보여줌
                # A.add_hidden(self.picture[self.image_number_list[count]], self.picture[self.image_number_list[count]])
                # Test하기 위해선 위에줄 처럼 해주면 된다.
                A.grid(row=i, column=j)
                A.bind('<Button-1>', self.show_hidden)
                A.bind('<ButtonRelease-1>', self.hide_picture)
                count += 1

    # TODO
    # hidden 이미지 셔플링
    def random_shuffle(self):
        self.image_number_list = list(sample(range(0, 16), 16))

    # 선택된 알파벳 ImageButton의 숨겨진 이미지 출력
    def show_hidden(self, event):
        event.widget.config(image=event.widget.get_hidden())
        self.update()

    # TODO
    # 숨겨진 이미지 숨기고 알파벳 이미지로 변환
    # 선택된 이미지와 컨베이어의 현재 이미지와 비교하고, 비교 결과에 따른 명령어 실행 부분
    def hide_picture(self, event):
        event.widget.config(image=event.widget.alphabet)
        selected_image = self.picture.index(event.widget.hidden) # index가 뽑힘
        # conv_image = self.master.conveyor.picture.index(event.widget.hidden)
        # selected_image 와 master.conveyor.cur_image(컨베이어가 가리키는 image가 일치하는지 여부 판단
        # 일치하면 conveyor의 correct_match()실행 / 불일치하면 wrong_match()실행
        if selected_image == self.master.conveyor.cur_image:
            self.master.conveyor.correct_match()
        else:
            self.master.conveyor.wrong_match()
        #time.sleep(10)
        #time.sleep(1.5)

        #if selected_image == cur_img
        #correct랑 wrong을 여기서 불러야함.
