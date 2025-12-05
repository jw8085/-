#!/usr/bin/env python3
"""
GoodNotes Template Generator
다양한 스타일의 굿노트 전용 템플릿을 생성합니다.
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import Color
import os

# 출력 디렉토리
OUTPUT_DIR = "templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# A4 크기
WIDTH, HEIGHT = A4

# 색상 정의
LIGHT_GRAY = Color(0.8, 0.8, 0.8, alpha=0.3)
MEDIUM_GRAY = Color(0.6, 0.6, 0.6, alpha=0.4)
LIGHT_BLUE = Color(0.7, 0.8, 0.9, alpha=0.3)
LIGHT_PINK = Color(0.95, 0.8, 0.85, alpha=0.3)


def create_lined_template(filename, line_spacing=7*mm, color=LIGHT_GRAY):
    """줄 노트 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setStrokeColor(color)
    c.setLineWidth(0.5)

    # 상단 여백
    margin_top = 20*mm
    margin_bottom = 20*mm

    y = HEIGHT - margin_top
    while y > margin_bottom:
        c.line(20*mm, y, WIDTH - 20*mm, y)
        y -= line_spacing

    c.save()
    print(f"✓ Created: {filename}")


def create_dotted_template(filename, dot_spacing=5*mm, color=MEDIUM_GRAY):
    """점 노트 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setStrokeColor(color)
    c.setFillColor(color)

    margin = 20*mm
    dot_size = 0.8

    x = margin
    while x < WIDTH - margin:
        y = margin
        while y < HEIGHT - margin:
            c.circle(x, y, dot_size, fill=1)
            y += dot_spacing
        x += dot_spacing

    c.save()
    print(f"✓ Created: {filename}")


def create_grid_template(filename, grid_spacing=5*mm, color=LIGHT_GRAY):
    """모눈 노트 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setStrokeColor(color)
    c.setLineWidth(0.3)

    margin = 20*mm

    # 세로선
    x = margin
    while x < WIDTH - margin + 1:
        c.line(x, margin, x, HEIGHT - margin)
        x += grid_spacing

    # 가로선
    y = margin
    while y < HEIGHT - margin + 1:
        c.line(margin, y, WIDTH - margin, y)
        y += grid_spacing

    c.save()
    print(f"✓ Created: {filename}")


def create_blank_template(filename, color=Color(1, 1, 1)):
    """빈 노트 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFillColor(color)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    c.save()
    print(f"✓ Created: {filename}")


def create_cornell_template(filename):
    """코넬 노트 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setStrokeColor(MEDIUM_GRAY)
    c.setLineWidth(1)

    margin = 20*mm
    cue_column_width = 60*mm
    summary_height = 50*mm
    line_spacing = 7*mm

    # 왼쪽 세로선 (Cue Column)
    c.line(margin + cue_column_width, margin + summary_height,
           margin + cue_column_width, HEIGHT - margin)

    # 하단 가로선 (Summary)
    c.line(margin, margin + summary_height,
           WIDTH - margin, margin + summary_height)

    # 테두리
    c.rect(margin, margin, WIDTH - 2*margin, HEIGHT - 2*margin)

    # 노트 영역 줄
    c.setLineWidth(0.3)
    c.setStrokeColor(LIGHT_GRAY)
    y = HEIGHT - margin - line_spacing
    while y > margin + summary_height:
        c.line(margin + cue_column_width, y, WIDTH - margin, y)
        y -= line_spacing

    c.save()
    print(f"✓ Created: {filename}")


def create_music_template(filename):
    """오선지 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setStrokeColor(Color(0, 0, 0))
    c.setLineWidth(0.5)

    margin = 20*mm
    staff_height = 8*mm
    staff_spacing = 15*mm

    y = HEIGHT - margin - 10*mm

    while y > margin + staff_height:
        # 5줄의 오선
        for i in range(5):
            line_y = y - (i * 2*mm)
            c.line(margin, line_y, WIDTH - margin, line_y)
        y -= staff_height + staff_spacing

    c.save()
    print(f"✓ Created: {filename}")


def create_weekly_planner(filename):
    """주간 플래너 템플릿 생성"""
    c = canvas.Canvas(filename, pagesize=A4)
    c.setStrokeColor(MEDIUM_GRAY)
    c.setLineWidth(1)
    c.setFont("Helvetica", 10)

    margin = 15*mm
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # 제목
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, HEIGHT - margin, "Weekly Planner")

    # 요일별 섹션
    section_height = (HEIGHT - 3*margin - 15*mm) / 7
    y = HEIGHT - margin - 20*mm

    c.setFont("Helvetica-Bold", 11)
    for day in days:
        c.rect(margin, y - section_height, WIDTH - 2*margin, section_height)
        c.drawString(margin + 5*mm, y - 5*mm, day)

        # 줄
        c.setLineWidth(0.3)
        c.setStrokeColor(LIGHT_GRAY)
        line_y = y - 10*mm
        while line_y > y - section_height + 3*mm:
            c.line(margin + 30*mm, line_y, WIDTH - margin - 3*mm, line_y)
            line_y -= 5*mm

        c.setStrokeColor(MEDIUM_GRAY)
        c.setLineWidth(1)
        y -= section_height

    c.save()
    print(f"✓ Created: {filename}")


def main():
    print("🎨 굿노트 템플릿 생성 시작...\n")

    # 기본 템플릿
    create_lined_template(f"{OUTPUT_DIR}/01_lined_notebook.pdf")
    create_lined_template(f"{OUTPUT_DIR}/02_lined_wide.pdf", line_spacing=10*mm)
    create_dotted_template(f"{OUTPUT_DIR}/03_dotted_notebook.pdf")
    create_grid_template(f"{OUTPUT_DIR}/04_grid_notebook.pdf")
    create_grid_template(f"{OUTPUT_DIR}/05_grid_small.pdf", grid_spacing=3*mm)
    create_blank_template(f"{OUTPUT_DIR}/06_blank_notebook.pdf")

    # 특수 템플릿
    create_cornell_template(f"{OUTPUT_DIR}/07_cornell_notes.pdf")
    create_music_template(f"{OUTPUT_DIR}/08_music_sheet.pdf")
    create_weekly_planner(f"{OUTPUT_DIR}/09_weekly_planner.pdf")

    # 색상 변형
    create_lined_template(f"{OUTPUT_DIR}/10_lined_blue.pdf", color=LIGHT_BLUE)
    create_lined_template(f"{OUTPUT_DIR}/11_lined_pink.pdf", color=LIGHT_PINK)

    print(f"\n✅ 총 11개의 템플릿이 '{OUTPUT_DIR}' 디렉토리에 생성되었습니다!")
    print("\n📝 생성된 템플릿:")
    print("  - 줄 노트 (기본, 넓은 간격)")
    print("  - 점 노트")
    print("  - 모눈 노트 (일반, 작은 칸)")
    print("  - 빈 노트")
    print("  - 코넬 노트")
    print("  - 오선지")
    print("  - 주간 플래너")
    print("  - 컬러 줄 노트 (파란색, 핑크색)")


if __name__ == "__main__":
    main()
