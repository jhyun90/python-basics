
# NAVER_1

'''
record = [
    "RECEIVE abcd@naver.com",
    "RECEIVE zzkn@naver.com",
    "DELETE",
    "RECEIVE qwerty@naver.com",
    "SAVE",
    "RECEIVE QwerTY@naver.com"
]
'''

# record = [
#     "RECEIVE abcd@naver.com",
#     "RECEIVE zzkn@naver.com",
#     "DELETE",
#     "RECEIVE qwerty@naver.com",
#     "SAVE",
#     "SAVE",
#     "DELETE",
#     "RECEIVE QwerTY@naver.com",
#     "SAVE"
# ]
#
# # ["abcd@naver.com", "qwerty@naver.com", "QwerTY@naver.com"]
#
# tmp_stack = []
# result = []
#
# for i in range(len(record)):
#     record[i] = record[i].split()
#     print(record[i])
#
#     cmd = record[i][0]
#     # print(cmd)
#
#     if cmd == "RECEIVE":
#         tmp_stack.append(record[i][1])
#         print("tmp", tmp_stack)
#
#     # print("tmp", tmp_stack)
#
#     elif cmd == "DELETE":
#         if len(tmp_stack) != 0:
#             del tmp_stack[-1]
#
#         else:
#             continue
#
#     elif cmd == "SAVE":
#         result += tmp_stack
#         tmp_stack = []
#
# print("tmp", tmp_stack)
# print("final", result)




# NAVER_2

def solution(n):
    answer = 0
    begin = 1
    end = 10
    result = []
    # result.append(1)

    for i in range(begin, end):
        mul = i
        for j in range(i + 1, end + 1):
            # print(i, j)
            mul *= j
            result.append(mul)

        i += 1

    result = sorted(set(result))
    print(result)
    # print(len(result))

    if len(result) < 10**6 and max(result) < 10**12:
        print(result)
        answer = result[n - 1]

    return answer

n = 10
print(solution(n))






'''
answer = 0
meta_parser = re.compile('<meta(.+?)/>')
a_parser = re.compile('<a(.+?)>')
page_infos = []

for page in pages:
    page_dict = dict()
    a_tags = a_parser.findall(page)
    # print(a_tags)
    
    outer_url = []
    
    for a_tag in a_tags:
        first_idx = end_idx = -1
        
        for idx, char in enumerate(a_tag):
            if char == '"':
                if first_idx == -1:
                    first_idx = idx
                    # print(first_idx)
                    
                elif end_idx == -1:\
                    end_idx = idx
                    # print(end_idx)

        outer_url.append(a_tag[first_idx+1:end_idx])
        # print(outer_url)

    meta_tag = meta_parser.search(page).group()
    content_prop = meta_tag.split(' ')[2]
    first_idx = end_idx = -1

    for idx, char in enumerate(content_prop):
        if char == '"':
            if first_idx == -1:
                first_idx = idx

            elif end_idx == -1:
                end_idx = idx

    url = content_prop[first_idx+1: end_idx]
    page_dict['outer_url_list'] = outer_url
    page_dict['url'] = url
    page_dict['keyword_point'] = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
    page_dict['link_point'] = 0
    page_infos.append(page_dict)

for page_info in page_infos:
    for outer_url in page_info['outer_url_list']:
        for outer_url_page_candidate in page_infos:
            if outer_url == outer_url_page_candidate['url']:
                outer_url_page_candidate['link_point'] += page_info['keyword_point']/len(page_info['outer_url_list'])

point_lst = [page_info['keyword_point'] + page_info['link_point'] for page_info in page_infos]
print(point_lst)
print(point_lst.index(max(point_lst)))
'''
