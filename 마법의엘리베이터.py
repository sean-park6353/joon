arr = []
def solution(storey):
    idx = 0
    while True:
        target = int(str(storey)[-1-idx])
        
        if target >= 6 :
            add_value = (10-target)
            storey = storey + add_value * (10**idx)
            arr.append(add_value)
            
        elif target == 5:
            try:
                if int(str(storey)[-2-idx]) >= 5:
                    add_value = (10-target)
                    storey = storey + add_value * (10**idx)
                    arr.append(add_value)
                else:
                    storey = storey - (target * (10**idx))
                    arr.append(target)
            except Exception as e:
                arr.append(int(str(storey)[-1-idx]))
                break
        else:
            storey = storey - (target * (10**idx))
            arr.append(target)
        if storey == 0:
            break
        idx += 1
    return sum(arr)



solution(49)