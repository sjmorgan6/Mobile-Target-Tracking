%For plotting solutions
%To use, import your data: home>import data> select your file (i.e.
% output_ga_example_objectives.csv)

pointsize = 25;
x = table2array(outputgaexampleobjectives(:,1))
x(~any(~isnan(x),2),:)=[]
y = table2array(outputgaexampleobjectives(:,2))
y(~any(~isnan(y),2),:)=[]
z = table2array(outputgaexampleobjectives(:,3))/1000
z(~any(~isnan(z),2),:)=[]
scatter(x, z, pointsize, -y, 'filled', 'MarkerEdgeColor', [0,0,0])
hold on;

xlabel('Delta-V Used Per Satellite (m/s)')
title('Single Satellite Example')
ax = gca
ax.FontSize = 12;

y = ylabel('Mean Distance for all Targets Accessed (km)')
ylim([0 100])
xlim([0 7])
h = colorbar;
set(h,'YTick',[0:10:50])
cb = ylabel(h, 'Total Approximate Access Time (s)')
cb.FontSize = 14


hold off;