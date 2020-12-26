# 미완성

def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0)) #+1의 이유 : 0부터 시작이니까
      lis = data[res[-1]+1:]
    except:
      break     
  return res

def solution(arrows):
    answer = 0
    current = (0, 0)
    points = [current]
    i = 0
    switch = False

    for arrow in arrows:
        # 이동
        prev = (current[0], current[1])
        if arrow == 0:
            current = (current[0], current[1]+1)
            
        elif arrow == 1:
            current = (current[0]+1, current[1]+1)

            tmp = (current[0]-1, current[1])
            if tmp in points:
                idxs = find_index(points, tmp)
                for idx in idxs:
                    if (tmp[0]+1, tmp[1]-1) == points[idx-1] or (tmp[0]+1, tmp[1]-1) == points[idx+1]:
                        answer += 1
                        switch = True
                        break

            if prev in points[:-1] and switch:
                idxs = find_index(points[:-1], prev)
                j = False
                for idx in idxs:
                    if current == points[idx-1] or current == points[idx+1]:
                        j = True
                        break

                if not j:
                    answer += 1
                else:
                    answer -= 1
            switch = False
            
        elif arrow == 2:
            current = (current[0]+1, current[1])
            
        elif arrow == 3:
            current = (current[0]+1, current[1]-1)
            
            tmp = (current[0], current[1]+1)
            if tmp in points:
                idxs = find_index(points, tmp)
                for idx in idxs:
                    if (tmp[0]-1, tmp[1]-1) == points[idx-1] or (tmp[0]-1, tmp[1]-1) == points[idx+1]:
                        answer += 1
                        switch = True
                        break

            if prev in points[:-1] and switch:
                idxs = find_index(points[:-1], prev)
                j = False
                for idx in idxs:
                    if current == points[idx-1] or current == points[idx+1]:
                        j = True
                        break

                if not j:
                    answer += 1
                else:
                    answer -= 1
            switch = False

        elif arrow == 4:
            current = (current[0], current[1]-1)
            
        elif arrow == 5:
            current = (current[0]-1, current[1]-1)
            
            tmp = (current[0]+1, current[1])
            if tmp in points:
                idxs = find_index(points, tmp)
                for idx in idxs:
                    if (tmp[0]-1, tmp[1]+1) == points[idx-1] or (tmp[0]-1, tmp[1]+1) == points[idx+1]:
                        answer += 1
                        switch = True
                        break
            
            if prev in points[:-1] and switch:
                idxs = find_index(points[:-1], prev)
                j = False
                for idx in idxs:
                    if current == points[idx-1] or current == points[idx+1]:
                        j = True
                        break

                if not j:
                    answer += 1
                else:
                    answer -= 1
            switch = False

        elif arrow == 6:
            current = (current[0]-1, current[1])
            
        elif arrow == 7:
            current = (current[0]-1, current[1]+1)
            
            tmp = (current[0], current[1]-1)
            if tmp in points:
                idxs = find_index(points, tmp)
                for idx in idxs:
                    if (tmp[0]+1, tmp[1]+1) == points[idx-1] or (tmp[0]+1, tmp[1]+1) == points[idx+1]:
                        answer += 1
                        switch = True
                        break

            if prev in points[:-1] and switch:
                idxs = find_index(points[:-1], prev)
                j = False
                for idx in idxs:
                    if current == points[idx-1] or current == points[idx+1]:
                        j = True
                        break

                if not j:
                    answer += 1
                else:
                    answer -= 1
            switch = False

        # points에 current가 이미 존재한다면 방의 개수 추가
        if current in points:
            # 이미 지나온 선이 아닐 때 추가

            if prev in points[:-1]:
                idxs = find_index(points[:-1], prev)
                j = False
                for idx in idxs:
                    if current == points[idx-1] or current == points[idx+1]:
                        j = True
                        break
                
                if not j:
                    answer += 1
                    
            elif current != points[-2]:
                answer += 1
        
        i += 1
        points.append(current)
        
    return answer


if __name__ == "__main__":
    print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))
