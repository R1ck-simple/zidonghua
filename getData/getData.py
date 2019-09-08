def getData(str):
    cases = open('./testData/testCases.txt', encoding='utf-8')
    data = open('./testData/test0908.txt', encoding='utf-8')
    # 首先处理case
    ca_li = cases.readlines()
    for i in range(0, len(ca_li)):
        if str in ca_li[i]:
            for j in range(i+1, len(ca_li)):
                if '#' in ca_li[j]:
                    ca_data = ca_li[i+1:j]
                    break
            break
    # 然后处理data
    da_data_li = []
    da_li = data.readlines()
    for i in range(0, len(da_li)):
        if str in da_li[i]:
            for j in range(i + 1, len(da_li)):
                if '#' in da_li[j]:
                    da_data = da_li[i + 1:j]
                    da_data_li.append(da_data)
                    break
    # 整合用例
    str_ca_li = []
    for i in da_data_li:
        li = []
        for j, k in zip(ca_data, i):
            li.append(j.strip() + '*' + k.strip())
        str_ca_li.append(li)
    return str_ca_li
