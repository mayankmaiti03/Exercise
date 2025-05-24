def consecutive_sim_frequency(tl):
  res=[]
  idx=0
  while idx<len(tl):
    st=idx
    val=tl[idx]
    while idx<len(tl) and tl[idx]==val:
      idx+=1
    count=idx-st
    res.append((val,count))
  return res
consecutive_sim_frequency([2, 2, 3, 3, 3, 3, 4,2])
