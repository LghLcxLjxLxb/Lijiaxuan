### Windows 10安装H2O（亲测可用）

&emsp;H2O的安装分为两个部分：
>1.	安装JAVA
>2.	解压H2O和运行h2o.jar文件


##### 一、	下载JDK和H2O的安装包

##### 二、	安装JDK（已经安装好JDK的请直接跳到第三步）
1.	双击下载的 ![Alt text](../imgs/image-53.png)文件

2.	出现欢迎使用Java SE开发工具包8 Update 212的安装向导界面，点击“下一步”（图片的版本是Update 60，仅供参考）
 
> ![Alt text](../imgs/image-54.png)

3.	出现选择安装可选功能界面，默认安装，安装到C:\Program Files\Java\jdk1.8.0_212。点击“下一步”
> ![Alt text](../imgs/image-40.png)

4.	出现进度情况显示界面，点击下一步，进行安装，耐心等待，需要几分钟
> ![Alt text](../imgs/image-41.png)
 

5.	目标文件夹安装选择界面，更改到C:\Program Files\Java\jre1.8.0_XXX，点击“下一步“
> ![Alt text](../imgs/image-42.png)

6.	安装状态显示界面，大概等半分钟
> ![Alt text](../imgs/image-43.png)

7.	已成功安装界面，点击关闭。
> ![Alt text](../imgs/image-44.png)

##### 验证环境：
&emsp;1.	点击左下角的搜索图标，输入cmd，回车弹出命令行窗口。
> ![Alt text](../imgs/image-45.png)

&emsp;2.	输入“java -version“，出现以下信息，说明安装成功
> ![Alt text](../imgs/image-46.png)
 
##### 三、	安装H2O
H2O不需要安装，解压后即可运行。
1.	解压下载的h2o-3.34.0.3.zip文件
> ![Alt text](../imgs/image-47.png)

2.	进入解压的目录，可以看到有一个h2o.jar文件
> ![Alt text](../imgs/image-48.png)

3.	进入命令提示符界面
 
> ![Alt text](../imgs/image-49.png)

4.	输入java -jar ，然后把h2o.jar从文件夹拖到命令行，最后形成下图所示的命令
> ![Alt text](../imgs/image-50.png)

5.	按下Enter键，运行h2o，仔细找屏幕上的提示
> ![Alt text](../imgs/image-51.png)

6.	把Open H2O Flow in your web browser: http://192.168.1.102:54323 后面的部分输入到浏览器的地址栏，或者直接在地址栏输入http://localhost:54323 就可以使用H2O了。
> ![Alt text](../imgs/image-52.png)

