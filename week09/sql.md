践习题3-10  

3. 新建一张user表，插入几条数据，属性包含：唯一标识（id），姓名（name）,性别（sex），年龄（age），联系方式（phone）。
   ```sql
      CREATE TABLE user(
       id INT PRIMARY KEY AUTO_INCREMNET,
       name VARCHAR(255) NOT NULL,
       age INT,
       gender VARCHAR(10),
       phone VARCHAR(20)
   );
   ```
4. 写出SQL语句，查询user表中所有年龄在20-30范围内的用户。
   ```sql
   SELECT * FROM user
   WHERE age>=20 AND age<=30;
   ```
5. 写出SQL语句，删除user表中名字包含“张”的用户。
   ```sql
   DELETE FROM user
   WHERE name LIKE "%张%"；
   ```
6. 写出SQL语句，计算user表中所有用户的平均年龄。
   ```sql
   SELECT AVG(age) AS average_age
   FROM user;
   ```
7. 写出SQL语句，查询user表中年龄在20-30范围内，名字包含“张”的用户，并按照年龄从大到小排序输出。
   ```sql
   SELECT * FROM user
   WHERE name LIKE "%张%" AND age BETWEEN 20 AND 30
   ```
8. 新建两张表，team表（id,teamName）,score表(id,teamid,userid,score)。其中，score表中的teamid为指向team表id的外键，userid为指向user表id的外键。
   ```sql
   CREATE TABLE team(
     id INT PRIMARY KEY AUTO_INCRMENT,
     teamName VARCHAR(255) NOT NULL
   );
   CREATE TABLE score(
     id INT PRIMARY KEY AUTO_INCREMENT,
     teamid INT,
     userid INT,
     score INT,
     FOREIGN KEY (teamid) REFERENCES team(id),
     FOREIGN KEY (userid) REFERENCES user(id) 
   );
   ```
9.  写出SQL语句，查询teamName为“ECNU”的队伍中，年龄小于20的用户们。
  ```sql
  SELECT user.*
  FROM user
  JOIN score ON user.id = score.id
  JOIN team ON score.teamid = team.id
  WHERE team.teamName  =  'ECNU' AND user.age < 20
  ```
10. 写出SQL语句，计算teamName为“ECNU”的总分（假设score存在null值，null值默认为0加入计算）。
  ```sql
  SELECT team.teamName, COALESCE(SUM(score.score), 0) AS totalScore
  FROM team
  LEFT JOIN score ON team.id = score.teamid
  WHERE team.teamName = 'ECNU'
  GROUP BY team.teamName;
  ```
    
