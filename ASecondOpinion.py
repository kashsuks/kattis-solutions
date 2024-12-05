totalSeconds = int(input(""))

hours = totalSeconds // 3600
leftoverHours = totalSeconds % 3600
minutes = leftoverHours // 60
seconds = leftoverHours % 60
print(f"{hours} : {minutes} : {seconds}")