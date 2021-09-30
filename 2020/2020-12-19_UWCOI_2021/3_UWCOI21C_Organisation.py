# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     colors = list(map(int, input().split()))
#     print("colors : now", colors)
#     ducks_inside_box = {}
#     box_has_colors = {}
#     color_in_these_boxes = {}
#     for i in range(N):
#         ducks_inside_box[i] = []
#         box_has_colors[i] = []
#         color_in_these_boxes = {}
#     for j in range(N + 1):
#         color_in_these_boxes[j] = []
#     i_box = 0
#     j_color = 0
#     turn_back = False
#     while True:
#         if turn_back:
#             j_color -= 1
#             turn_back = False
#             print("turn back")
#         else:
#             if colors[j_color] >= K:
#                 if colors[j_color] == 0:
#                     j_color += 1
#                 else:
#                     if i_box in color_in_these_boxes[j_color]:
#                         j_color += 1
#                         turn_back = True
#                         ducks_of_this_color = colors[j_color]
#                     if len(ducks_inside_box[i_box]) < 1 or ducks_inside_box[i_box][0] <= 1:
#                         insertable = K - 1
#                     else:
#                         insertable = K - ducks_inside_box[i_box][0]
#                     colors[j_color] -= insertable
#                     ducks_inside_box[i_box].append(insertable)
#                     box_has_colors[i_box].append(j_color)
#                     color_in_these_boxes[j_color].append(i_box)
#             else:
#                 if colors[j_color] == 0:
#                     j_color += 1
#                 else:
#                     if i_box in color_in_these_boxes[j_color]:
#                         j_color += 1
#                         turn_back = True
#                         ducks_of_this_color = colors[j_color]
#                     if len(ducks_inside_box[i_box]) < 1 or ducks_inside_box[i_box][0] <= 1:
#                         insertable = ducks_of_this_color
#                     else:
#                         insertable = min(K - ducks_inside_box[i_box][0], ducks_of_this_color)
#                     colors[j_color] -= insertable
#                     ducks_inside_box[i_box].append(insertable)
#                     box_has_colors[i_box].append(j_color)
#                     color_in_these_boxes[j_color].append(i_box)
#             if len(ducks_inside_box[i_box]) == 2:
#                 i_box += 1
#             print("ducks in box", ducks_inside_box)
#             print("box has colo", box_has_colors)
#             print("color in box", color_in_these_boxes)
#             print("colors : now", colors)
#             print()
#         if j_color == N + 1:
#             break
#     for i in range(N):
#         c1 = box_has_colors[i][0]
#         m1 = ducks_inside_box[i][0]
#         if len(box_has_colors[i]) == 2:
#             c2 = box_has_colors[i][1]
#             m2 = ducks_inside_box[i][1]
#             print(c1, m1, c2, m2)
#         else:
#             print(c1, m1)