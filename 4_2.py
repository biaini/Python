#Student: Avakian Andranik

gt_list = [45, 48, 12, 22, 10, 17, 15, 8, 32] 
greater_than = [gt_list[num] for num in range(1, len(gt_list)) if gt_list[num] > gt_list[num-1]]
print (greater_than)
