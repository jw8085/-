#!/usr/bin/env python3
"""
GoodNotes Sample Notes Generator
실제 내용이 채워진 노트 예제를 생성합니다.
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import Color, black, blue, red, green
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT_DIR = "samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = A4
LIGHT_GRAY = Color(0.8, 0.8, 0.8, alpha=0.3)
MEDIUM_GRAY = Color(0.6, 0.6, 0.6, alpha=0.4)


def create_study_notes_python():
    """파이썬 학습 노트 예제"""
    filename = f"{OUTPUT_DIR}/example_python_study_notes.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # 배경 줄
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    margin_top = 40*mm
    y = HEIGHT - margin_top
    while y > 20*mm:
        c.line(20*mm, y, WIDTH - 20*mm, y)
        y -= 7*mm

    # 내용 작성
    c.setStrokeColor(black)
    c.setFillColor(black)

    # 제목
    c.setFont("Helvetica-Bold", 20)
    c.drawString(20*mm, HEIGHT - 25*mm, "Python 기초 학습 노트")

    c.setFont("Helvetica", 10)
    c.setFillColor(Color(0.5, 0.5, 0.5))
    c.drawString(20*mm, HEIGHT - 32*mm, "2025-12-05 | 프로그래밍 기초")

    # 섹션 1
    y = HEIGHT - 45*mm
    c.setFillColor(blue)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20*mm, y, "1. 변수와 데이터 타입")

    y -= 10*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 11)

    content1 = [
        "• 변수: 데이터를 저장하는 공간",
        "  - 예: name = 'Python'",
        "  - 예: age = 25",
        "",
        "• 주요 데이터 타입:",
        "  - str (문자열): 'hello', \"world\"",
        "  - int (정수): 1, 2, 100",
        "  - float (실수): 3.14, 2.5",
        "  - bool (불린): True, False",
        "  - list (리스트): [1, 2, 3]",
    ]

    for line in content1:
        c.drawString(25*mm, y, line)
        y -= 6*mm

    # 섹션 2
    y -= 5*mm
    c.setFillColor(blue)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20*mm, y, "2. 조건문과 반복문")

    y -= 10*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 11)

    content2 = [
        "• if 문: 조건에 따라 코드 실행",
        "  if age >= 18:",
        "      print('성인입니다')",
        "",
        "• for 반복문: 정해진 횟수만큼 반복",
        "  for i in range(5):",
        "      print(i)  # 0, 1, 2, 3, 4",
        "",
        "• while 반복문: 조건이 참인 동안 반복",
        "  while count < 10:",
        "      count += 1",
    ]

    for line in content2:
        c.drawString(25*mm, y, line)
        y -= 6*mm

    # 중요 포인트 박스
    y -= 10*mm
    c.setStrokeColor(red)
    c.setFillColor(Color(1, 0.9, 0.9))
    c.setLineWidth(1.5)
    c.roundRect(20*mm, y - 20*mm, WIDTH - 40*mm, 25*mm, 3*mm, fill=1)

    c.setFillColor(red)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(25*mm, y - 5*mm, "💡 핵심 요약")

    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(25*mm, y - 11*mm, "• Python은 동적 타입 언어 - 변수 선언 시 타입 지정 불필요")
    c.drawString(25*mm, y - 17*mm, "• 들여쓰기로 코드 블록 구분 (매우 중요!)")

    # 다음 학습 계획
    y -= 35*mm
    c.setFillColor(green)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20*mm, y, "📚 다음 학습 주제")

    y -= 8*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(25*mm, y, "☐ 함수 정의와 사용")
    y -= 6*mm
    c.drawString(25*mm, y, "☐ 리스트 컴프리헨션")
    y -= 6*mm
    c.drawString(25*mm, y, "☐ 딕셔너리와 세트")

    c.save()
    print(f"✓ Created: {filename}")


def create_meeting_notes():
    """회의록 예제"""
    filename = f"{OUTPUT_DIR}/example_meeting_notes.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # 배경 줄
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    y = HEIGHT - 40*mm
    while y > 20*mm:
        c.line(20*mm, y, WIDTH - 20*mm, y)
        y -= 7*mm

    c.setStrokeColor(black)
    c.setFillColor(black)

    # 헤더
    c.setFont("Helvetica-Bold", 18)
    c.drawString(20*mm, HEIGHT - 25*mm, "프로젝트 기획 회의록")

    # 회의 정보 박스
    c.setStrokeColor(Color(0.3, 0.5, 0.8))
    c.setFillColor(Color(0.9, 0.95, 1))
    c.setLineWidth(1)
    c.roundRect(20*mm, HEIGHT - 50*mm, WIDTH - 40*mm, 20*mm, 2*mm, fill=1)

    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(25*mm, HEIGHT - 36*mm, "일시: 2025년 12월 5일 14:00")
    c.drawString(25*mm, HEIGHT - 42*mm, "장소: 회의실 A")
    c.drawString(25*mm, HEIGHT - 48*mm, "참석자: 김팀장, 이과장, 박대리, 최사원")

    # 안건
    y = HEIGHT - 60*mm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(Color(0.2, 0.4, 0.7))
    c.drawString(20*mm, y, "회의 안건")

    y -= 10*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 11)
    c.drawString(25*mm, y, "1. 새로운 모바일 앱 개발 프로젝트 논의")
    y -= 6*mm
    c.drawString(25*mm, y, "2. 개발 일정 및 마일스톤 설정")
    y -= 6*mm
    c.drawString(25*mm, y, "3. 팀 역할 분담")

    # 논의 내용
    y -= 15*mm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(Color(0.2, 0.4, 0.7))
    c.drawString(20*mm, y, "주요 논의 내용")

    y -= 10*mm
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(25*mm, y, "▪ 프로젝트 목표")

    y -= 7*mm
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y, "- iOS/Android 크로스 플랫폼 앱 개발")
    y -= 6*mm
    c.drawString(30*mm, y, "- React Native 프레임워크 사용 결정")
    y -= 6*mm
    c.drawString(30*mm, y, "- 출시 목표: 2026년 3월")

    y -= 10*mm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(25*mm, y, "▪ 개발 단계")

    y -= 7*mm
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y, "- 1단계 (12월): 기획 및 디자인")
    y -= 6*mm
    c.drawString(30*mm, y, "- 2단계 (1-2월): 개발 및 테스트")
    y -= 6*mm
    c.drawString(30*mm, y, "- 3단계 (3월): 베타 테스트 및 출시")

    y -= 10*mm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(25*mm, y, "▪ 역할 분담")

    y -= 7*mm
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y, "- 김팀장: 프로젝트 총괄, 일정 관리")
    y -= 6*mm
    c.drawString(30*mm, y, "- 이과장: 백엔드 개발, API 설계")
    y -= 6*mm
    c.drawString(30*mm, y, "- 박대리: 프론트엔드 개발")
    y -= 6*mm
    c.drawString(30*mm, y, "- 최사원: UI/UX 디자인, 테스트")

    # 액션 아이템
    y -= 15*mm
    c.setStrokeColor(Color(0.8, 0.4, 0))
    c.setFillColor(Color(1, 0.95, 0.85))
    c.setLineWidth(1.5)
    c.roundRect(20*mm, y - 30*mm, WIDTH - 40*mm, 35*mm, 3*mm, fill=1)

    c.setFillColor(Color(0.8, 0.4, 0))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(25*mm, y - 7*mm, "📋 액션 아이템")

    y -= 14*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y, "☐ [김팀장] 프로젝트 일정표 작성 (마감: 12/10)")
    y -= 6*mm
    c.drawString(30*mm, y, "☐ [이과장] 기술 스택 상세 검토 보고서 (마감: 12/12)")
    y -= 6*mm
    c.drawString(30*mm, y, "☐ [최사원] 경쟁사 앱 분석 자료 준비 (마감: 12/15)")
    y -= 6*mm
    c.drawString(30*mm, y, "☐ [전체] 다음 회의 일정: 12월 15일 14:00")

    # 푸터
    y = 25*mm
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(Color(0.5, 0.5, 0.5))
    c.drawString(20*mm, y, "작성자: 박대리 | 검토: 김팀장")

    c.save()
    print(f"✓ Created: {filename}")


def create_daily_journal():
    """일기 예제"""
    filename = f"{OUTPUT_DIR}/example_daily_journal.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # 배경 - 점 노트
    c.setStrokeColor(MEDIUM_GRAY)
    c.setFillColor(MEDIUM_GRAY)

    margin = 20*mm
    dot_spacing = 5*mm
    dot_size = 0.5

    x = margin
    while x < WIDTH - margin:
        y = margin
        while y < HEIGHT - margin:
            c.circle(x, y, dot_size, fill=1)
            y += dot_spacing
        x += dot_spacing

    # 내용
    c.setFillColor(black)

    # 날짜
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20*mm, HEIGHT - 25*mm, "2025년 12월 5일 목요일")

    c.setFont("Helvetica", 11)
    c.setFillColor(Color(0.5, 0.5, 0.5))
    c.drawString(20*mm, HEIGHT - 32*mm, "날씨: ☀️ 맑음 | 기분: 😊 좋음")

    # 본문
    y = HEIGHT - 45*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 11)

    journal_text = [
        "오늘은 정말 생산적인 하루였다. 아침 일찍 일어나서 조깅을 했는데,",
        "상쾌한 공기를 마시며 뛰니 하루를 시작하는 기분이 너무 좋았다.",
        "",
        "오전에는 Python 프로그래밍 공부를 했다. 드디어 리스트 컴프리헨션을",
        "완전히 이해하게 되어서 뿌듯했다. 코드가 점점 간결해지는 것을 보니",
        "실력이 늘고 있다는 느낌이 든다.",
        "",
        "점심은 동료들과 함께 새로 생긴 일식집에 갔다. 음식도 맛있었고",
        "팀원들과 여유롭게 이야기 나누는 시간이 좋았다. 일만 하다가",
        "이렇게 쉬는 시간을 가지는 것도 중요하다는 걸 느꼈다.",
        "",
        "오후에는 프로젝트 회의가 있었다. 새로운 모바일 앱 개발 프로젝트가",
        "시작되는데, 내가 프론트엔드 개발을 맡게 되었다. 처음으로 맡는",
        "큰 프로젝트라 긴장되지만, 동시에 정말 기대된다.",
    ]

    for line in journal_text:
        c.drawString(25*mm, y, line)
        y -= 7*mm

    # 오늘의 감사
    y -= 10*mm
    c.setStrokeColor(Color(0.9, 0.7, 0.8))
    c.setFillColor(Color(1, 0.95, 0.98))
    c.setLineWidth(1.5)
    c.roundRect(20*mm, y - 25*mm, WIDTH - 40*mm, 30*mm, 3*mm, fill=1)

    c.setFillColor(Color(0.8, 0.3, 0.6))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(25*mm, y - 7*mm, "💝 오늘 감사한 일")

    y -= 13*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y, "1. 건강하게 아침 조깅을 할 수 있어서")
    y -= 6*mm
    c.drawString(30*mm, y, "2. 새로운 프로젝트 기회가 생겨서")
    y -= 6*mm
    c.drawString(30*mm, y, "3. 함께 일하는 좋은 동료들이 있어서")

    # 내일의 목표
    y -= 15*mm
    c.setFillColor(Color(0.3, 0.5, 0.8))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20*mm, y, "🎯 내일의 목표")

    y -= 8*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(25*mm, y, "☐ 프로젝트 기술 스택 학습 시작하기")
    y -= 6*mm
    c.drawString(25*mm, y, "☐ 30분 이상 운동하기")
    y -= 6*mm
    c.drawString(25*mm, y, "☐ 팀장님께 프로젝트 질문 정리해서 여쭙기")

    c.save()
    print(f"✓ Created: {filename}")


def create_recipe_note():
    """레시피 노트 예제"""
    filename = f"{OUTPUT_DIR}/example_recipe_note.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # 배경 줄
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    y = HEIGHT - 40*mm
    while y > 20*mm:
        c.line(20*mm, y, WIDTH - 20*mm, y)
        y -= 7*mm

    # 제목 영역
    c.setStrokeColor(Color(0.9, 0.6, 0.2))
    c.setFillColor(Color(1, 0.95, 0.85))
    c.setLineWidth(2)
    c.roundRect(15*mm, HEIGHT - 35*mm, WIDTH - 30*mm, 20*mm, 3*mm, fill=1)

    c.setFillColor(Color(0.8, 0.4, 0))
    c.setFont("Helvetica-Bold", 20)
    c.drawString(20*mm, HEIGHT - 24*mm, "🍝 토마토 크림 파스타")

    c.setFont("Helvetica", 10)
    c.drawString(20*mm, HEIGHT - 31*mm, "난이도: ⭐⭐ 중 | 조리시간: 25분 | 2인분")

    # 재료
    y = HEIGHT - 50*mm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(Color(0.2, 0.6, 0.3))
    c.drawString(20*mm, y, "🛒 재료")

    y -= 10*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 11)

    ingredients = [
        "주재료:",
        "  • 파스타 면 200g",
        "  • 토마토 소스 1컵",
        "  • 생크림 1/2컵",
        "  • 양파 1/2개",
        "  • 마늘 3쪽",
        "",
        "부재료:",
        "  • 올리브유 2큰술",
        "  • 파마산 치즈 가루",
        "  • 바질 (선택)",
        "  • 소금, 후추 약간",
    ]

    for line in ingredients:
        c.drawString(25*mm, y, line)
        y -= 6*mm

    # 조리 순서
    y -= 10*mm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(Color(0.8, 0.3, 0.2))
    c.drawString(20*mm, y, "👨‍🍳 조리 순서")

    y -= 10*mm
    c.setFillColor(black)
    c.setFont("Helvetica", 11)

    steps = [
        "1. 큰 냄비에 물을 끓이고 소금을 넣은 후 파스타 면을 삶는다.",
        "   (8-10분, 포장지의 조리시간 참고)",
        "",
        "2. 양파와 마늘을 잘게 다진다.",
        "",
        "3. 팬에 올리브유를 두르고 마늘을 먼저 볶다가 향이 나면",
        "   양파를 넣고 투명해질 때까지 볶는다.",
        "",
        "4. 토마토 소스를 넣고 중불에서 5분간 끓인다.",
        "",
        "5. 생크림을 넣고 잘 섞은 후 2-3분 더 끓인다.",
        "",
        "6. 삶은 파스타 면을 소스에 넣고 잘 버무린다.",
        "",
        "7. 소금, 후추로 간을 맞춘다.",
        "",
        "8. 접시에 담고 파마산 치즈와 바질을 올려 완성!",
    ]

    for line in steps:
        c.drawString(25*mm, y, line)
        y -= 6*mm

    # 팁 박스
    y -= 5*mm
    c.setStrokeColor(Color(0.4, 0.6, 0.9))
    c.setFillColor(Color(0.95, 0.97, 1))
    c.setLineWidth(1.5)
    c.roundRect(20*mm, y - 20*mm, WIDTH - 40*mm, 25*mm, 3*mm, fill=1)

    c.setFillColor(Color(0.2, 0.4, 0.8))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(25*mm, y - 6*mm, "💡 요리 팁")

    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(30*mm, y - 12*mm, "• 생크림 대신 우유를 사용해도 되지만, 크림이 더 고소해요")
    c.drawString(30*mm, y - 18*mm, "• 파스타 삶은 물을 조금 남겨두었다가 소스가 뻑뻑하면 추가하세요")

    c.save()
    print(f"✓ Created: {filename}")


def create_book_notes():
    """독서 노트 예제"""
    filename = f"{OUTPUT_DIR}/example_book_notes.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # 코넬 노트 스타일 배경
    c.setStrokeColor(MEDIUM_GRAY)
    c.setLineWidth(1)

    margin = 20*mm
    cue_column_width = 60*mm
    summary_height = 50*mm

    c.line(margin + cue_column_width, margin + summary_height,
           margin + cue_column_width, HEIGHT - margin)
    c.line(margin, margin + summary_height,
           WIDTH - margin, margin + summary_height)
    c.rect(margin, margin, WIDTH - 2*margin, HEIGHT - 2*margin)

    # 제목
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(black)
    c.drawString(margin + 5*mm, HEIGHT - 25*mm, "📚 『아침 10분의 기적』 독서 노트")

    c.setFont("Helvetica", 10)
    c.setFillColor(Color(0.5, 0.5, 0.5))
    c.drawString(margin + 5*mm, HEIGHT - 32*mm, "저자: 할 엘로드 | 2025년 12월 독서")

    # 노트 영역 (오른쪽)
    y = HEIGHT - 45*mm
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin + cue_column_width + 5*mm, y, "📖 주요 내용")

    y -= 10*mm
    c.setFont("Helvetica", 10)

    notes = [
        "• SAVERS 아침 루틴:",
        "  - Silence (침묵/명상): 5분",
        "  - Affirmations (긍정확언): 5분",
        "  - Visualization (시각화): 5분",
        "  - Exercise (운동): 20분",
        "  - Reading (독서): 20분",
        "  - Scribing (글쓰기): 5분",
        "",
        "• 핵심 메시지:",
        "  아침 시간을 활용하면 인생이 바뀐다.",
        "  일찍 일어나는 것만으로도 하루의 주도권을",
        "  가질 수 있다.",
        "",
        "• 실천 방법:",
        "  - 알람을 멀리 두어 일어날 수밖에 없게",
        "  - 전날 밤 일찍 자기",
        "  - 아침에 할 일을 미리 정해두기",
    ]

    for line in notes:
        c.drawString(margin + cue_column_width + 8*mm, y, line)
        y -= 6*mm

    # Cue 영역 (왼쪽)
    y = HEIGHT - 45*mm
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(Color(0.6, 0.3, 0.8))

    cues = [
        ("SAVERS", y),
        ("왜 아침?", y - 50*mm),
        ("실천 팁", y - 100*mm),
        ("명언", y - 130*mm),
    ]

    for cue, cue_y in cues:
        c.drawString(margin + 5*mm, cue_y, cue)

    # 명언 추가
    y = HEIGHT - 175*mm
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(Color(0.3, 0.3, 0.3))
    c.drawString(margin + cue_column_width + 8*mm, y,
                 '"당신이 아침에 일어나는 방식이')
    c.drawString(margin + cue_column_width + 8*mm, y - 6*mm,
                 ' 당신의 성공 수준을 결정한다"')

    # 요약 영역 (하단)
    y = margin + summary_height - 10*mm
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(Color(0.8, 0.4, 0))
    c.drawString(margin + 5*mm, y, "✍️ 요약 및 실천 계획")

    y -= 10*mm
    c.setFont("Helvetica", 10)
    c.setFillColor(black)

    summary = [
        "아침 시간 활용의 중요성을 깨달았다. 내일부터 6시에 일어나서 SAVERS 루틴을",
        "시작해보기로 결심. 특히 명상과 독서를 아침에 하면 하루가 더 차분하고",
        "생산적으로 시작될 것 같다. 우선 2주간 실험해보고 효과를 확인해볼 것.",
    ]

    for line in summary:
        c.drawString(margin + 5*mm, y, line)
        y -= 6*mm

    c.save()
    print(f"✓ Created: {filename}")


def main():
    print("📝 실제 내용이 채워진 노트 예제 생성 시작...\n")

    create_study_notes_python()
    create_meeting_notes()
    create_daily_journal()
    create_recipe_note()
    create_book_notes()

    print(f"\n✅ 5개의 샘플 노트가 '{OUTPUT_DIR}' 디렉토리에 생성되었습니다!")
    print("\n📋 생성된 샘플:")
    print("  1. Python 학습 노트 - 공부할 때 쓰는 노트 예제")
    print("  2. 회의록 - 프로젝트 회의 기록")
    print("  3. 일기 - 일상 기록")
    print("  4. 레시피 노트 - 요리법 정리")
    print("  5. 독서 노트 - 책 읽고 정리하기")


if __name__ == "__main__":
    main()
