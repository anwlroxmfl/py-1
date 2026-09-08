class BurgerStore: 
    def __init__(self,name,menu):
        self.name = name
        self.menu = menu
    def show_menu(self):
        print(f"대표 매뉴는 {self.menu}입니다")
    def cook(self):
        print("버거를 만듭니다")

class KoreaStore(BurgerStore):
    def __init__(self,name):
        super().__init__(name,"불고기버거")
        self.name = name
        
        
    def cook(self):
        print("한국 스타일 불고기버거를 만듭니다")

class JapanStore(BurgerStore):
    def __init__(self,name):
        super().__init__(name,"데리야끼버거")
        self.name = name
        
        
    def cook(self):
        print("일본 스타일 데리야끼버거를 만듭니다")

class USAStore(BurgerStore):
    def __init__(self,name):
        super().__init__(name,"치즈버거")
        self.name = name
        
    def cook(self):
        print("미국 스타일 치즈버거를 만듭니다")

k = KoreaStore("맥도날드 한국")
j = JapanStore("마꾸도나르도 일본")
u = USAStore("맥도날드 미국")
k.show_menu()
k.cook()
j.show_menu()
j.cook()
u.show_menu()
u.cook()




