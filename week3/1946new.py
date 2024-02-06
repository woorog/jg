import sys


def max_candidates(menlist):
    results = []
    for N, applicants in menlist:
        # 서류심사 성적으로 지원자 정렬
        applicants.sort()
        max_hire = 1  # 첫 번째 지원자는 항상 선발
        min_interview_rank = applicants[0][1]

        # 나머지 지원자에 대해 면접 성적 확인
        for i in range(1, N):
            if applicants[i][1] < min_interview_rank:
                max_hire += 1
                min_interview_rank = applicants[i][1]

        results.append(max_hire)
    return results

# 예제 입력
tc = int(sys.stdin.readline())
for _ in range(tc):
    mens=int(sys.stdin.readline())
    menlist=[]
    for _ in range(mens):
        menlist.append(list(map(int, sys.stdin.readline().split())))
    print(menlist)
    max_candidates(menlist)