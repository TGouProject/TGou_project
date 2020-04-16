# `TGou商城`

##### **简介** :

​	 	 基于 `pyhton3.x` 和 `Django3.x`的购物网站

**使用说明:**

目录结构

- ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/ZUXCJANDCZJwMw9eDcmXBTEyGkjQTxc.Bgd0oxcg9qQeEW1rWoANQfS3OU88yJOdJUekQnFke0.oZYVgsKDbxA!!/b&bo=RgF2AQAAAAADBxI!&rf=viewer_4)

1. 同步环境:

  `pip install -r requirement.txt`

2. 项目层更改`settings.py`中的数据库配置.

3. 数据库迁移: `python manage.py makemigrations`

  `python manage.py migrate`

4. 创建超级用户:

  `python manage.py createsuperuser`

5. 运行项目:

  `python manage.py runserver`

  



#### 功能 : 

1. 登录注册 : 用户的登录与注册
2. 商品浏览 : 商品的图片 售价 种类 简介以及销量
3. 商品查询 : 支持对商品的模糊查询
4. 用户中心 : 支持用户个人信息 , 添加,更改收货地址等信息 , 商品加入购物车 ,订单生成
5. 商品下单 :暂时跳转下单成功页面
6. 后台管理 : 支持后台管理功能 , 商品及用户信息的增加 ,更新与删除 



### 界面展示 :

- 首页

  ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXSsX95.9TXX3C*wJHZ.4Xn0ABLnqXsl8MHiwen8Hr14DMRGuNspKPIV6bbIMPTfmrh53I3zXNfXVGDG.fakk*NY!/b&bo=AweOAwAAAAADR.s!&rf=viewer_4)

  ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXQeLsooWxldc9iQge35h.8f6tvlY7e.*YcQtD68IoTOIUC9AH6jdSa29HDO9wk1MfgD7E*K6ElLbqrrIVx*xRPg!/b&bo=9AanAwAAAAADRzQ!&rf=viewer_4)

  

- 登录/注册
  
  - ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXbLNr*IdY0coxdhmaoChbD4hFGYadKenWJ*J5ViJzDlfV2kpfzEh3z4FD5xuFSNYvrYySF.xmnwMhETVTq2Bl44!/b&bo=fge*AwAAAAADR6c!&rf=viewer_4)
  - ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXZkdn4tEOaAMTsqmn2zDIGD6KxIVqWQRcdBDzuorwt8*kCxFiusnMU8RIJNzDOiW9EsgTfSpmjhoYgzd7Tt5ovg!/b&bo=eweHAwAAAAADR5o!&rf=viewer_4)
  - ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXYqFRd4eDehhX7WQfeBKsHXMVgMl5NsUoBnqGexmThTYm*zhp3Nn3xkNMjl6oyNRD7sKtr0E.M7DogIunWBqCXI!/b&bo=JgcKAwAAAAADFxo!&rf=viewer_4)
  
- 商品详情
  
  - ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXZCWYY0GacaTZPRn1DNJ*BFEbWGbI6pdkRdEHd9Gvn36zpYeb0wmH.cprRPTB5xbu2T3Kp6KxAtya*Wjfi6vPdE!/b&bo=gAfvAgAAAAADRwg!&rf=viewer_4)
  
- 购物车
  
  - ![](http://m.qpic.cn/psc?/V13p1bPR03JQ85/wSJ2S*tZT7v.5zxXfWcfXYYWh1zLZalL0AWMbAsClt1.A5Dk7dJhC4J9MqP45f9EQ6qV5x*bZjSwwOgEpINrrhFfbhsg.rBLzbkNsYbKHQI!/b&bo=fgfrAgAAAAADZ9I!&rf=viewer_4)

