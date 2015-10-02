pro thermo_hw2
set_plot,'ps'
device,filename='tempvsvolume.ps',/color,bits=8
obj=5
loadct,11
plotsym,0,/fill
  
xp=10.^5
pressure=[1.0*xp,1.1*xp,1.2*xp,1.3*xp,1.4*xp]
volume=[20.,21.8,23.7,25.4,27.3]
temp=[273.,298.,323.,348.,373.]
temp1=[0,273]
vol1=[-0.252,20.]


plot,temp,volume,xtitle='Temperature (K)',ytitle='Volume (L)',xrange=[0,400],yrange=[vol1[0]-1.0,volume[4]+1.0]
oplot,temp,volume,color=50,symsize=0.75,psym=8
oplot,temp1,vol1,linestyle=5

;oplot,temp1,press1,linestyle=5

y=volume[2]-volume[0]
x=temp[2]-temp[0]
print,y/x


device,/close
end
