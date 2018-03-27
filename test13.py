# 处理文件中数据
f=open('scores.txt')
lines=f.readlines()
f.close()

results=[]

for line in lines:
    data=line.split()
    # print(data)

    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s \t: %d\n' % (data[0], sum)
    # print result

    results.append(result)

output=open('result.txt','w')
output.writelines(results)
output.close()



