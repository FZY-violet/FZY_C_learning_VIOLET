alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points','No point value assigned.')#第一个参数用于指定键，必不可少，而第二个参数为当指定的键不存在时要返回的值。
print(point_value)

alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points')#若未指定第二个参数，那么返回值为None
print(point_value)