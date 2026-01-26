init python:
    
    def gameee():

        import pygame
        import sys
        import os
        import random
        import renpy
        # --- [1] 설정 및 상수 정의 ---
        current_path = renpy.game.scriptpath
        image_path = os.path.join(current_path, "background.png")

        global cost #땅값
        cost=10000

        # 맵 설정
        TILE_SIZE = 8
        MAP_WIDTH = 96
        MAP_HEIGHT = 64
        MAP_PIXEL_WIDTH = MAP_WIDTH * TILE_SIZE
        MAP_PIXEL_HEIGHT = MAP_HEIGHT * TILE_SIZE

        # UI 설정
        UI_WIDTH = 300
        UI_BG_COLOR = (40, 40, 40)

        # 타일 ID
        TILE_WATER = 0
        TILE_GROUND = 1
        TILE_PLAYER = 2
        TILE_ENEMY_START = 3

        # 유닛 ID
        UNIT_MELEE = 1
        UNIT_RANGED = 2
        UNIT_ADV_MELEE = 3
        UNIT_ADV_RANGED = 4
        UNIT_SHIP = 5
        UNIT_ADV_SHIP = 6

        # 색상 정의
        COLOR_PLAYER = (255, 50, 50)
        COLOR_WATER = (0, 100, 255)
        COLOR_GROUND = (100, 200, 50)
        COLOR_NORMAL = (100, 100, 100)
        COLOR_HOVER = (150, 150, 150)
        COLOR_TEXT = (255, 255, 255)

        ENEMY_COLORS = [
            (255, 0, 255),
            (255, 165, 0),
            (0, 0, 0),
            (150, 50, 250),
            (50, 255, 255)
        ]

        # 유닛 스펙
        UNIT_SPECS = {
            UNIT_MELEE:      {'cost': 200,   'name': "Melee",      'color': (200, 200, 200)},
            UNIT_RANGED:     {'cost': 400,   'name': "Ranged",     'color': (200, 100, 100)},
            UNIT_ADV_MELEE:  {'cost': 2000,  'name': "Adv.Melee",  'color': (50, 50, 50)},
            UNIT_ADV_RANGED: {'cost': 4000,  'name': "Adv.Ranged", 'color': (100, 0, 0)},
            UNIT_SHIP:       {'cost': 2000,  'name': "Ship",       'color': (0, 0, 255)},
            UNIT_ADV_SHIP:   {'cost': 20000, 'name': "Adv.Ship",   'color': (0, 255, 255)},
        }

        # 유닛 픽셀 데이터
        PIXELS1 = [(3,1),(4,1),(3,2),(4,2),(3,3),(4,3),(3,4),(4,4),(3,5),(4,5),(3,6),(4,6),(2,5),(5,5)]
        PIXELS2 = [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(2,1),(4,1)]
        PIXELS3 = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(1,2),(6,2),(1,3),(6,3),(3,2),(4,2)]
        PIXELS4 = [(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(1,3),(1,5),(2,4),(4,2),(4,4),(4,6),(5,3),(5,4),(5,5),(6,4)]
        PIXELS5 = [(1,4),(2,5),(3,5),(4,5),(5,5),(6,4),(4,1),(4,2),(4,3),(4,4),(5,2)]
        PIXELS6 = [(3,1),(4,1),(3,2),(4,2),(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),
                (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5)]


        # --- [2] 함수 정의 ---

        def count_neighbors(grid, x, y):
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x = x + i
                    neighbor_y = y + j
                    if i == 0 and j == 0: continue
                    if neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= MAP_WIDTH or neighbor_y >= MAP_HEIGHT:
                        count += 1
                    elif grid[neighbor_y][neighbor_x] == TILE_GROUND:
                        count += 1
            return count

        def smooth_map(input_map):
            temp_map = [[0] * MAP_WIDTH for _ in range(MAP_HEIGHT)]
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    ground_neighbors = count_neighbors(input_map, x, y)
                    if ground_neighbors > 4:
                        temp_map[y][x] = TILE_GROUND
                    else:
                        temp_map[y][x] = TILE_WATER
            return temp_map

        def create_random_map():
            global nation_capitals
            nation_capitals = {}
            new_map = [[0] * MAP_WIDTH for _ in range(MAP_HEIGHT)]
            
            # 1. 랜덤 생성
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    if random.randint(0, 100) < 60:
                        new_map[y][x] = TILE_GROUND
                    else:
                        new_map[y][x] = TILE_WATER
            
            # 2. 다듬기
            for _ in range(7):
                new_map = smooth_map(new_map)
            
            # 3. 시작점 선정
            ground_coords = []
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    if new_map[y][x] == TILE_GROUND:
                        ground_coords.append((x, y))
            
            if len(ground_coords) < 6:
                return new_map
                
            seeds = random.sample(ground_coords, 6)
            
            for i, (sx, sy) in enumerate(seeds):
                if i == 0:
                    nation_id = TILE_PLAYER
                else:
                    nation_id = TILE_ENEMY_START + (i - 1)
                
                new_map[sy][sx] = nation_id
                nation_capitals[nation_id] = (sx, sy)
                
            return new_map 

        # [핵심] 주인 ID를 받아서 유닛 색상을 결정하는 함수
        def get_unit_image(u_type, owner_id):
            image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)

            # 1. 주인의 색상 결정 (플레이어는 무조건 빨강!)
            if owner_id == TILE_PLAYER:
                base_color = COLOR_PLAYER
            elif owner_id >= TILE_ENEMY_START:
                idx = owner_id - TILE_ENEMY_START
                if 0 <= idx < len(ENEMY_COLORS):
                    base_color = ENEMY_COLORS[idx]
                else:
                    base_color = (100, 100, 100)
            else:
                base_color = UNIT_SPECS[u_type]['color'] # 기본값

            # 2. 배경 몸통 그리기
            pygame.draw.rect(image, base_color, (1, 1, 6, 6))
            
            # 3. 픽셀 도트 찍기 (검은색)
            pixels_to_draw = []
            if u_type == UNIT_MELEE: pixels_to_draw = PIXELS1
            elif u_type == UNIT_RANGED: pixels_to_draw = PIXELS2
            elif u_type == UNIT_ADV_MELEE: pixels_to_draw = PIXELS3
            elif u_type == UNIT_ADV_RANGED: pixels_to_draw = PIXELS4
            elif u_type == UNIT_SHIP: pixels_to_draw = PIXELS5
            elif u_type == UNIT_ADV_SHIP: pixels_to_draw = PIXELS6

            for px, py in pixels_to_draw:
                if 0 <= px < TILE_SIZE and 0 <= py < TILE_SIZE:
                    image.set_at((px, py), (0, 0, 0))

            return image


        # --- [3] 초기화 및 메인 실행 ---

        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("World Conquest")

        font = pygame.font.SysFont("malgungothic", 50)
        ui_font = pygame.font.SysFont("malgungothic", 15)

        # 이미지 로드 (없으면 검은 배경)
        try:
            background_img = pygame.image.load(image_path)
            background_img = pygame.transform.scale(background_img, (1280, 720))
        except FileNotFoundError:
            background_img = None
        except:
            background_img = None

        # 전역 변수 초기화
        world_map = []
        nation_money = {}
        nation_capitals = {}
        units = []
        unit_images = {}
        game_logs = []

        # 이미지 캐시 생성
        def load_all_unit_images():
            all_owners = [TILE_PLAYER] + [TILE_ENEMY_START + i for i in range(5)]
            for u_type in UNIT_SPECS.keys():
                for owner_id in all_owners:
                    unit_images[(u_type, owner_id)] = get_unit_image(u_type, owner_id)
        load_all_unit_images()

        def add_log(msg):
            game_logs.append(msg)
            if len(game_logs) > 5:
                game_logs.pop(0)

        # UI 객체 정의
        UI_RECT = pygame.Rect(1280 - UI_WIDTH, 0, UI_WIDTH, 720)
        start_button = pygame.Rect(500, 400, 200, 60)

        BTN_MODE_RECT = pygame.Rect(1280 - UI_WIDTH + 10, 50, UI_WIDTH - 20, 40)
        LOG_RECT = pygame.Rect(1280 - UI_WIDTH + 10, 100, UI_WIDTH - 20, 120)
        BTN_BUY_RECT = pygame.Rect(1280 - UI_WIDTH + 10, 240, UI_WIDTH - 20, 50)

        # 유닛 컨트롤 버튼
        ctrl_buttons = []
        ctrl_labels = ["MOVE", "HOLD", "DISBAND"]
        for i, label in enumerate(ctrl_labels):
            rect = pygame.Rect(1280 - UI_WIDTH + 10, 240 + (i * 50), UI_WIDTH - 20, 40)
            ctrl_buttons.append((rect, label))

        # 유닛 생산 버튼
        unit_buttons = []
        land_menu_start_y = 300
        keys = sorted(UNIT_SPECS.keys())
        for i, u_type in enumerate(keys):
            col = i % 2
            row = i // 2
            btn_w = 135
            btn_h = 40
            gap = 10
            bx = (1280 - UI_WIDTH + 10) + (col * (btn_w + gap))
            by = land_menu_start_y + (row * (btn_h + gap))
            rect = pygame.Rect(bx, by, btn_w, btn_h)
            unit_buttons.append((rect, u_type))

        # [카메라 변수]
        cam_zoom = 3.0      # 기본 확대 배율 (3배)
        cam_x = 0      # 카메라 위치 (화면 중앙에 올 맵 좌표)
        cam_y = 0
        is_dragging = False
        last_mouse_pos = (0, 0)

        # 상태 변수
        current_state = "MENU"
        ui_mode = "LAND"
        selected_tile = None
        selected_unit = None
        is_moving = False

        # 타이머
        RESOURCE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(RESOURCE_EVENT, 1000)

        running = True
        while running:
            # --- 이벤트 처리 ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # [카메라 줌] - 휠 이벤트
                if event.type == pygame.MOUSEWHEEL and current_state == "GAME":
                    if event.y > 0: # Zoom In
                        cam_zoom = min(cam_zoom + 0.5, 6.0)
                    elif event.y < 0: # Zoom Out
                        cam_zoom = max(cam_zoom - 0.5, 1.0)

                # [카메라 이동] - 우클릭 드래그
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3: # 우클릭
                        is_dragging = True
                        last_mouse_pos = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        is_dragging = False
                elif event.type == pygame.MOUSEMOTION:
                    if is_dragging:
                        dx = event.pos[0] - last_mouse_pos[0]
                        dy = event.pos[1] - last_mouse_pos[1]
                        cam_x += dx
                        cam_y += dy
                        last_mouse_pos = event.pos

                # [자원 증가 이벤트]
                if event.type == RESOURCE_EVENT and current_state == "GAME":
                    current_tile_counts = {}
                    for y in range(MAP_HEIGHT):
                        for x in range(MAP_WIDTH):
                            tile_val = world_map[y][x]
                            if tile_val >= TILE_PLAYER:
                                if tile_val not in current_tile_counts:
                                    current_tile_counts[tile_val] = 0
                                current_tile_counts[tile_val] += 1

                    for nid, count in current_tile_counts.items():
                        income = count * 10
                        if nid not in nation_money:
                            nation_money[nid] = 10000
                        nation_money[nid] += income

                # [메뉴 상태 로직]
                if current_state == "MENU":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start_button.collidepoint(event.pos):
                            world_map = create_random_map()
                            nation_money = {}
                            units = []
                            # 맵 중앙으로 카메라 초기화
                            cam_x = (1280 - UI_WIDTH) // 2 - (MAP_PIXEL_WIDTH * cam_zoom) // 2
                            cam_y = 720 // 2 - (MAP_PIXEL_HEIGHT * cam_zoom) // 2
                            
                            current_state = "GAME"
                            print("새로운 맵 생성 완료!")
                
                # [게임 상태 로직]
                elif current_state == "GAME":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # 좌클릭만 처리 (우클릭은 카메라 이동)
                            mouse_pos = event.pos
                            
                            # [공통] 모드 전환
                            if BTN_MODE_RECT.collidepoint(mouse_pos):
                                if ui_mode == "LAND":
                                    ui_mode = "UNIT"
                                    selected_tile = None
                                    add_log("Mode: UNIT CONTROL")
                                else:
                                    ui_mode = "LAND"
                                    selected_unit = None
                                    add_log("Mode: LAND MANAGEMENT")
                            
                            # [CASE A] 영토 관리 모드
                            elif ui_mode == "LAND":
                                # [중요] 마우스 클릭 좌표 -> 그리드 좌표 변환 (카메라 적용)
                                map_mouse_x = mouse_pos[0] - cam_x
                                map_mouse_y = mouse_pos[1] - cam_y
                                
                                grid_x = int(map_mouse_x // (TILE_SIZE * cam_zoom))
                                grid_y = int(map_mouse_y // (TILE_SIZE * cam_zoom))
                                
                                # [추가된 로직] 1. 이동 모드 활성화 시 이동 처리  
                                if is_moving and selected_unit:  
                                # 맵 영역 안쪽을 클릭했는지 확인  
                                    if 0 <= grid_x < MAP_WIDTH and 0 <= grid_y < MAP_HEIGHT and mouse_pos[0] < 1280 - UI_WIDTH:  
                                # 유닛 좌표 갱신  
                                        selected_unit['x'] = grid_x  
                                        selected_unit['y'] = grid_y  
                                        add_log(f"Unit moved to ({grid_x}, {grid_y})")  
                                        is_moving = False  # 이동 완료 후 모드 해제  
                                        continue  # 이동했으면 선택 로직은 건너뜀

                                # 2. 유닛 선택 로직 (이동 모드가 아닐 때)  
                                if 0 <= grid_x < MAP_WIDTH and 0 <= grid_y < MAP_HEIGHT and mouse_pos[0] < 1280 - UI_WIDTH:  
                                    clicked_unit = None  
                                    for u in units:  
                                        if u['x'] == grid_x and u['y'] == grid_y:  
                                            clicked_unit = u  
                                            break  
            
                                        if clicked_unit:  
                                            if clicked_unit['owner'] == TILE_PLAYER:  
                                                selected_unit = clicked_unit  
                                                is_moving = False # 유닛을 새로 찍으면 이동 모드 취소  
                                                add_log("Unit Selected!")  
                                            else:  
                                                add_log("Enemy Unit.")  
                                        else:  
            # 빈 땅을 찍으면 선택 해제 (이동 모드가 아닐 때)  
                                            if not is_moving:  
                                                selected_unit = None  
                                # 3. 유닛 컨트롤 버튼 처리  
                                for rect, label in ctrl_buttons:  
                                    if rect.collidepoint(mouse_pos):  
                                        if selected_unit:  
                                            if label == "MOVE":  
                                                is_moving = True  # <--- 이동 모드 활성화  
                                                add_log("Select target tile to Move...")  
                                            elif label == "HOLD":  
                                                is_moving = False  
                                                add_log("Order: HOLD Position")  
                                            elif label == "DISBAND":  
                                                units.remove(selected_unit)  
                                                selected_unit = None  
                                                is_moving = False  
                                                add_log("Unit Disbanded.")  
                                        else:  
                                            add_log("Select Unit First!")
            




                                # 1. 지도 클릭 (땅 선택)
                                if 0 <= grid_x < MAP_WIDTH and 0 <= grid_y < MAP_HEIGHT and mouse_pos[0] < 1280 - UI_WIDTH:
                                    selected_tile = (grid_x, grid_y)
                                    add_log(f"Tile ({grid_x}, {grid_y}) Selected")
                                
                                # 2. 땅 구매 버튼
                                elif BTN_BUY_RECT.collidepoint(event.pos):
                                    if selected_tile:
                                        sx, sy = selected_tile
                                        target_tile = world_map[sy][sx]
                                        if target_tile == TILE_GROUND:
                                            cost = 10000
                                            my_money = nation_money.get(TILE_PLAYER, 0)
                                            if my_money >= cost:
                                                nation_money[TILE_PLAYER] -= cost
                                                world_map[sy][sx] = TILE_PLAYER
                                                add_log(f"Bought Land! (-{cost}G)")
                                            else:
                                                add_log("Not enough Gold!")
                                        else:
                                            add_log("Invalid Target!")
                                    else:
                                        add_log("Select a tile first.")
                                
                                # 3. 유닛 생산 버튼
                                else:
                                    for btn_rect, u_type in unit_buttons:
                                        if btn_rect.collidepoint(event.pos):
                                            spec = UNIT_SPECS[u_type]
                                            if not selected_tile:
                                                add_log("Select land first!")
                                                break
                                            
                                            sx, sy = selected_tile
                                            if world_map[sy][sx] != TILE_PLAYER:
                                                add_log("Must select YOUR land!")
                                                break
                                            if nation_money.get(TILE_PLAYER, 0) < spec['cost']:
                                                add_log("Not enough Gold!")
                                                break
                                            
                                            spawn_x, spawn_y = sx, sy
                                            can_spawn = True
                                            
                                            if u_type == UNIT_SHIP:
                                                found_water = False
                                                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                                    nx, ny = sx + dx, sy + dy
                                                    if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                                                        if world_map[ny][nx] == TILE_WATER:
                                                            spawn_x, spawn_y = nx, ny
                                                            found_water = True
                                                            break
                                                if not found_water:
                                                    add_log("No water nearby!")
                                                    can_spawn = False
                                            
                                            if can_spawn:
                                                nation_money[TILE_PLAYER] -= spec['cost']
                                                new_unit = {
                                                    'type': u_type,
                                                    'x': spawn_x,
                                                    'y': spawn_y,
                                                    'owner': TILE_PLAYER,
                                                    'hp': 100
                                                }
                                                units.append(new_unit)
                                                add_log(f"Spawned {spec['name']}!")
                                            break 

                            # [CASE B] 유닛 지휘 모드
                            elif ui_mode == "UNIT":
                                map_mouse_x = mouse_pos[0] - cam_x
                                map_mouse_y = mouse_pos[1] - cam_y
                                grid_x = int(map_mouse_x // (TILE_SIZE * cam_zoom))
                                grid_y = int(map_mouse_y // (TILE_SIZE * cam_zoom))
                                
                                # 유닛 선택
                                if 0 <= grid_x < MAP_WIDTH and 0 <= grid_y < MAP_HEIGHT and mouse_pos[0] < 1280 - UI_WIDTH:
                                    clicked_unit = None
                                    for u in units:
                                        if u['x'] == grid_x and u['y'] == grid_y:
                                            clicked_unit = u
                                            break
                                    if clicked_unit:
                                        if clicked_unit['owner'] == TILE_PLAYER:
                                            selected_unit = clicked_unit
                                            add_log("Unit Selected!")
                                        else:
                                            add_log("Enemy Unit.")
                                    else:
                                        selected_unit = None
                                
                                # 유닛 컨트롤 버튼
                                for rect, label in ctrl_buttons:
                                    if rect.collidepoint(mouse_pos):
                                        if selected_unit:
                                            add_log(f"Order: {label}")
                                        else:
                                            add_log("Select Unit First!")

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            current_state = "MENU"

            # --- 화면 그리기 ---
            if current_state == "MENU":
                if background_img:
                    screen.blit(background_img, (0, 0))
                else:
                    screen.fill((20, 20, 20))
                
                pygame.draw.rect(screen, COLOR_NORMAL, start_button)
                text_surf = font.render("게임시작", True, COLOR_TEXT)
                text_rect = text_surf.get_rect(center=start_button.center)
                screen.blit(text_surf, text_rect)
                title = font.render("WORLD", True, (0, 0, 0))
                screen.blit(title, (510, 150))

            elif current_state == "GAME":
                screen.fill((0,0,0))
                
                # [지도 그리기] - 카메라 적용
                current_tile_size = TILE_SIZE * cam_zoom
                
                for y in range(MAP_HEIGHT):
                    for x in range(MAP_WIDTH):
                        draw_x = (x * current_tile_size) + cam_x
                        draw_y = (y * current_tile_size) + cam_y
                        
                        # 화면 밖이면 건너뛰기 (최적화)
                        if draw_x > 1280 - UI_WIDTH or draw_x + current_tile_size < 0: continue
                        if draw_y > 720 or draw_y + current_tile_size < 0: continue
                        
                        rect = (draw_x, draw_y, current_tile_size, current_tile_size)
                        # 틈새 방지를 위해 약간 크게 그림
                        draw_rect = (draw_x, draw_y, current_tile_size + 1, current_tile_size + 1)
                        
                        tile_val = world_map[y][x]
                        
                        if tile_val == TILE_WATER:
                            pygame.draw.rect(screen, COLOR_WATER, draw_rect)
                        elif tile_val == TILE_GROUND:
                            pygame.draw.rect(screen, COLOR_GROUND, draw_rect)
                        elif tile_val == TILE_PLAYER:
                            pygame.draw.rect(screen, COLOR_PLAYER, draw_rect)
                        elif tile_val >= TILE_ENEMY_START:
                            enemy_idx = tile_val - TILE_ENEMY_START
                            if 0 <= enemy_idx < len(ENEMY_COLORS):
                                pygame.draw.rect(screen, ENEMY_COLORS[enemy_idx], draw_rect)
                            else:
                                pygame.draw.rect(screen, (255, 255, 255), draw_rect)
                
                # 수도(왕관) 그리기
                for nid, (cx, cy) in nation_capitals.items():
                    k_x = (cx * current_tile_size) + cam_x
                    k_y = (cy * current_tile_size) + cam_y
                    crown_points = [  
            (k_x + 1, k_y + 2),  
            (k_x + 1, k_y + 3),  
            (k_x + 1, k_y + 4),  
            (k_x + 1, k_y + 5),  
            (k_x + 2, k_y + 3),
            (k_x + 2, k_y + 5),
            (k_x + 3, k_y + 2),
            (k_x + 3, k_y + 5),  
            (k_x + 4, k_y + 2),
            (k_x + 4, k_y + 5), 
            (k_x + 5, k_y + 3),
            (k_x + 5, k_y + 5),
            (k_x + 6, k_y + 2),  
            (k_x + 6, k_y + 3),  
            (k_x + 6, k_y + 4),  
            (k_x + 6, k_y + 5)    
            ]  
                    pygame.draw.polygon(screen, (255, 255, 0), crown_points)

                # 유닛 그리기 (확대/축소 적용)
                for u in units:
                    ux = (u['x'] * current_tile_size) + cam_x
                    uy = (u['y'] * current_tile_size) + cam_y
                    
                    u_key = (u['type'], u['owner'])
                    if u_key in unit_images:
                        u_img = unit_images[u_key]
                        # 이미지 확대
                        scaled_img = pygame.transform.scale(u_img, (int(current_tile_size), int(current_tile_size)))
                        screen.blit(scaled_img, (ux, uy))
                    
                    if ui_mode == "UNIT" and selected_unit == u:
                        pygame.draw.rect(screen, (0, 255, 0), (ux-2, uy-2, current_tile_size+4, current_tile_size+4), 2)
                        color = (255, 0, 0) if is_moving else (0, 255, 0)  
                        pygame.draw.rect(screen, color, (ux-2, uy-2, current_tile_size+4, current_tile_size+4), 2)
                # 선택된 타일 테두리
                if selected_tile:
                    sx, sy = selected_tile
                    sel_x = (sx * current_tile_size) + cam_x
                    sel_y = (sy * current_tile_size) + cam_y
                    pygame.draw.rect(screen, (255, 255, 0), (sel_x, sel_y, current_tile_size, current_tile_size), 2)

                # [UI 영역 그리기] (지도를 다 그린 후 위에 덮어씀)
                pygame.draw.rect(screen, UI_BG_COLOR, UI_RECT)
                pygame.draw.line(screen, (255, 255, 255), (1280 - UI_WIDTH, 0), (1280 - UI_WIDTH, 720), 2)
                
                # 모드 버튼
                mode_color = (100, 200, 100) if ui_mode == "LAND" else (200, 100, 100)
                pygame.draw.rect(screen, mode_color, BTN_MODE_RECT)
                pygame.draw.rect(screen, (255, 255, 255), BTN_MODE_RECT, 2)
                mode_text = f"MODE: {ui_mode}"
                text_surf = ui_font.render(mode_text, True, (0, 0, 0))
                screen.blit(text_surf, (BTN_MODE_RECT.x + 80, BTN_MODE_RECT.y + 10))
                
                # 로그 창
                pygame.draw.rect(screen, (0, 0, 0), LOG_RECT)
                pygame.draw.rect(screen, (100, 100, 100), LOG_RECT, 1)
                for i, msg in enumerate(game_logs):
                    log_surf = ui_font.render(msg, True, (0, 255, 0))
                    screen.blit(log_surf, (LOG_RECT.x + 10, LOG_RECT.y + 10 + (i * 20)))
                
                # [UI 분기]
                if ui_mode == "LAND":
                    # 땅 구매 버튼
                    btn_color = (100, 100, 100)
                    if selected_tile:
                        sx, sy = selected_tile
                        if world_map[sy][sx] == TILE_GROUND:
                            if nation_money.get(TILE_PLAYER, 0) >= cost:
                                btn_color = (0, 150, 50)
                            else:
                                btn_color = (150, 50, 50)
                    
                    pygame.draw.rect(screen, btn_color, BTN_BUY_RECT)
                    pygame.draw.rect(screen, (200, 200, 200), BTN_BUY_RECT, 2)
                    btn_text = ui_font.render(f"BUY LAND ('{cost}G)", True, (255, 255, 255))
                    text_rect = btn_text.get_rect(center=BTN_BUY_RECT.center)
                    screen.blit(btn_text, text_rect)

                    # 유닛 생산 버튼들
                    for btn_rect, u_type in unit_buttons:
                        spec = UNIT_SPECS[u_type]
                        is_active = False
                        if selected_tile:
                            sx, sy = selected_tile
                            if world_map[sy][sx] == TILE_PLAYER:
                                if nation_money.get(TILE_PLAYER, 0) >= spec['cost']:
                                    is_active = True
                        
                        c_bg = (50, 100, 150) if is_active else (60, 60, 60)
                        pygame.draw.rect(screen, c_bg, btn_rect)
                        pygame.draw.rect(screen, (100, 200, 255) if is_active else (100,100,100), btn_rect, 2)
                        
                        name_surf = ui_font.render(spec['name'], True, (255, 255, 255))
                        cost_surf = ui_font.render(f"{spec['cost']}G", True, (255, 215, 0))
                        screen.blit(name_surf, (btn_rect.x + 5, btn_rect.y + 3))
                        screen.blit(cost_surf, (btn_rect.x + 5, btn_rect.y + 20))

                elif ui_mode == "UNIT":
                    for rect, label in ctrl_buttons:
                        pygame.draw.rect(screen, (60, 60, 100), rect)
                        pygame.draw.rect(screen, (150, 150, 255), rect, 2)
                        lbl_surf = ui_font.render(label, True, (255, 255, 255))
                        screen.blit(lbl_surf, (rect.x + 120, rect.y + 10))
                    
                    if selected_unit:
                        info_txt = f"Unit: {UNIT_SPECS[selected_unit['type']]['name']}"
                        info_surf = ui_font.render(info_txt, True, (255, 255, 0))
                        screen.blit(info_surf, (1280 - UI_WIDTH + 10, 600))

                # 범례 및 자원
                legend_list = [("Player", COLOR_PLAYER, TILE_PLAYER)]
                for i in range(len(ENEMY_COLORS)):
                    enemy_id = TILE_ENEMY_START + i
                    legend_list.append((f"Enemy {i+1}", ENEMY_COLORS[i], enemy_id))
                
                bottom_margin = 30
                item_height = 35
                start_y = 720 - bottom_margin - (len(legend_list) * item_height)
                start_x = 1280 - UI_WIDTH + 30
                
                for i, (name, color, nid) in enumerate(legend_list):
                    current_y = start_y + (i * item_height)
                    color_box = pygame.Rect(start_x, current_y, 20, 20)
                    pygame.draw.rect(screen, color, color_box)
                    pygame.draw.rect(screen, (255, 255, 255), color_box, 1)
                    name_surf = ui_font.render(name, True, (255, 255, 255))
                    screen.blit(name_surf, (start_x + 30, current_y - 2))
                    
                    if nid == TILE_PLAYER:
                        current_money = nation_money.get(nid, 0)
                        money_text = f"{current_money} G"
                        money_surf = ui_font.render(money_text, True, (255, 215, 0))
                        screen.blit(money_surf, (start_x + 130, current_y - 2))
                    else:
                        unknown_surf = ui_font.render("??? G", True, (150, 150, 150))
                        screen.blit(unknown_surf, (start_x + 130, current_y - 2))

            pygame.display.flip()

        pygame.quit()
        sys.exit()