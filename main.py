#첫번째니까...
#메뉴리스트
menu = {"아이스아메리카노": 4500,
        "아메리카노": 4000,
        "아이스바닐라라떼": 5500,
        "바닐라라떼": 5000}

order_list = []


#주문
while True:
    try:
        print("=" * 20)
        print("지현이네 카페 - MENU")
        print(menu)
        print("=" * 20)
        
        user_order_input = input("음료명을 입력하세요.: ")
        
        # 'q'를 입력하면 while break
        if user_order_input == 'q': 
            break

        # 잘못된 음료명을 넣으면 ValueError 예외가 발생합니다.
        if user_order_input not in menu:
            raise ValueError("잘못된 음료명입니다. 다시입력해주세요. q를 입력하면 주문종료됩니다.")

        # 주문한 음료와 해당 음료의 가격을 주문 리스트에 추가합니다.
        order_list.append((user_order_input, menu[user_order_input]))
        print("주문이 완료되었습니다. 현재 주문 리스트:", order_list)
        
    except ValueError as ve:
        # ValueError 예외가 발생한 경우 오류 메시지를 출력하고 다시 주문을 받습니다.
        print(ve)
        continue

# 주문이 완료되면 주문 리스트에 있는 모든 음료와 총 주문 금액을 보여줍니다.
print("=" * 20)
print("주문이 완료되었습니다. 주문 내역을 확인해주세요.")
total_price = sum(menu[item[0]] for item in order_list)  # 주문 리스트에 있는 음료의 가격을 더합니다.
for item in order_list:
    print("음료명:", item[0], "| 가격:", menu[item[0]])
print("총 주문 금액:", total_price, "원")
print("=" * 20)

#결제... 시간없어서 못했습니다 ㅠㅠ 현금결제라고 가정해주세요...


print("주문 감사합니다! :) ")