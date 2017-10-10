from tkinter import *
from random import *
from time import *

class Conveyor(Frame):
    def __init__(self, master, picture, width):
        super(Conveyor, self).__init__()
        self.image_number_list = [] # 셔플된 이미지의 번호를 저장하기 위한 리스트. 13개
        self.labels = [] # 컨베이어 frame에 추가되는 이미지 label 위젯의 리스트
        self.master = master # 컨베이어 frame의 parent 설정 : mater를 설정해줘서 maintable Conveyor를 자유롭게 왔다갔다 할 수있음
        self.width = width # 메인 테이블의 가로 길이. = 4
        self.n = width*(width-1)+1 # 컨베이어에 넣을 이미지의 수. = 13
        self.picture = picture # app에서 생성한 이미지 받아와서 저장
        # 이미지가 컨베이어에 올라갔는지 아닌지 체크하기 위한 리스트. 초기 세팅은 모두 FALSE. : 나는 이거 사용 안했음!!
        self.image_flags = list(False for i in range(self.width*self.width)) # 어떤이미지들이 선택됐는지 그 정보 담고있음.

        # 현재 위치 표시를 위한 캔버스 위젯 생성 : 역삼각형 그릴라고 만든것임 / 배경이 하얀부분이 캔버스.
        self.conveyor_canvas = Canvas(self, width = 700, height=30, background = 'white')
        # 현재 맞춰야할 그림을 나타내는 역삼각형 생성(polygon)
        self.x0 = 499
        self.x1 = 529
        self.x2 = 514
        self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')
        
        # final text와 졌을때 졌다고 표시해주는 text 생성
        self.final = self.conveyor_canvas.create_text(653,26, text="FINAL", anchor=SW, fill = 'red', font="Times 13 bold italic")
        self.lose = self.conveyor_canvas.create_text(0, 26, text=" ", anchor=SW, fill='red', font="Times 13 bold italic")

        # 컨베이어에 올릴 이미지 셔플링 : 16개중에 13개 뽑는거
        self.random_shuffle()

        # TODO
        # 셔플 결과대로 이미지 label 생성하여 리스트에 저장 : 그림
        for i in range(0, self.n):
            label = Label(self, image=self.picture[self.image_number_list[i]])
            self.labels.append(label)
            label.grid(row=1, column=i)

        # cur_idx와 cur_image를 함께 가야함(생각해야함.)
        # 현재 index 설정 = 시작 위치 설정
        self.cur_idx = int(self.n/self.width*(self.width-1))
        print('self.cur_idx', self.cur_idx)
        # 역삼각형의 초기위치(숫자로 줘도된다) : polygon 만들때 줬음.

        # 현재 이미지 설정 = 시작 이미지 설정 : 선택한 이미지와 비교 목적으로 저장
        # picture list 내에서 몇번째에 위치하고있는지.
        self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
        print('cur_image', self.cur_image)

        # TODO
        # 캔버스 세팅 : 캔버스를 배치 시키는거
        self.conveyor_canvas.grid(row=0, column=0, columnspan = 13)

    # TODO
    # 이미지 셔플 함수
    def random_shuffle(self):
        # 0~15 숫자 중 임의로 중복되지 않는 13개의 숫자 선택 : 선택된건 True로 변환?
        # sample함수? 거기서 중복되지않는 임의의 숫자 뽑아줌.
        self.image_number_list = list(sample(range(0, 16), 13))


   # TODO
   # 선택한 그림이 현재 위치의 그림과 일치하는 경우
    def correct_match(self):
        print('correct','/cur_idx',self.cur_idx, '/cur_image' ,self.cur_image)
        # 마지막 이미지를 찾은 경우
        if self.cur_idx == self.n-1:
            #종료
            self.master.quit_game(True)
            # 현재 이미지 및 현재 위치 재설정
            self.cur_idx += 1
            self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
            print('correct_find_last', self.cur_idx,'/cur_image' ,self.cur_image)
            # 캔버스 위젯
            # 현재 위치 표시 도형 우측 이동
            self.x0 += 54
            self.x1 += 54
            self.x2 += 54
            self.polygon = self.conveyor_canvas.delete(self.polygon)
            self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')

            # ※canvas.itemconfig(도형의객체, outline='white', fill='white', + 추가적인 parameter 세팅) 기존에 생성된 도형 객체의 변경 가능
        else:
            # 현재 위치가 컨베이어의 가장 우측 도형을 지목할 때 : self.n-2에서 맞춰야 넘어감.
            # FINAL 글씨를 가리지 않도록 도형 수정
            if self.cur_idx == self.n-2:
                # 현재 이미지 및 현재 위치 재설정
                self.cur_idx += 1
                self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
                print('correct_to_last_image', self.cur_idx, '/cur_image' ,self.cur_image)
                self.final = self.conveyor_canvas.delete(self.final)
                self.x0 += 54
                self.x1 += 54
                self.x2 += 54
                self.polygon = self.conveyor_canvas.delete(self.polygon)
                self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')

            # 그 외 도형 이동
            else:
                # 현재 이미지 및 현재 위치 수정
                self.cur_idx += 1
                self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
                print('correct_normal_case', self.cur_idx, '/cur_image' ,self.cur_image)

                self.x0 += 54
                self.x1 += 54
                self.x2 += 54
                self.polygon = self.conveyor_canvas.delete(self.polygon)
                self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')


   # TODO
   # 선택한 그림이 현재 위치의 그림과 일치하지 않는 경우
    def wrong_match(self):
        print('wrong', '/cur_idx', self.cur_idx, '/cur_image' ,self.cur_image)
        # 마지막 기회에서 틀린 경우 - > 게임을 졌다는 표시를 해줘야함
        if(self.cur_idx == 0):
            self.cur_idx -= 1
            print('wrong_last_chance', '/cur_idx', self.cur_idx, '/cur_image', self.cur_image)
            self.polygon = self.conveyor_canvas.delete(self.polygon)
            # You Lose!! 표시
            self.lose = self.conveyor_canvas.create_text(0, 26, text="YOU LOSE!!", anchor=SW, fill='red', font="Times 13 bold italic")
            #종료
            self.master.quit_game(False)

            self.x0 -= 54
            self.x1 -= 54
            self.x2 -= 54
            self.polygon = self.conveyor_canvas.delete(self.polygon)
            self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')
                # 종료 :  self.master.App.quit_game()
        # 캔버스 위젯
        # 가장 왼쪽의 이미지를 제거
        # 기존 이미지들 좌측으로 한 칸씩 이동
        # 컨베이어에 추가되지 않은 이미지 중 하나 선택하여 가장 우측에 추가
        # 현재 위치 재설정
        # canvas.itemconfig(도형의객체, outline='white', fill='white', + 추가적인 parameter 세팅) 기존에 생성된 도형 객체의 변경 가능
        else: # 게임 지지않았으면 왼쪽으로 이동하는거
            # FINAL에서 오답 선택했을 때 도형 복구
           if self.cur_idx == self.n-1:
               self.cur_idx -= 1
               print('wrong_recove_final', '/cur_idx', self.cur_idx, '/cur_image', self.cur_image)

               self.x0 -= 54
               self.x1 -= 54
               self.x2 -= 54
               self.polygon = self.conveyor_canvas.delete(self.polygon)
               self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')
               self.final = self.conveyor_canvas.create_text(653, 26, text="FINAL", anchor=SW, fill='red',
                                                             font="Times 13 bold italic")
           else:
               self.cur_idx -= 1
               print('wrong_recove_final', '/cur_idx', self.cur_idx, '/cur_image', self.cur_image)

               self.x0 -= 54
               self.x1 -= 54
               self.x2 -= 54
               self.polygon = self.conveyor_canvas.delete(self.polygon)
               self.polygon = self.conveyor_canvas.create_polygon(self.x0, 10, self.x1, 10, self.x2, 25, fill='blue')

           # 도형 이동
           # 새 이미지 추가 :
           while True:
               new_image = randint(0, self.width*self.width-1)
               if new_image not in self.image_number_list :
                   break
           # 기존 이미지 좌측으로 한 칸씩 이동
           # label.config(parameter = configuration) 기존의 label 위젯 변경 가능
           for i in range(0,self.n-1):
               self.labels[i].config(image=self.picture[self.image_number_list [i+1]])
               self.image_number_list [i] = self.image_number_list [i+1]
           # 새 이미지 추가
           self.image_number_list[self.n-1] = new_image
           self.labels[self.n-1].config(image=self.picture[self.image_number_list [self.n-1]])