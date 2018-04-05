function r = media(varargin)
%mean - media
numeros = cell2mat(varargin);
somaDosnumeros = sum(numeros);

t = size(numeros);

r=somaDosnumeros/t(2);

end