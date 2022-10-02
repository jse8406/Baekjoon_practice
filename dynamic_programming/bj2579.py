stair_num = int(input())
stair_list = []
stair_cost_subtotal = []
for i in range(stair_num):
  stair = int(input())
  stair_list.append(stair)
if stair_num == 1:
  stair_cost_subtotal.append(stair_list[0])
elif stair_num == 2:
  stair_cost_subtotal.append(stair_list[0])
  stair_cost_subtotal.append(stair_list[1] + stair_list[0])
elif stair_num == 3:
  stair_cost_subtotal.append(stair_list[0])
  stair_cost_subtotal.append(stair_list[1] + stair_list[0])
  bigger = max(stair_list[0] + stair_list[2], stair_list[1] + stair_list[2]) # 3번째 계단을 갈 수 있는 경우의 수
  stair_cost_subtotal.append(bigger)
else:
  stair_cost_subtotal.append(stair_list[0])
  stair_cost_subtotal.append(stair_list[1] + stair_list[0])
  bigger = max(stair_list[0] + stair_list[2], stair_list[1] + stair_list[2]) # 3번째 계단을 갈 수 있는 경우의 수
  stair_cost_subtotal.append(bigger)
  for i in range(3, stair_num):
    bigger = max(stair_list[i] + stair_list[i-1] + stair_cost_subtotal[i-3], stair_list[i] + stair_cost_subtotal[i-2]) 
    #두 계단 오르고 한 계단 오르기, 두 계단 올라오기, 
    stair_cost_subtotal.append(bigger)
print(stair_cost_subtotal[stair_num-1])