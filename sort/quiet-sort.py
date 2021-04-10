import pandas

#导入数据
data = {'A':['1','9','8'],
        'B':['12','22','18'],
        'C':['16','19','4'],
        }
# data1={'D':['4','2','9'],
#         'E':['15','10','14'],
#         'F':['16','3','1'],
#         }


#创建DataFrame对象
data_frame=pandas.DataFrame(data)
# data_frame1=pandas.DataFrame(data1)

# 合并
# data_cont=pandas.concat([data_frame,data_frame1],sort=True)
data_cont=pandas.concat([data_frame],sort=True)
# if __name__ == '__main__':
#     print(data_cont)

#根据C降序排序
# df_sc=data_cont.sort_values(by='C',ascending=False)

#根据第0行进行升序排序
df_sc=data_cont.sort_values(by=0,axis=1,ascending=True)

#打印合并后的数据
if __name__ == '__main__':
    print(df_sc)