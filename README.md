# CAFE-KIOSK App : mini project

[![Python Version](https://img.shields.io/badge/Python-3.10.13-blue)](https://www.python.org/downloads/release/python-31013/) [![Django Version](https://img.shields.io/badge/Django-3.2.9-green)](https://www.djangoproject.com/)

## 요구사항

![이미지 설명](https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihbVfuuX8pKBz0O0FbMXcAfw5TgkvZ4lSM-9zZZVimJ-Y-5Y8EJ7wyP7K_N1JfHqOt1NgI4Hs_Et0ZR6uwDYxVn-adb44Vzr9a0=w1327-h876)

## 기능

### 1. kiosk

- 메뉴 조회 및 주문: 사용자는 카페의 메뉴를 조회하고 주문할 수 있습니다.
- 주문 처리: 주문은 포스기에서 실시간으로 처리됩니다.
- 결제: 주문은 현금 또는 신용카드로 결제할 수 있습니다.
- 주문 상태 업데이트: 사용자는 주문 상태를 실시간으로 확인할 수 있습니다.

### 2. admin

- superuser create
- menu CURD

## Question Model


| SR No | Category  | Drinks                                                        |
| ------- | ----------- | --------------------------------------------------------------- |
| 1     | 핫 음료   | 아메리카노, 라떼, 모카, 화이트 초콜릿 모카, 카푸치노          |
| 2     | 콜드 음료 | 아이스 아메리카노, 아이스 라떼, 아이스 티, 프라푸치노, 스무디 |
| 3     | 티        | 그린 티, 얼 그레이, 차이 티 라떼, 히비스커스 티               |

## Choice Model

1. 핫 음료


   | 음료       | 세부 음료 종류                              |
   | ------------ | --------------------------------------------- |
   | 아메리카노 | 블론드, 에스프레소, 데카프리노              |
   | 라떼       | 바닐라 라떼, 헤이즐넛 라떼, 카라멜 마키아또 |
   | 모카       | 카라멜 모카, 화이트 초콜릿 모카             |
   | ...        | ...                                         |
2. 콜드 음료


   | 음료              | 세부 음료 종류                              |
   | ------------------- | --------------------------------------------- |
   | 아이스 아메리카노 | 블론드, 에스프레소, 데카프리노              |
   | 아이스 라떼       | 바닐라 라떼, 헤이즐넛 라떼, 카라멜 마키아또 |
   | ...               | ...                                         |
3. 티


   | 음료      | 세부 음료 종류                        |
   | ----------- | --------------------------------------- |
   | 그린 티   | 레몬 그린 티, 자몽 그린 티, ...       |
   | 얼 그레이 | 블랙 얼 그레이, 라벤더 얼 그레이, ... |
   | ...       | ...                                   |

## 개발 환경 설정

```shell
pip install django
pip install psycopg2-binary
```

## 업데이트 내역

* 0.0.1
  * docs
  * feat: table create
    * admin : user list
    * menu : list, price

* 0.0.2
  * feat: table create
    * admin
    * menu
    * order
    * payment