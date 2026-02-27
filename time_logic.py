print("Give me seconds and I'll convert it to hours, minutes, seconds")
given_second = int(input())

hour = given_second // 3600
minute = (given_second % 3600) // 60
second = given_second % 60


print(hour, "Hour", minute, "Minute", second, "Second")