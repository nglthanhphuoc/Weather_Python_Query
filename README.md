
# Truy vấn dữ liệu bằng Python

Trong dự án này tôi sẽ dùng Spyder 5 với ngôn ngữ Python để truy vấn và phân tích dữ liệu thời tiết.


## Import lib và dữ liệu lên spyder


```bash
import pandas as pd

data = pd.read_csv(r"C:\Users\Welcome\Downloads\1. Weather Data.csv")
```
## Khám phá dữ liệu

Xem tổng quan dữ liệu thời tiết

```bash
print(data.head(5))
print(data.index)
print(data.columns)
print(data.dtypes)
print(data['Rel Hum_%'].unique())
print(data.nunique)
print(data['Weather'].count())
print(data['Weather'].value_counts())
print(data.info())

```
Tìm giá trị Unique về tốc độ gió

```bash
TypeOfWindSpeed = data['Wind Speed_km/h'].nunique()
print('Types Of Wind Speed' +' are ' + str( TypeOfWindSpeed ))
WindSpeed = data['Wind Speed_km/h'].unique()
print('Wind Speed' +' are ' + str( WindSpeed ))
```
Tính số lần khi thời tiết báo hiệu trong lành 
```bash
print(data.Weather.value_counts())
Clear_weather = data[data.Weather == 'Clear']
Clear_weather2 = data.groupby('Weather').get_group('Clear')  
```
Số lần khi thời tiết ở tốc độ gió là 4km/h
```bash
FourKmPerHour = data.groupby('Wind Speed_km/h').get_group(4)
``
Tìm tất cả giá trị Null trong bảng
```bash
NullData = data.sum().isnull()
```
Đặt lại tên cột thời tiết thành Điều kiện thời tiết
```bash
data.rename(columns = {'Weather' : 'Weather Condition', 'Temp_C': 'Temp'})
```
Tìm giá trị trung bình của độ trong lành
```bash
data.Visibility_km.mean()
```
Tìm độ lệch chuẩn của áp lực khí    
```bash
data.Press_kPa.std()
```
Độ lệch chuẩn của độ ẩm tương quan
```bash
data['Rel Hum_%'].var()
```
Tìm tất cả các trường hợp khi trời tuyết
```bash
data.groupby(['Weather Condition']).get_group('Snow')

""" hoặc có thể làm theo cách 2
data[data['Weather Condition'] == 'Snow']
```
Tìm tất cả các trường hợp khi thời tuyết liên quan đến tuyết
```bash
data[data['Weather Condition'].str.contains('Snow')]
```
Tìm tất cả trường hợp khi tốc độ gió trên 24 và độ nhìn xa hơn 25 km
```bash
data[(data['Wind Speed_km/h']) > 24 & (data['Visibility_km'] == 25)]
```
## 🛠 Skills
Python, Spyder

