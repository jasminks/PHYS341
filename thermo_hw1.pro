pro thermo_hw1
set_plot,'ps'
device,filename='tempvspressure.ps',/color,bits=8
obj=5
loadct,11
plotsym,0,/fill
  
xp=10.^5
pressure=[1.0*xp,1.1*xp,1.2*xp,1.3*xp,1.4*xp]
volume=[20,21.8,23.7,25.4,27.3]
temp=[273,298,323,348,373]
press1=[-9200.,1.0*10.^5]
temp1=[0.,273.]

plot,temp,pressure,xtitle='Temperature (K)',ytitle='Pressure (N/m^2)',xrange=[0,400],yrange=[-10000,pressure[4]+10000]
oplot,temp,pressure,color=50,symsize=0.75,psym=8
oplot,temp1,press1,linestyle=5


device,/close
end
