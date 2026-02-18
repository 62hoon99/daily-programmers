from collections import defaultdict
import heapq

def solution(jobs):
    disk_controller = []
    
    # key: 작업이 요청되는 시점, value: job
    job_dict = defaultdict(list)
    for i in range(len(jobs)):
        job = jobs[i]
        job_dict[job[0]].append((job[1], job[0], i))
    
    # 끝난 작업 개수
    count = 0
    # 현재 시각
    current_ms = 0
    # 현재 작업이 끝나는 시간
    current_job_end_ms = -1
    # 현재 작업 여부
    working = False
    # 현재 job
    current_job = None
    # 반환 시간 총합
    total_res_ms = 0
    
    while count < len(jobs):
        # heap 에 현재 시간에 시작 가능한 job 추가
        avail_jobs = job_dict[current_ms]
        if len(avail_jobs) > 0:
            for aj in avail_jobs:
                heapq.heappush(disk_controller, aj)

        # 현재 작업이 끝나는 시간인 경우
        if current_job_end_ms == current_ms:
            count += 1
            working = False
            total_res_ms += current_ms - current_job[1]
            current_job = None
        
        if not working and len(disk_controller) > 0:
            new_job = heapq.heappop(disk_controller)
            current_job_end_ms = current_ms + new_job[0]
            working = True
            current_job = new_job
        
        current_ms += 1
    
    return total_res_ms // count