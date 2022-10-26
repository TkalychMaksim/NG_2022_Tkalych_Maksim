seconds = int(input('Enter number of seconds:'))
t_days = seconds//86400
# Counting the number of days from the t_seconds
t_hours = (seconds - (t_days*86400))//3600
# Counting of the number of hours from the rest
t_minutes = ((seconds-(t_days*86400) - (t_hours *3600)) // 60)
# Counting the number of minutes left from steps 2,4
t_seconds = (seconds -(t_days * 86400) - (t_hours *3600) -(t_minutes * 60))
#Counting the number of seconds left
print('Days:' +str(t_days), 'Hours:' + str(t_hours), 'Minutes:' +str(t_minutes), 'Seconds:' + str(t_seconds))