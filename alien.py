alien_0={'color':'green','points' : 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0={'color':'green','points' : 5}
new_prints=alien_0['points']
print(f"\tYou just earned {new_prints} prints!")

alien_0={'color':'green','points' : 5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

alien_0={'color':'green'}
print(f"The alien is now {alien_0['color']}")
alien_0['color']='yellow'
print(f'The alien is now {alien_0["color"]}')

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
alien_0['speed']='fast'#在更改之后为“快”
print(f"Original position:{alien_0['x_position']}")
#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed']=='show':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    #这个外星人的移动速度肯定很快
    x_increment=3
#新位置为旧位置加移动距离
alien_0['x_position']=alien_0['x_position']+x_increment
print(f'New position:{alien_0['x_position']}')

alien_0={'color':'green','points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)