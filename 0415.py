import time
class Smartphone: 
    def __init__(self,model,battery,max_battery, power_on):
        self.model = model
        self.battery = battery
        self.max_battery = max_battery
        self.power_on = power_on

    def use_battery(self,amount):
        if self.battery <= 0 :
            print("전원이 꺼졌습니다")
        elif self.battery < amount :
            print("잔여배터리가 부족합니다")
        else:
            self.max_battery -= amount
            print(f"배터리 사용: {amount}")
    def charge(self, charger):
        if self.power_on == 0:
            print ("전원이 켜졌습니다")
            self.power_on = 1
        amount = min(self.battery, charger.get_needed_battery(self))

        self.battery += amount
        charger.amount -= amount
        if self.battery > 100:
            self.battery = 100

        print(f"충전됨: {charger.amount} 현재: {self.battery}")
    
    def status(self):
        print(f"모델: {self.model} / 베터리: {self.battery}")

    def get_need_battery(self):
        return self.max_battery - self.battery

class Charger:
    def __init__(self,name,amount,max_battery):
        self.name = name
        self.amount = amount
        self.max_battery = max_battery

    def get_needed_battery(self, a):
        return  a.max_battery - a.battery
    def charge_charger(self):
        while(1):
            if self.amount < self.max_battery:
                self.amount += 10
                time.sleep(1)
                print(f"charing, current: {self.amount}")
            else:
                break
        




    

a = Smartphone("idk", 60, 100, True)
b = Charger("Charger 1", 9500,10000)

a.charge(b)
b.get_needed_battery(a)
b.charge_charger()
    

        