money = float(input("Nhập số tiền hiện có của sinh viên: "))

food = float(input("Chi phí ăn uống mỗi ngày: "))
rent = float(input("Chi phí ở mỗi ngày: "))
electric = float(input("Chi phí điện mỗi ngày: "))
transport = float(input("Chi phí đi lại mỗi ngày: "))

asset_value = float(input("Giá trị gốc tài sản: "))
depreciation_rate = float(input("Tỷ lệ khấu hao (% mỗi ngày): "))

depreciation = asset_value * (depreciation_rate / 100)

daily_expense = food + rent + electric + transport + depreciation
print("Tổng chi phí 1 ngày:", daily_expense)

weekly_expense = daily_expense * 7
print("Tổng chi phí 1 tuần:", weekly_expense)

final_money = money - weekly_expense
print("Số tiền còn lại sau 1 tuần:", final_money)
