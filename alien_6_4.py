alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':5}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
    
#创建一个用于存储外星人的空列表
aliens=[]
#使用range创建30个绿色外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:       #显示前五个外星人
    print(alien)
print("...")
print(f"Total number of aliens:{len(aliens)}")#显示创建了多少个外星人

#创建一个用于存储外星人的空列表
aliens=[]
#使用range创建30个绿色外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
for alien in aliens[:5]:       #显示前五个外星人
    print(alien)
print("...")

#创建一个用于存储外星人的空列表
aliens=[]
#使用range创建30个绿色外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['ccolor']='red'
        alien['speed']='fast'
        alien['points']=15
for alien in aliens[:5]:       #显示前五个外星人
    print(alien)
print("...")
