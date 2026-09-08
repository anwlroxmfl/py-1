import pygame
import math 
import random
import sys

# 1. 초기화 및 화면 설정
pygame.init()
WIDTH, HEIGHT = 1400, 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("더 브레이커: 오류 수정 & 스킬 업데이트")
clock = pygame.time.Clock()

# [오류 방지] 폰트 설정: 나눔고딕이나 맑은고딕이 없으면 기본 폰트 사용
def get_font(size, bold=False):
    try:
        return pygame.font.SysFont("malgungothic", size, bold)
    except:
        return pygame.font.SysFont("arial", size, bold)

font_L = get_font(35, True)
font_M = get_font(18, True)
font_S = get_font(12)

# 색상 정의
WHITE, BLACK, RED, GREEN, YELLOW, GOLD, PURPLE, CYAN, BLUE, ORANGE, GRAY = \
    (255, 255, 255), (10, 10, 15), (231, 76, 60), (46, 204, 113), (241, 196, 15), (255, 215, 0), \
    (155, 89, 182), (52, 152, 219), (41, 128, 185), (230, 126, 34), (100, 100, 100)
DEEP_RED = (150, 0, 0)

# 2. 데이터 생성 (로봇 & 무기 50종)
TIER_NAMES = ["일반", "희귀", "영웅", "전설", "신화", "초월"]
robot_themes = ["드론", "봇", "머신", "가디언", "센티넬", "타이탄"]

robot_data = []
weapon_data = []

for i in range(50):
    t_idx = min(int((i / 50) * 6), 5)
    t_color = [GRAY, GREEN, BLUE, PURPLE, GOLD, RED][t_idx]
    
    # 로봇 데이터
    robot_data.append({
        "name": f"{TIER_NAMES[t_idx]} {robot_themes[t_idx]} #{i%8 + 1}",
        "base": int(20 * (1.4 ** i)),
        "color": t_color
    })
    # 무기 데이터
    weapon_data.append({
        "name": f"[{TIER_NAMES[t_idx]}] 무기 #{i+1}",
        "mult": round(2.5 * (1.32 ** i), 1),
        "color": t_color
    })

my_robots = [{"level": 0, "exp": 0} for _ in range(50)]
owned_weapons = [False] * 50
owned_weapons[0] = True
equipped_idx = 0

# 3. 게임 시스템 변수
money = 15000
target_lvl = 1
max_hp = 100
current_hp = max_hp
click_cnt, fever = 0, 0
r_price, w_price = 100, 500
is_boss = False
boss_timer = 1800
boss_pattern_timer = 0
boss_msg = ""

# 스킬 시스템
skills = {
    "1": {"name": "하이퍼 클릭", "cool": 0, "max_cool": 600, "dur": 180, "active": 0, "desc": "3배 데미지"},
    "2": {"name": "골드 수확", "cool": 0, "max_cool": 1200, "dur": 0, "active": 0, "desc": "즉시 골드"},
    "3": {"name": "시간 왜곡", "cool": 0, "max_cool": 1800, "dur": 300, "active": 0, "desc": "시간 정지"}
}

upgrades = {
    "click": {"lvl": 1, "cost": 100, "name": "공격력 강화", "inc": 20},
    "gold": {"lvl": 1, "cost": 500, "name": "골드 보너스", "inc": 0.5},
    "auto_speed": {"lvl": 1, "cost": 2000, "name": "자동 속도", "inc": 50},
    "boss_dmg": {"lvl": 1, "cost": 2500, "name": "보스 특공", "inc": 0.3},
    "reset": {"lvl": 0, "cost": 10000, "name": "가격 초기화", "inc": 0}
}
stats = {"crit_rate": 15, "crit_mult": 5.0, "g_mult": 1.0, "a_speed": 1000}
particles, logs = [], []
target_pos = (250, 450)

# 4. 핵심 로직 함수
def add_log(msg, color=WHITE):
    logs.append({"text": msg, "color": color, "timer": 150})
    if len(logs) > 6: logs.pop(0)

def spawn_p(color, count=8):
    for _ in range(count):
        particles.append([[target_pos[0], target_pos[1]], [random.uniform(-6, 6), random.uniform(-6, 6)], random.randint(4, 10), color])

def boss_fail_penalty():
    global money, owned_weapons, current_hp, boss_timer
    lost = int(money * 0.3)
    money -= lost
    add_log(f"보스전 패배! {lost:,}G 상실!", RED)
    
    destroyed = 0
    for i in range(1, 50):
        if owned_weapons[i] and i != equipped_idx:
            if random.random() < 0.2:
                owned_weapons[i] = False
                destroyed += 1
    if destroyed > 0: add_log(f"무기 {destroyed}개 파괴됨!", PURPLE)
    current_hp, boss_timer = max_hp, 1800

def apply_dmg(is_auto):
    global money, current_hp, max_hp, target_lvl, click_cnt, fever, is_boss, boss_timer, boss_msg
    if is_auto:
        dmg = sum([my_robots[i]["level"] * robot_data[i]["base"] for i in range(50)])
    else:
        dmg = int(upgrades["click"]["lvl"] * upgrades["click"]["inc"] * weapon_data[equipped_idx]["mult"])
        if skills["1"]["active"] > 0: dmg *= 3
        if random.randint(1, 100) <= stats["crit_rate"]: 
            dmg = int(dmg * stats["crit_mult"])
            spawn_p(PURPLE, 15)
        if fever <= 0:
            click_cnt += 1
            if click_cnt >= 50: fever = 400; click_cnt = 0; add_log("FEVER TIME!", RED)

    if fever > 0: dmg *= 5
    if is_boss:
        dmg *= (1 + upgrades["boss_dmg"]["lvl"] * upgrades["boss_dmg"]["inc"])
        if 120 < (boss_pattern_timer % 300) < 240:
            dmg = int(dmg * 0.2)
            boss_msg = "SHIELD!"
        else: boss_msg = "BOSS BATTLE"

    if dmg <= 0 and is_auto: return
    current_hp -= dmg
    spawn_p(RED if is_boss else BLUE)

    if current_hp <= 0:
        money += int(target_lvl * 50 * stats["g_mult"]) * (10 if is_boss else 1)
        target_lvl += 1
        is_boss = (target_lvl % 5 == 0)
        max_hp = math.floor(100 * ((2.8 if is_boss else 1.4) ** (target_lvl-1)))
        current_hp, boss_timer = max_hp, 1800

# 5. 메인 게임 루프
AUTO_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(AUTO_EVENT, stats["a_speed"])

run = True
while run:
    screen.fill(BLACK)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        
        # 키보드 스킬 (1, 2, 3)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1 and skills["1"]["cool"] <= 0:
                skills["1"]["active"], skills["1"]["cool"] = 180, 600
                add_log("하이퍼 클릭!", CYAN)
            if e.key == pygame.K_2 and skills["2"]["cool"] <= 0:
                bonus = int(target_lvl * 500 * stats["g_mult"])
                money += bonus
                skills["2"]["cool"] = 1200
                add_log(f"골드 수확 (+{bonus:,})", GOLD)
            if e.key == pygame.K_3 and skills["3"]["cool"] <= 0:
                skills["3"]["active"], skills["3"]["cool"] = 300, 1800
                add_log("시간 왜곡!", BLUE)

        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = e.pos
            # 적 클릭
            if pygame.Rect(target_pos[0]-110, target_pos[1]-110, 220, 220).collidepoint(e.pos):
                apply_dmg(False)
            
            # 가챠 버튼
            if pygame.Rect(530, 750, 220, 80).collidepoint(e.pos) and money >= r_price:
                money -= r_price; r_price = int(r_price * 1.05)
                idx = random.choices(range(50), weights=[max(1, 100-i*2) for i in range(50)])[0]
                my_robots[idx]["exp"] += 1
                if my_robots[idx]["exp"] >= max(1, my_robots[idx]["level"]):
                    my_robots[idx]["level"] += 1; my_robots[idx]["exp"] = 0
            if pygame.Rect(770, 750, 220, 80).collidepoint(e.pos) and money >= w_price:
                money -= w_price; w_price = int(w_price * 1.08)
                idx = random.choices(range(50), weights=[max(1, 100-i*2) for i in range(50)])[0]
                if not owned_weapons[idx]: owned_weapons[idx] = True; add_log(f"무기 발견: {weapon_data[idx]['name']}", CYAN)
            
            # 업그레이드 버튼
            for i, (k, v) in enumerate(upgrades.items()):
                if pygame.Rect(530, 100 + i*75, 230, 65).collidepoint(e.pos) and money >= v["cost"]:
                    money -= v["cost"]
                    if k == "reset": r_price, w_price = 100, 500
                    else:
                        v["lvl"] += 1
                        if k == "gold": stats["g_mult"] += v["inc"]
                        if k == "auto_speed": 
                            stats["a_speed"] = max(100, stats["a_speed"]-v["inc"])
                            pygame.time.set_timer(AUTO_EVENT, stats["a_speed"])
                    v["cost"] = int(v["cost"] * 2.5)

            # 무기 선택
            for i in range(50):
                if owned_weapons[i]:
                    r, c = i // 2, i % 2
                    if pygame.Rect(1020 + c*180, 100 + r*32, 170, 28).collidepoint(e.pos):
                        equipped_idx = i

        if e.type == AUTO_EVENT:
            apply_dmg(True)

    # 쿨타임/지속시간/보스 로직
    for s in skills.values():
        if s["cool"] > 0: s["cool"] -= 1
        if s["active"] > 0: s["active"] -= 1
    if is_boss:
        if skills["3"]["active"] <= 0: boss_timer -= 1
        boss_pattern_timer += 1
        if boss_pattern_timer % 60 == 0: current_hp = min(max_hp, current_hp + (max_hp * 0.015))
        if boss_timer <= 0: boss_fail_penalty()

    # --- UI 렌더링 ---
    pygame.draw.line(screen, GRAY, (510, 0), (510, HEIGHT), 2)
    pygame.draw.line(screen, GRAY, (1010, 0), (1010, HEIGHT), 2)

    # 1. 전투 구역
    screen.blit(font_L.render(f"GOLD: {money:,}", True, GOLD), (40, 40))
    # 무기 정보창
    pygame.draw.rect(screen, (20, 20, 30), (40, 90, 430, 80), 0, 10)
    pygame.draw.rect(screen, weapon_data[equipped_idx]["color"], (40, 90, 430, 80), 2, 10)
    screen.blit(font_M.render(f"E: {weapon_data[equipped_idx]['name']}", True, weapon_data[equipped_idx]["color"]), (55, 100))
    screen.blit(font_S.render(f"Damage x{weapon_data[equipped_idx]['mult']} | Crit {stats['crit_rate']}%", True, WHITE), (55, 135))

    # 적/레벨
    lvl_txt = f"{'BOSS' if is_boss else 'STAGE'} {target_lvl}"
    screen.blit(font_L.render(lvl_txt, True, RED if is_boss else WHITE), (target_pos[0]-80, target_pos[1]-165))
    t_c = DEEP_RED if is_boss else (100, 100, 120)
    if is_boss and 120 < (boss_pattern_timer % 300) < 240: t_c = CYAN
    pygame.draw.rect(screen, t_c, (target_pos[0]-110, target_pos[1]-110, 220, 220), 0, 15)
    
    # HP 바
    pygame.draw.rect(screen, (30, 30, 40), (60, 600, 380, 30), 0, 10)
    pygame.draw.rect(screen, GREEN, (60, 600, (max(0, current_hp)/max_hp)*380, 30), 0, 10)
    screen.blit(font_M.render(f"{int(current_hp):,} / {int(max_hp):,}", True, WHITE), (150, 603))
    
    # 보스 타이머
    if is_boss:
        pygame.draw.rect(screen, RED, (60, 185, (boss_timer/1800)*380, 10))

    # 스킬 UI
    for i, (k, v) in enumerate(skills.items()):
        s_c = GREEN if v["cool"] <= 0 else GRAY
        if v["active"] > 0: s_c = YELLOW
        pygame.draw.rect(screen, s_c, (40 + i*150, 750, 140, 60), 2, 5)
        screen.blit(font_S.render(f"[{k}] {v['name']}", True, s_c), (45 + i*150, 755))
        if v["cool"] > 0:
            pygame.draw.rect(screen, RED, (45 + i*150, 800, (v["cool"]/v["max_cool"])*130, 5))

    # 2. 중앙 및 도감
    for i, (k, v) in enumerate(upgrades.items()):
        rect = pygame.Rect(530, 100 + i*75, 230, 65)
        pygame.draw.rect(screen, BLUE if money >= v["cost"] else GRAY, rect, 0, 10)
        screen.blit(font_M.render(v["name"], True, WHITE), (540, 105 + i*75))
        screen.blit(font_S.render(f"Cost: {v['cost']:,}", True, YELLOW), (540, 135 + i*75))

    for i in range(50):
        r, c = i % 25, i // 25
        lvl = my_robots[i]["level"]
        color = robot_data[i]["color"] if lvl > 0 else (60, 60, 60)
        screen.blit(font_S.render(f"{robot_data[i]['name'] if lvl > 0 else '???'} (Lv.{lvl})", True, color), (780 + c*110, 130 + r*22))

    # 가챠 버튼
    pygame.draw.rect(screen, ORANGE, (530, 750, 220, 80), 0, 15)
    screen.blit(font_M.render(f"ROBOT ({r_price:,})", True, WHITE), (550, 775))
    pygame.draw.rect(screen, RED, (770, 750, 220, 80), 0, 15)
    screen.blit(font_M.render(f"WEAPON ({w_price:,})", True, WHITE), (790, 775))

    # 3. 무기 가방
    for i in range(50):
        r, c = i // 2, i % 2
        color = CYAN if equipped_idx == i else (weapon_data[i]["color"] if owned_weapons[i] else GRAY)
        pygame.draw.rect(screen, color, (1020 + c*180, 100 + r*32, 170, 28), 1, 5)
        screen.blit(font_S.render(weapon_data[i]["name"] if owned_weapons[i] else "???", True, color), (1030 + c*180, 105 + r*32))

    # 파티클/피버/로그
    if fever > 0: fever -= 1
    for p in particles[:]:
        p[0][0]+=p[1][0]; p[0][1]+=p[1][1]; p[2]-=0.4
        if p[2] <= 0: particles.remove(p)
    for l in logs: l["timer"] -= 1
    for p in particles: pygame.draw.circle(screen, p[3], (int(p[0][0]), int(p[0][1])), int(p[2]))
    for i, log in enumerate(logs):
        s = font_M.render(log["text"], True, log["color"]); s.set_alpha(log["timer"]*2)
        screen.blit(s, (530, 500 + i*25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()