import random
import datetime
import sys
import os

# 색상 코드
class Color:
	RESET   = "\033[0m"
	BOLD    = "\033[1m"
	DIM     = "\033[2m"

	CYAN    = "\033[96m"
	YELLOW  = "\033[93m"
	GREEN   = "\033[92m"
	MAGENTA = "\033[95m"
	BLUE    = "\033[94m"
	WHITE   = "\033[97m"
	ORANGE  = "\033[38;5;214m"
	PINK    = "\033[38;5;213m"
	TEAL    = "\033[38;5;43m"

# 데이터
DESTINATIONS = [
	{
		"city": "도쿄",
		"country": "일본 🇯🇵",
		"emoji": "🗼",
		"highlight": "벚꽃과 네온사인이 공존하는 도시",
		"tip": "신주쿠 골든가이에서 소박한 이자카야 체험을 놓치지 마세요.",
		"best_time": "3월~4월 (벚꽃 시즌)",
		"vibe": "전통 ✦ 미래 ✦ 음식천국",
	},
	{
		"city": "산토리니",
		"country": "그리스 🇬🇷",
		"emoji": "🏛️",
		"highlight": "흰 벽과 파란 지붕이 이어진 절벽 위의 낙원",
		"tip": "이아(Oia) 마을에서 일몰을 보려면 1시간 전부터 자리 잡으세요.",
		"best_time": "5월~6월 (성수기 전)",
		"vibe": "낭만 ✦ 고요 ✦ 절경",
	},
	{
		"city": "방콕",
		"country": "태국 🇹🇭",
		"emoji": "🛕",
		"highlight": "황금 사원과 길거리 음식의 도시",
		"tip": "짜오프라야 강에서 보트 택시를 타면 교통 체증을 피할 수 있어요.",
		"best_time": "11월~2월 (건기)",
		"vibe": "활기 ✦ 영성 ✦ 맛",
	},
	{
		"city": "바르셀로나",
		"country": "스페인 🇪🇸",
		"emoji": "🎨",
		"highlight": "가우디의 건축과 지중해가 만나는 곳",
		"tip": "사그라다 파밀리아는 온라인 예약 필수! 아침 첫 타임이 한산해요.",
		"best_time": "5월~6월, 9월~10월",
		"vibe": "예술 ✦ 열정 ✦ 자유",
	},
	{
		"city": "뉴욕",
		"country": "미국 🇺🇸",
		"emoji": "🗽",
		"highlight": "잠들지 않는 도시, 수천 개의 이야기가 교차하는 곳",
		"tip": "하이라인 파크를 걸으며 첼시 갤러리 투어를 해보세요.",
		"best_time": "9월~11월 (가을 단풍)",
		"vibe": "에너지 ✦ 다양성 ✦ 가능성",
	},
	{
		"city": "교토",
		"country": "일본 🇯🇵",
		"emoji": "⛩️",
		"highlight": "천년 역사가 골목마다 살아있는 고도(古都)",
		"tip": "아라시야마 대나무 숲은 이른 아침 6시에 가면 혼자 즐길 수 있어요.",
		"best_time": "11월 (단풍 절정)",
		"vibe": "고요 ✦ 전통 ✦ 선(禪)",
	},
	{
		"city": "두바이",
		"country": "아랍에미리트 🇦🇪",
		"emoji": "🏙️",
		"highlight": "사막 위에 세운 불가능을 현실로 만든 도시",
		"tip": "부르즈 할리파 전망대는 일몰 30분 전이 가장 아름다워요.",
		"best_time": "11월~3월 (선선한 겨울)",
		"vibe": "웅장 ✦ 사치 ✦ 혁신",
	},
	{
		"city": "프라하",
		"country": "체코 🇨🇿",
		"emoji": "🏰",
		"highlight": "중세 동화 속에 들어온 듯한 황금빛 도시",
		"tip": "카를교는 새벽 5시에 가면 관광객 없이 안개 낀 풍경을 즐길 수 있어요.",
		"best_time": "5월~6월, 9월",
		"vibe": "동화 ✦ 역사 ✦ 맥주",
	},
	{
		"city": "발리",
		"country": "인도네시아 🇮🇩",
		"emoji": "🌺",
		"highlight": "신들의 섬, 논밭과 파도와 사원이 공존하는 곳",
		"tip": "우붓 계단식 논밭(떼갈랄랑)은 오전 7시 전이 황금빛으로 빛나요.",
		"best_time": "4월~10월 (건기)",
		"vibe": "영성 ✦ 자연 ✦ 치유",
	},
	{
		"city": "파리",
		"country": "프랑스 🇫🇷",
		"emoji": "🗺️",
		"highlight": "사랑과 예술, 철학이 카페 한 잔에 녹아있는 도시",
		"tip": "몽마르트 언덕 계단에 앉아 크레페 하나 들고 파리를 내려다보세요.",
		"best_time": "6월~9월",
		"vibe": "낭만 ✦ 예술 ✦ 미식",
	},
	{
		"city": "이스탄불",
		"country": "튀르키예 🇹🇷",
		"emoji": "🕌",
		"highlight": "유럽과 아시아가 한 도시에서 만나는 유일한 곳",
		"tip": "그랜드 바자르 옆 이집션 바자르에서 현지인처럼 향신료를 구경해보세요.",
		"best_time": "4월~5월, 9월~10월",
		"vibe": "신비 ✦ 역사 ✦ 차이",
	},
	{
		"city": "리스본",
		"country": "포르투갈 🇵🇹",
		"emoji": "🚋",
		"highlight": "언덕과 파두 음악, 타일 벽화가 가득한 서유럽의 숨은 보석",
		"tip": "28번 트램을 타고 알파마 지구를 돌며 도시를 느껴보세요.",
		"best_time": "5월~6월, 9월~10월",
		"vibe": "서정 ✦ 郷愁 ✦ 여유",
	},
]

QUOTES = [
	("세상은 책과 같다. 여행하지 않는 사람은 책의 한 페이지만 읽은 것이다.", "성 아우구스티누스"),
	("여행은 당신을 무언가로 되돌려준다 — 당신 자신에게.", "미상"),
	("직업은 잊어버릴 수 있지만, 여행은 절대 잊히지 않는다.", "미상"),
	("여행의 목적은 도착이 아니라 그 자체다.", "조슈아 슬로컴"),
	("두려움이 가득한 삶보다, 후회가 가득한 삶을 살지 마라.", "미상"),
	("나는 내가 있는 곳이 아닌, 아직 가지 않은 곳에서 나를 찾는다.", "미상"),
	("지도에서 길을 잃는 것은, 세상에서 자신을 찾는 것이다.", "존 스타인벡"),
	("우리는 돌아왔을 때 비로소 떠난 이유를 이해한다.", "G.K. 체스터턴"),
	("언젠가는 너무 늦다. 지금 떠나라.", "미상"),
	("가장 먼 여정은 마음속에서 시작된다.", "미상"),
	("여행은 당신이 집에서 가지고 있던 편견을 부숴준다.", "마크 트웨인"),
	("모든 여행은 처음에는 약간 무질서하게 시작된다.", "존 스타인벡"),
	("여행하는 자는 많지만, 진정으로 보는 자는 적다.", "귀스타브 플로베르"),
	("낯선 곳에서의 하루는 고향에서의 한 달보다 더 많은 것을 가르쳐준다.", "미상"),
	("멀리 보면 두려움이 생기고, 가까이 가면 아름다움이 보인다.", "미상"),
	("비행기 티켓은 그 어떤 치료제보다 낫다.", "미상"),
	("짐을 싸는 순간 이미 여행은 시작된 것이다.", "미상"),
	("길을 잃는 것을 두려워하지 마라. 그게 곧 발견이다.", "미상"),
]

# 유틸
def get_daily_seed():
	"""날짜 기반 시드 — 하루에 하나씩 바뀜"""
	today = datetime.date.today()
	return today.year * 10000 + today.month * 100 + today.day

def pick_daily(items):
	rng = random.Random(get_daily_seed())
	return rng.choice(items)

def terminal_width():
	try:
		return os.get_terminal_size().columns
	except:
		return 72

def divider(char="─", color=Color.DIM):
	w = min(terminal_width(), 72)
	print(f"{color}{char * w}{Color.RESET}")

def center(text, width=72):
	# strip ANSI for length calculation
	import re
	plain = re.sub(r'\033\[[0-9;]*m', '', text)
	pad = max(0, (width - len(plain)) // 2)
	print(" " * pad + text)

# 렌더링
def print_header():
	today = datetime.date.today()
	day_str = today.strftime("%Y년 %m월 %d일")
	weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
	weekday = weekdays[today.weekday()]

	print()
	divider("═", Color.CYAN)
	center(f"{Color.BOLD}{Color.CYAN}  🌍  W A N D E R L U S T  🌍  {Color.RESET}")
	center(f"{Color.DIM}{day_str} {weekday}{Color.RESET}")
	divider("═", Color.CYAN)

def print_quote(quote, author):
	print()
	print(f"  {Color.YELLOW}{Color.BOLD}✦ 오늘의 명언{Color.RESET}")
	print()

	# 긴 명언 줄바꿈
	words = quote
	max_w = min(terminal_width(), 72) - 6
	if len(words) > max_w:
		mid = len(words) // 2
		# 중간 공백 찾기
		split = words.rfind(' ', 0, mid + 10)
		if split == -1:
			split = mid
		line1 = words[:split]
		line2 = words[split:].strip()
		print(f"  {Color.WHITE}❝ {line1}{Color.RESET}")
		print(f"  {Color.WHITE}  {line2} ❞{Color.RESET}")
	else:
		print(f"  {Color.WHITE}❝ {words} ❞{Color.RESET}")

	print()
	print(f"  {Color.DIM}— {author}{Color.RESET}")

def print_destination(dest):
	print()
	divider("·", Color.DIM + Color.CYAN)
	print()
	print(f"  {Color.MAGENTA}{Color.BOLD}✈  오늘의 여행지{Color.RESET}")
	print()
	print(f"  {dest['emoji']}  {Color.BOLD}{Color.CYAN}{dest['city']}{Color.RESET}  {Color.DIM}{dest['country']}{Color.RESET}")
	print()
	print(f"  {Color.WHITE}{dest['highlight']}{Color.RESET}")
	print()
	print(f"  {Color.TEAL}분위기{Color.RESET}   {Color.DIM}{dest['vibe']}{Color.RESET}")
	print(f"  {Color.TEAL}최적 시기{Color.RESET} {Color.DIM}{dest['best_time']}{Color.RESET}")
	print()
	print(f"  {Color.YELLOW}💡 여행 팁{Color.RESET}")
	print(f"  {Color.DIM}{dest['tip']}{Color.RESET}")

def print_footer():
	print()
	divider("─", Color.DIM)
	msgs = [
		"언젠가가 아니라, 지금 꿈을 키워요 🌱",
		"오늘 하루도 그 여행을 향해 한 걸음씩! 🚀",
		"힘들 때일수록, 가고 싶은 곳을 떠올려요 ✨",
		"버티는 오늘이 내일의 여행을 만들어줍니다 💪",
	]
	rng = random.Random(get_daily_seed() + 1)
	print(f"\n  {Color.PINK}{rng.choice(msgs)}{Color.RESET}\n")
	divider("─", Color.DIM)
	print()

def show_help():
	print(f"""
{Color.CYAN}{Color.BOLD}Wanderlust CLI 사용법{Color.RESET}

{Color.YELLOW}python wanderlust.py{Color.RESET}          오늘의 명언 + 여행지 보기
{Color.YELLOW}python wanderlust.py list{Color.RESET}     모든 여행지 목록 보기
{Color.YELLOW}python wanderlust.py random{Color.RESET}   랜덤 여행지 보기 (오늘과 다를 수 있음)
{Color.YELLOW}python wanderlust.py help{Color.RESET}     도움말
""")

def show_list():
	print()
	divider("═", Color.CYAN)
	center(f"{Color.BOLD}{Color.CYAN}  📍 여행지 목록  {Color.RESET}")
	divider("═", Color.CYAN)
	print()
	for i, d in enumerate(DESTINATIONS, 1):
		print(f"  {Color.DIM}{i:02d}.{Color.RESET} {d['emoji']} {Color.BOLD}{d['city']}{Color.RESET}  {Color.DIM}{d['country']}{Color.RESET}")
	print()

# 메인
def main():
	args = sys.argv[1:]
	cmd = args[0].lower() if args else ""

	if cmd == "help":
		show_help()
		return

	if cmd == "list":
		show_list()
		return

	if cmd == "random":
		dest = random.choice(DESTINATIONS)
		quote, author = random.choice(QUOTES)
	else:
		dest = pick_daily(DESTINATIONS)
		quote, author = pick_daily(QUOTES)

	print_header()
	print_quote(quote, author)
	print_destination(dest)
	print_footer()

if __name__ == "__main__":
	main()
 
