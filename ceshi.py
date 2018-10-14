''''计算输出百位、个位和十位数'''''

x=input("输入一个三位数:")
baiwei=int(x)//100
shiwei=(int(x)-baiwei*100)//10
gewei=int(x)-baiwei*100-shiwei*10
print ("baiwei=",baiwei)
print ("shiwei=",shiwei)
print ("gewei=",gewei)
