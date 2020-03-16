중요한 것: 데이터 저장 시 CSV파일이든 TXT파일이든 메모장으로 저장 형식을 utf-8로 바꾸어주어야 한다.



## TXT파일

```
USE db2;
LOAD DATA local infile "C:/Users/paik/Downloads/data1.txt" 
INTO TABLE addr
CHARACTER SET 'utf8'
FIELDS TERMINATED BY '|' ENCLOSED BY "" LINES TERMINATED BY '\n';
```

주소가 경기도인 것만 새로운 테이블에 옮기기

```
USE db2;
INSERT addr
SELECT * FROM addr_t WHERE 시도명 = '경기도';
```

필드 삭제

```
USE db2;
ALTER TABLE addr DROP 변경이력정보;
ALTER TABLE addr DROP 변경사유;
ALTER TABLE addr DROP 고시일자;
```



## CSV파일

```
LOAD DATA LOCAL INFILE 'C:/Users/paik/Downloads/download/meddata2.csv'
INTO TABLE `db2`.`medical_t`
COLUMNS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
```

옮기기

```
USE db2;
INSERT medical
SELECT * FROM medical_t WHERE 시도 = '경기';
```

