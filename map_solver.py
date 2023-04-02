import time

def binarySearch(target):
    f = open("cmap.txt", "r")
    datas = f.readlines()
    f.close()
    max_index = len(datas)-1
    min_index = 0
    mid_index = (max_index+min_index)//2
    while True:
        tmp_string = datas[mid_index][0:54]
        if tmp_string == target:
            return datas[mid_index][55]
        elif tmp_string < target:
            min_index = mid_index +1
            mid_index = (max_index+min_index)//2
        elif tmp_string > target:
            max_index = mid_index 
            mid_index = (max_index+min_index)//2
        if max_index == min_index:
            return False
        


if __name__ == "__main__":
    start_time = time.perf_counter()
    print(binarySearch("334300011554114001122122225035035322142140043554453453"))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")
