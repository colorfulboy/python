import itchat
from pandas import DataFrame
itchat.login()
friends=itchat.get_friends(update=True)[0:]
male=flmale=other=0
for i in friends[1:]:
    sex=i['Sex']
    if  sex==1:
         male+=1
    elif sex==2:
        flmale+=1
    else:
         other+=1
    total=len(friends[1:])
print('男性好友：%.2f%%'%(float(male)/total*100)+'\n'+
      '女性好友: %.2f%%'%(float(flmale)/total*100)+'\n'+
      '性别不明: %.2f%%'%(float(other)/total*100))
def get_data(var):
    variable=[]
    for i in friends:
        value=i[var]
        variable.append(value)
    return variable
nickname=get_data('NickName')
province=get_data('Province')
city=get_data('City')
signature=get_data('Signature')
data={
    'nickname':nickname,
    'province':province,
    'city':city,
    'signature':signature
}
frame=DataFrame(data)
frame.to_csv('data.csv',index=True)