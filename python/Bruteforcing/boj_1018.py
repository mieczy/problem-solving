###체스판 다시 칠하기
def ps_1018():
    n, m = map(int, input().split())
    board = []
    case = []

    # 보드판 입력
    for y in range(n):
        board.append(input())

    # 보드판에서 (8x8)크기로 1칸씩 이동
    for board_y in range(n-7):
        for board_x in range(m-7):
            collect_color = board[board_y][board_x]    # 맨 왼쪽 위 칸의 색상
            count = 0
            # 체스판(8x8) 변화 횟수 
            for y in range(board_y, board_y+8):
                for x in range(board_x, board_x+8):
                    # 정답과 다른 경우 횟수 증가
                    if board[y][x] != collect_color:
                        count += 1
                    # 다음번 열 색상
                    collect_color = 'W' if collect_color=='B' else 'B'
                # 다음번 행 색상
                collect_color = 'W' if collect_color=='B' else 'B'
                
            # w로 시작하는 경우와 b로 시작하는 경우 중 더 작은 변화 횟수 추가
            case.append(min(count, 64-count))   
    
    print(min(case))
