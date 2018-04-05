function r = mediana(varargin)

numeros = cell2mat(varargin);
nordenados = sort(numeros);
t = size(nordenados);

if((mod(t(2),2)==0))
    r = (nordenados(t(2)/2)+nordenados(t(2)/2+1))/2;
else
    if ((mod(t(2),2)==1))
       r = nordenados(t(2)/2+0.5);
    end 
end 
end