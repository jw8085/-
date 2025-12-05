# 굿노트 전용 템플릿 📓

굿노트(GoodNotes)에서 바로 사용할 수 있는 다양한 노트 템플릿 모음입니다.

## 📦 포함된 템플릿

### 기본 노트 템플릿
1. **01_lined_notebook.pdf** - 표준 줄 노트 (7mm 간격)
2. **02_lined_wide.pdf** - 넓은 줄 노트 (10mm 간격)
3. **03_dotted_notebook.pdf** - 점 노트 (5mm 간격)
4. **04_grid_notebook.pdf** - 모눈 노트 (5mm 격자)
5. **05_grid_small.pdf** - 작은 모눈 노트 (3mm 격자)
6. **06_blank_notebook.pdf** - 빈 노트

### 특수 목적 템플릿
7. **07_cornell_notes.pdf** - 코넬 노트 (효과적인 학습용)
8. **08_music_sheet.pdf** - 오선지 (음악 작곡용)
9. **09_weekly_planner.pdf** - 주간 플래너 (일정 관리용)

### 컬러 템플릿
10. **10_lined_blue.pdf** - 파란색 줄 노트
11. **11_lined_pink.pdf** - 핑크색 줄 노트

## 📝 실제 작성 예제 (samples 폴더)

실제로 작성된 노트 예제들을 제공합니다. 어떻게 활용할 수 있는지 참고하세요!

1. **example_python_study_notes.pdf** - Python 프로그래밍 학습 노트
   - 변수, 데이터 타입, 조건문, 반복문 정리
   - 핵심 요약 박스와 다음 학습 계획 포함

2. **example_meeting_notes.pdf** - 프로젝트 기획 회의록
   - 회의 정보, 안건, 주요 논의 내용
   - 액션 아이템과 담당자, 마감일 정리

3. **example_daily_journal.pdf** - 일상 기록 일기
   - 하루 일과와 생각 정리
   - 감사 일기와 내일의 목표 섹션

4. **example_recipe_note.pdf** - 토마토 크림 파스타 레시피
   - 재료 리스트와 조리 순서
   - 요리 팁과 포인트 정리

5. **example_book_notes.pdf** - 독서 노트 (코넬 노트 스타일)
   - 책 주요 내용 정리
   - 핵심 키워드와 요약 포함

## 🚀 사용 방법

### GoodNotes에서 템플릿 가져오기
1. 원하는 PDF 템플릿을 iPad/iPhone으로 다운로드
2. GoodNotes 앱 실행
3. 새 노트 생성 시 "템플릿" 선택
4. "가져오기" 버튼을 눌러 다운로드한 PDF 선택
5. 템플릿이 추가되어 사용 가능

### 템플릿 활용 팁
- **코넬 노트**: 왼쪽 여백에 핵심 키워드, 오른쪽에 노트, 하단에 요약 작성
- **주간 플래너**: 요일별로 할 일과 일정을 체계적으로 관리
- **오선지**: 악보 작성, 음악 이론 학습에 활용
- **점/모눈 노트**: 다이어그램, 그래프, 스케치에 유용

## 🛠️ 템플릿 커스터마이징

템플릿을 직접 수정하거나 새로 만들고 싶다면:

```bash
# 필요한 라이브러리 설치
pip install reportlab Pillow

# 빈 템플릿 생성
python3 create_templates.py

# 샘플 노트 생성 (내용이 채워진 예제)
python3 create_sample_notes.py
```

스크립트 파일을 수정하여:
- `create_templates.py`: 줄 간격, 색상, 레이아웃 조정
- `create_sample_notes.py`: 새로운 예제 노트 추가

## 📐 템플릿 사양

- **페이지 크기**: A4 (210 × 297mm)
- **여백**: 20mm (상하좌우)
- **파일 형식**: PDF
- **호환성**: GoodNotes 5/6, Notability, PDF 리더 앱

## 📝 라이선스

이 템플릿들은 자유롭게 사용, 수정, 배포할 수 있습니다.

## 🎨 제작 정보

Python과 ReportLab 라이브러리를 사용하여 프로그래밍 방식으로 생성되었습니다.

---

**즐거운 노트 작성 되세요!** ✍️
