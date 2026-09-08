import random 
import time

# 1. 데코레이터: 연습 시간 측정
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "═" * 60)
        print("🚀 파이썬 코드 & 문장 타이핑 연습을 시작합니다!")
        print("👉 종료하려면 'quit'을 입력하세요.")
        print("═" * 60)
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("\n" + "═" * 60)
        print(f"⏱️ 총 연습 시간: {end_time - start_time:.1f}초")
        print("═" * 60)
        return result
    return wrapper

# 2. 제너레이터: 단어와 문장을 섞어서 배출
def practice_generator():
    # 파이썬 핵심 문장들 (f-string, List Comprehension 등 포함)
    sentences = [
        "print(f'Hello, {name}!')",
        "result = [i for i in range(10) if i % 2 == 0]",
        "def my_function(*args, **kwargs):",
        "for index, value in enumerate(my_list):",
        "with open('file.txt', 'r') as f:",
        "async def fetch_data(): await asyncio.sleep(1)",
        "if __name__ == '__main__': main()",
        "class MyClass(BaseClass): pass",
        "try: do_something() except Exception as e: print(e)",
        "items = sorted(data, key=lambda x: x['price'])"
    ]
    
    # 단어들 (기존 리스트 유지)
    words = ["decorator", "generator", "asyncio", "f-string", "variable", "immutable"]

    while True:
        # 30% 확률로 문장, 70% 확률로 단어 출현
        if random.random() < 0.3:
            yield random.choice(sentences)
        else:
            yield random.choice(words)

# 3. 메인 연습 로직
@timer_decorator
def start_typing_practice():
    gen = practice_generator()
    count = 0
    
    for target in gen:
        count += 1
        print(f"\n[{count}] {target}")
        user_input = input("입력 👉 ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if user_input == target:
            print("✅ Perfect!")
        else:
            print(f"❌ 오타 발생! (정답: {target})")

if __name__ == "__main__":
    start_typing_practice()