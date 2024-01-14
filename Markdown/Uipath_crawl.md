####Uipath爬取房租数据详细步骤
具体流程如下：

#####第一阶段（爬取上海市各行政区链家租房网址）：
  &emsp;浏览器打开https://sh.lianjia.com/zufang/ →打开Uipath→点击“新建序列”→点击“数据抓取”→在弹出的“提取向导”里将光标依次点击“静安”“徐汇”→出现弹窗，编辑列名为“districts”，勾选URL，作为机器后续爬取数据的网址来源→点击“完成”→将右侧“活动”里的“写入CSV”拖拽到左侧执行框里→ “写入来源”设为ExtractDataTable,右侧属性编码设置为“utf-8”，选择要写入的文件data.csv。
 
#####第二阶段（引导机器自动爬取各区数据）：
  &emsp;新建序列→拖拽“Excel应用程序范围”，选择上一步得到的“data.csv”，将开始读取的位置设为“B2”（即静安区链家网址）。→创建变量“districts”（参照csdn教程创建）→拖拽“遍历循环”，将districts作为循环变量，类型设为“string”。

#####第三阶段（记录每次循环详细操作）：
  &emsp;拖拽“打开浏览器”，属性里浏览器类型改为“谷歌”，设置输入的URL为“item”→点击“数据抓取”，提取向导里依次点击房屋名称、价格、面积、朝向、房型、详细地址等→弹出的“指出下一条链接”里点击“是”，使机器爬取多页→删去第二次不必要的“打开浏览器”操作，将变量“ExtractDataTable”删去，创建新的变量“txt”。由于数据抓取后还需要重新打开浏览器进行下一个区域的数据抓取，所以这里我们进行关闭浏览器的操作，即“关闭选项卡”→拖拽“附加到CSV”到关闭选项卡后面，将前面遍历循环抓取到的数据全部读取到提前新建的csv表格—data-all 里。

&emsp;最后，点击“运行文件”，检查data-all文件，得到上面爬取到的数据。






#####过程截图：
> ![Alt text](../imgs/image.png)

> ![Alt text](../imgs/image-2.png)

> ![Alt text](../imgs/image-3.png)

> ![Alt text](../imgs/image-4.png)

> ![Alt text](../imgs/image-5.png)

> ![Alt text](../imgs/image-6.png)

> ![Alt text](../imgs/image-7.png)

> ![Alt text](../imgs/image-8.png)

> ![Alt text](../imgs/image-9.png)

> ![Alt text](../imgs/image-11.png)

> ![Alt text](../imgs/image-12.png)

> ![Alt text](../imgs/image-13.png)

> ![Alt text](../imgs/image-14.png)

> ![Alt text](../imgs/image-15.png)

> ![Alt text](../imgs/image-16.png)

> ![Alt text](../imgs/image-17.png)

> ![Alt text](../imgs/image-18.png)