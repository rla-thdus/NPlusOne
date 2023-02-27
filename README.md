# N+1
외래키를 사용해서 데이터를 가져올 때 발생하는 현상이다. N+1이라고 해서 N개의 쿼리를 사용해야 하는데 1개가 더 보내지는 문제인지 알았는데, 알아보니 1개의 쿼리를 사용해서 가져올 수 있는 걸 N번 더 날려서 발생하는 것이였다.

### ERD
![](img/db-erd.png)

## N+1 발생 조건
### 1️⃣ 1:1 관계 테이블의 데이터 가져올 때
```python
for webtoon in WebToon.objects.all():
	print(webtoon.writer.name)
```
![](img/one-to-one.png)
### 2️⃣ 1:N 관계 중 N의 데이터 가져올 때
```python
for webtoon in WebToon.objects.all():
    print(webtoon.upload_date.day)
```
![](img/one-to-many.png)

### 3️⃣ 1:N 관계 중 1의 데이터 가져올 때
```python
for upload_day in UploadDay.objects.all():
    print([day.title for day in upload_day.webtoon_set.all()])
```
![](img/many-to-one.png)

### 4️⃣ N:M 관계 테이블의 데이터 가져올 때
```python
for webtoon in WebToon.objects.all():
    print(webtoon.title, [tag.name for tag in webtoon.tag.all()])
```
![](img/many-to-many.png)

## N+1 해결
Django ORM의 Eager Loading 방식인 `select_related()` 와 `prefetch_related()` 를 사용해서 해결할 수 있다.

### 1️⃣ `select_related()` 사용
#### 1:1 관계 테이블 가져오기
```python
for webtoon in WebToon.objects.all().select_related('writer'):
    print(webtoon.writer.name)
```
![](img/onetoonesolve.png)

#### 1:N 관계 중 N 가져오기
```python
for webtoon in WebToon.objects.all().select_related('upload_date'):
    print(webtoon.upload_date.day)
```
![](img/one-to-many-solve.png)

### 2️⃣ `prefetch_related()` 사용
#### 1:N 관계 중 1 가져오기
```python
for upload_day in UploadDay.objects.all().prefetch_related('webtoon_set'):
    print([day.title for day in upload_day.webtoon_set.all()])
```
![](img/many-to-one-solve.png)

#### N:M 관계 테이블 가져오기
```python
for webtoon in WebToon.objects.all().prefetch_related('tag'):
    print(webtoon.title, [tag.name for tag in webtoon.tag.all()])
```
![](img/many-to-many-solve.png)

