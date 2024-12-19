import pandas as pd

# Đọc dữ liệu từ file csv với index_col là cột đầu tiên
drink = pd.read_csv("drinks.csv", index_col=0)

# Yêu cầu 1: In thông tin cơ bản của dataframe drink
def print_info():
    print("Type:", type(drink))
    print("Shape:", drink.shape)
    print("Columns:", drink.columns.tolist())
    print("\n5 dòng đầu:")
    print(drink.head())
    print("\n5 dòng cuối:")
    print(drink.tail())

print_info()

# Yêu cầu 2: Số lượng bia tiêu thụ trung bình ở mỗi châu lục
beer_mean_by_continent = drink.groupby("continent")["beer_servings"].mean()
print("\nSố lượng bia tiêu thụ trung bình ở mỗi châu lục:")
print(beer_mean_by_continent)

# Yêu cầu 3: Thống kê tổng quát số lượng rượu vang tiêu thụ ở mỗi châu lục
wine_stats_by_continent = drink.groupby("continent")["wine_servings"].describe()
print("\nThông tin thống kê số lượng rượu vang tiêu thụ ở mỗi châu lục:")
print(wine_stats_by_continent)

# Yêu cầu 4: Số lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục
mean_beer_wine_by_continent = drink.groupby("continent")[["beer_servings", "wine_servings"]].mean()
print("\nSố lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
print(mean_beer_wine_by_continent)
# Yêu cầu 5: Giá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục
median_beer_wine_by_continent = drink.groupby("continent")[["beer_servings", "wine_servings"]].median()
print("\nGiá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục:")
print(median_beer_wine_by_continent)

# Yêu cầu 6: Thông tin về rượu mạnh tiêu thụ ở mỗi châu lục
spirit_stats_by_continent = drink.groupby("continent")["spirit_servings"].agg(["mean", "max", "min"])
print("\nSố lượng rượu mạnh tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục:")
print(spirit_stats_by_continent)

# Yêu cầu 7: Sắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ
drink_sorted_by_beer = drink.sort_values(by="beer_servings")
print("\nDữ liệu sắp xếp tăng dần theo số lượng bia tiêu thụ:")
print(drink_sorted_by_beer)

# 5 quốc gia có lượng tiêu thụ bia nhiều nhất
top_5_beer_countries = drink_sorted_by_beer.tail(5)
print("\n5 quốc gia có lượng tiêu thụ bia nhiều nhất:")
print(top_5_beer_countries)

# 5 quốc gia có lượng tiêu thụ bia ít nhất
bottom_5_beer_countries = drink_sorted_by_beer.head(5)
print("\n5 quốc gia có lượng tiêu thụ bia ít nhất:")
print(bottom_5_beer_countries)
