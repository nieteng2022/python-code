# code
# 导入time模块
import time

# 定义一个专注时钟函数，接受一个参数minutes，表示要专注的分钟数
def focus_timer(minutes):
    # 将分钟数转换为秒数
    seconds = minutes * 60
    # 循环直到秒数为0
    while seconds:
        # 计算剩余的分钟数和秒数
        mins, secs = divmod(seconds, 60)
        # 格式化输出剩余时间，例如 05:30
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # 在同一行打印剩余时间，并覆盖上一次的输出
        print(timer, end="\r")
        # 等待一秒
        time.sleep(1)
        # 秒数减一
        seconds -= 1
    # 打印提示信息
    print("Time's up!")

# 如果是主程序，执行以下代码
if __name__ == "__main__":
    # 输入要专注的分钟数，转换为整数类型
    minutes = int(input("Enter the number of minutes to focus: "))
    # 调用专注时钟函数
    focus_timer(minutes)
