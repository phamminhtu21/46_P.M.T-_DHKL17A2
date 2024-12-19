import pandas as pd

# Tải dữ liệu từ file csv
data = pd.read_csv("euro12.csv")

# In thông tin cơ bản của dataframe
def print_info():
    print("Type:", type(data))
    print("Shape:", data.shape)
    print("Columns:", data.columns.tolist())

# Yêu cầu 1: In giá trị cột Goals
print("\nCột Goals:")
print(data["Goals"])

# Yêu cầu 2: Có bao nhiêu đội tham gia Euro2012?
num_teams = data["Team"].nunique()
print(f"\nSố đội tham gia Euro 2012: {num_teams}")

# Yêu cầu 3: In thông tin của Euro2012
print("\nThông tin của Euro2012:")
data.info()

# Yêu cầu 4: Tạo dataframe mới với 3 cột Team, Yellow Cards, Red Cards
discipline = data[["Team", "Yellow Cards", "Red Cards"]]
print("\nDataframe discipline:")
print(discipline)

# Yêu cầu 5: Sắp xếp discipline giảm dần theo 2 cột 'Red Cards', 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=["Red Cards", "Yellow Cards"], ascending=False)
print("\nDiscipline sau khi sắp xếp:")
print(discipline_sorted)
# Yêu cầu 6a: Tính trung bình Yellow Cards
mean_yellow_cards = discipline["Yellow Cards"].mean()
print(f"\nTrung bình số Yellow Cards: {mean_yellow_cards}")

# Yêu cầu 6b: Lọc các đội đã ghi hơn 6 bàn thắng
teams_with_more_than_6_goals = data[data["Goals"] > 6]
print("\nCác đội ghi hơn 6 bàn thắng:")
print(teams_with_more_than_6_goals[["Team", "Goals"]])

# Yêu cầu 7: In các đội mà tên bắt đầu bằng 'G'
teams_start_with_g = data[data["Team"].str.startswith("G")]
print("\nCác đội có tên bắt đầu bằng 'G':")
print(teams_start_with_g["Team"])

# Yêu cầu 8: In 7 cột đầu của Euro 2012
print("\n7 cột đầu:")
print(data.iloc[:, :7])

# Yêu cầu 9: In tất cả các cột, trừ 3 cột cuối
print("\nTất cả các cột, trừ 3 cột cuối:")
print(data.iloc[:, :-3])

# Yêu cầu 10: In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
print("\nCác cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards:")
print(data[["Team", "Goals", "Shooting Accuracy", "Yellow Cards", "Red Cards"]])

# Yêu cầu 11: In các cột Team và Shooting Accuracy từ England, Italy, Russia
specific_teams = data[data["Team"].isin(["England", "Italy", "Russia"])]
print("\nTeam và Shooting Accuracy của England, Italy, Russia:")
print(specific_teams[["Team", "Shooting Accuracy"]])