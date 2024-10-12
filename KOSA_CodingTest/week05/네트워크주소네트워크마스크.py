# 네트워크 마스크는 앞의 32-m 자리가 1로 채워져 있고, 뒤의 m자리는 0으로 채워지게 된다. 이와 같은 IP 네트워크에는 앞의 32-m 자리가 네트워크 주소와 일치하는 모든 IP들이 포함되게 된다.

# 결국 이게 핵심이네, 앞의 32-m자리가 일치한다고 하는데 그 일치하는 녀석이 네트워크 주소

# m은 최소값이어야됨. 그러니까 네트워크 주소만 구하고 맨오른쪽 0처리해버리면 네트워크 마스크

# 194.85.160.177
# a = 194*2^24 + 85*2^16 + 160*2^8 + 177
# a = 160*2^8 + 177
# a = 160*256 + 177
# a = 85*65,536 + 160*256 + 177
# print(a)

# net address = 194.85.160.183
# 핵심 : 넷어드레스 2진수 -> 넷마스크 바꾼다/
# c = 194.85.160.178

# address = [[0], [0], [0], [0], [0]]
# address[1].append(194)
# address[2].append(85)
# address[3].append(160)
# address[4].append(177)
# print(address)

# a, b, c, d = map(int, input().split('.'))
# print(a)
# print(b)
# print(c)
# print(d)

address = [[0], [0], [0], [0], [0]]
netaddress = [-1, 255, 255, 255, 255]

n = int(input())
for _ in range(n):
	a, b, c, d = map(int, input().split('.'))
	address[1].append(a)
	address[2].append(b)
	address[3].append(c)
	address[4].append(d)
	# print(address)
	netaddress[1] = netaddress[1] & a
	netaddress[2] = netaddress[2] & b
	netaddress[3] = netaddress[3] & c
	netaddress[4] = netaddress[4] & d

print(netaddress)

isEnd = False
pose = 4
res = 0
# while not isEnd:
#     if netaddress[pose] > 0:
#         temp = netaddress[pose]
#         print(temp)
#         #왼쪽 시프트를 하는데 0이되는 순간이 오른쪽이 전부 0이었겠구나 아
# -> 결과는 에러. 그리고 가정도 이상하긴했네
#         for i in range(8):
#             temp <<= temp
#             if temp == 0:
#                 res = i
#     else:
#         pose -= 1

#     if pose == 0:
#         break
operlist = [128, 64, 32, 16, 8, 4, 2, 1]
restemplist = [0, 0, 0, 0, 0, 0, 0, 0]
# while not isEnd:
#     if netaddress[pose] > 0:
#         temp = netaddress[pose]
#         restemplist[0] = int(temp / operlist[0])
#         temp -= operlist[0]
#         restemplist[1] = int(temp / operlist[1])
#         temp -= operlist[1]
#         restemplist[2] = int(temp / operlist[2])
#         temp -= operlist[2]
#         restemplist[3] = int(temp / operlist[3])
#         temp -= operlist[3]
#         restemplist[4] = int(temp / operlist[4])
#         temp -= operlist[4]
#         restemplist[5] = int(temp / operlist[5])
#         temp -= operlist[5]
#         restemplist[6] = int(temp / operlist[6])
#         temp -= operlist[6]
#         restemplist[7] = int(temp / operlist[7])
#         temp -= operlist[7]

#         # 비트 자리수 단위로 나눠서 배열에 저장한다음에 맨오른쪽부터 순회하며 1을 찾기?
#         for i in range(8):
#             if restemplist[7 - i] == 1:
#                 res = i
#         break
#     else:
#         pose -= 1

#     if pose == 0:
#         break

#
while not isEnd:
	if netaddress[pose] > 0:
		temp = netaddress[pose]

		# 각 operlist 값으로 나누고, 몫이 1 이상이면 빼는 방식
		for i in range(8):
			if temp >= operlist[i]:  # 나눠서 몫이 1 이상일 경우
				restemplist[i] = 1  # 해당 자리를 1로 설정
				temp -= operlist[i]  # 그 값을 temp에서 빼기
			else:
				restemplist[i] = 0  # 몫이 1 미만이면 그냥 0

		for i in range(8):
			if restemplist[7 - i] == 1:
				res = i
				break
		break
	else:
		pose -= 1  # pose 값을 줄여가며 다른 바이트로 넘어감

	if pose == 0:  # pose가 0이면 종료
		isEnd = True

print(pose)
print(res)
print(netaddress)
print(operlist)
print(restemplist)
