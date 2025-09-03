file_name = 'data/juso.txt'

with open(file_name,'a',encoding='utf-8')as file:
    name='이가연'
    phone='010-1234-5678'
    address='경기도 광명시 소하동'
    file.write(f"{name},{phone},{address}\n")

    name='심청이'
    phone='010-0000-0000'
    address='경기도 광명시 소하동'
    file.write(f"{name},{phone},{address}\n")