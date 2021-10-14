from pico2d import *
import random



KPU_WIDTH, KPU_HEIGHT = 1280, 1024

# 이 함수는 분석할 필요 없음. 기존 코드.
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

# 이 함수는 10개의 랜덤 위치의 화살표를 화면에 그려줌. 분석 필요 없음.
def draw_all_arrows():
    for i, p in enumerate(target_points):
        arrow.draw(p[0], p[1])
        pico2d.debug_font.draw(p[0], p[1], str(i), (255,0,0))



# 이 이후의 코드에 대한 분석하면 됨.


def update_character():
    global cx, cy
    global running_right
    global p1, p2, p3, p4
    global t
    global prev_cx

    cx = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
    cy = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

    # 다음 코드가 하는 일은?
    # t를 매개변수로 하는 방정식을 따라 캐릭터가 움직일 예정인데, 이때 t가 1.0보다 크거나 같게 될 경우 목적지에 도달했다는 의미가 되어 새로운 목적지를 설정해주는 코드이다.
    t += 0.001
    if t >= 1.0:
        p1, p2, p3, p4 = get_next_four_points()
        t = 0


    # 다음 코드의 목적은?
    # 캐릭터의 좌우 스프라이트 변환을 위한 코드. 이전에 cx값이 현재 새로 설정된 cx 값보다 작다면 True 아니라면 false를 준다. 오른쪽으로 이동할 경우, 현재 cx의 위치는 이전 prev_cx의 위치보다 클 것이므로 이를 이용한 연산이다.
    running_right = cx > prev_cx
    prev_cx = cx


# 아래 코드는 어떤 식으로 4개의 포인트를 가져오는가?
# 시작 인덱스에서 4개만큼 extended_target_points를 슬라이스하여 가져온다. 이때 cur_index는 배열의 인덱스 위치를, num_points는 점의 개수를 나타낸다.
def get_next_four_points():
    global cur_index
    start = cur_index % num_points
    
    print(start)
    end = start + 4
    points = extended_target_points[start:end]
    cur_index += 1
    return points


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# prepare images
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
running_right = True
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
prev_cx = cx
frame = 0
hide_cursor()

num_points = 10
target_points = []
for i in range(num_points):
    target_points.append((random.randint(100, KPU_WIDTH-100), random.randint(100, KPU_HEIGHT-100)))

# 아래의 코드에서, target_points[:3]을 더해서, extended_target_points를 만든 이유는?
# 위에 update_character에서 cx, cy를 구하는 공식은 4점 곡선그리기에서 중간 2점을 그리는 연산이다. 이 4점 곡선 그리기를 반복적으로 수행하여 결과적으로 모든 점에 대하여 부드러운 곡선을 그리는 것인데, 4개 중 가운데 2점 사이의 부분만을 그리는 특성상 맨 마지막부분에 누락이 생긴다. 이를 해결하기 위하여 앞에 인덱스 3개를 뒤에 추가는 방식으로 확장하여 마지막 점에 대한 곡선을 효과적으로 처리할 수 있도록 준비한다.
extended_target_points = target_points + target_points[:3]
# print(extended_target_points)
cur_index = -1

t = 0
p1, p2, p3, p4 = get_next_four_points()

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_all_arrows()
    if running_right:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, cx, cy)
    update_canvas()

    frame = (frame + 1) % 8
    update_character()

    handle_events()

close_canvas()




