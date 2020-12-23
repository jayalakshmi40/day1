from PIL import Image,ImageDraw,ImageFont
import pandas  as  pd
df =pd.read_excel("Book.xlsx")
for index,j in df.iterrows():
    img=Image.open('template.jpg')
    draw=ImageDraw.Draw(img)
    draw.text(xy=(700,690),text='{}'.format(j['Name']),file=(0,137,209),font=ImageFont.truetype('arial.ttf',100))
    draw.text(xy=(700,890),text='{}'.format(j['Project name']),file=(0,0,102),font=ImageFont.truetype('arial.ttf',75))
    draw.text(xy=(240,840),text='{}'.format(j['Mentor name']),file=(102,0,51),font=ImageFont.truetype('arial.ttf',30))
    draw.text(xy=(300,1150),text='{}'.format(j['Project manager']),file=(102,0,51),font=ImageFont.truetype('arial.ttf',30))
    draw.text(xy=(800,1350),text='{}'.format(j['Certificate number']),file=(0,137,209),font=ImageFont.truetype('arial.ttf',25))
    img.save('Certificates\{}.jpg'.format(j['Name']))
print("success")
