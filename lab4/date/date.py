from datetime import*

def currentday():

    today = datetime.now()
    
    result = today - timedelta(days = 5)
    return result

print(currentday())


def todaytomorrowyesterday():

    today = datetime.now()
    tomorrow = today + timedelta(days = 1)
    yesterday = today - timedelta(days = 1)

    result = f"today - {today} \n tomorrow - {tomorrow}  \n yesterday - {yesterday}"
    return result

print(f"\n {todaytomorrowyesterday()}")


def currentdaymicrosec():

    today = datetime.now()
    
    result = today.replace(microsecond=0)
    return result

print(f"\n {currentdaymicrosec()}")


def diffintime():

    today = datetime.now()
    tomorrow = today + timedelta(days = 1)
    
    result = (tomorrow - today).total_seconds()
    return result

print(f"\n {diffintime()}")

