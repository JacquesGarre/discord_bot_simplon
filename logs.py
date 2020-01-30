def Save(p_date,p_output):
    with open('Logs/Log-{}-{}.log'.format(p_date.year,p_date.month),'a') as log_file:
        log_file.write('{Y}-{M}-{D} {h}:{m} - {o}\n'.format(Y=p_date.year,M=p_date.month,D=p_date.day,h=p_date.hour,m=p_date.minute,o=p_output))

def Show(p_date,p_output):
    print('{Y}-{M}-{D} {h}:{m} - {o}'.format(Y=p_date.year,M=p_date.month,D=p_date.day,h=p_date.hour,m=p_date.minute,o=p_output))

def Full(p_date,p_output):
    Save(p_date,p_output)
    Show(p_date,p_output)