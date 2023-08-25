clc;
clear all;
close all;
a=arduino();
for i = 1:1000 
   voltage(i) = readVoltage(a,'A0');   
   plot(voltage, 'b');
   title('x');
   pause(.002);
end