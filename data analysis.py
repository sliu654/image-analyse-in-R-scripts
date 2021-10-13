import math
import numpy as np
from scipy import log
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import openpyxl
import xlrd

#import data
shu=xlrd.open_workbook(r'C:/Users/Shu/Desktop/Figure 1.xlsx')    
sheet3=shu.sheet_names()                   
sheet3=shu.sheet_by_name('Sheet3')               
rows=sheet3.nrows                           
cols=sheet3.ncols                             
#print(rows,cols)                           
data=[]                                     
for i in range(rows): 
 data.append(sheet3.row_values(i))     

x0_total =[]                            
for i in range(rows):
  x0_total.append(sheet3.cell_value(i,0))   
#print(colmun1_data)                         

x0=x0_total[1:]
xl=x0_total[0]


y0_total=[]                            
for i in range(rows):
  y0_total.append(sheet3.cell_value(i,1))   
#print(colmun1_data)  

y0=y0_total[1:]
yl=y0_total[0]

# 字体
plt.rcParams['font.sans-serif']=['SimHei']

# 拟合函数
def func(x, a, b, c):
    y = c*np.exp(-a*(x+b))
    return y

# 拟合的坐标点
    
#x0 = [0,0.33,]  
#y0 = [2,4,10,11,13,15,16,18]

plt.scatter(x0,y0,s=30,marker='o')
plt.scatter(xl,yl,s=30,marker='o')

# 拟合，可选择不同的method
result = curve_fit(func, x0, y0,method='trf')
a, b, c = result[0]  


x1 = np.arange(0, 30, 0.1)  
y1 = c*np.exp(-a*(x1+b))
   
plt.plot(x1, y1, "blue")  
 
x0 = np.array(x0)
y0 = np.array(y0)

y2 = c*np.exp(-a*(x0+b))
r2 = r2_score(y0, y2)  

print(a)
print(b)  
print(c)
print(r2)

m = round(max(y0)/10,1)
#print(m)
plt.text(60, m, 'y='+str(round(c,2)) +'exp(-'+str(round(a,2))+'*(x+'+str(round(b,2))+'))', ha='right',fontsize=20)  
#plt.text(20, m, r'$R^2=$'+str(round(r2,3)), ha='top', va='right',fontsize=20) 
plt.text(48, m, r'$R^2=$'+str(round(r2,3)), ha='right', va='top',fontsize=20)  

# True 显示网格  
# linestyle 设置线显示的类型(一共四种)  
# color 设置网格的颜色  
# linewidth 设置网格的宽度   
plt.grid(True, linestyle = "--", color = "g", linewidth = "0.5")
plt.show()