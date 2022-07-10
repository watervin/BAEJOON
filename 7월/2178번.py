from collections import deque

N, M = map(int, input().split())

road = []

for _ in range(N):
  road.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  rx = [-1, 1, 0, 0] 
  ry = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + rx[i]
      ny = y + ry[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if road[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if road[nx][ny] == 1:
        road[nx][ny] = road[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return road[N-1][M-1]

print(bfs(0, 0))