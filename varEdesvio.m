function [d,v] = varEdesvio(varargin)
%std - desvio padrao
numeros = cell2mat(varargin); %numeros
somaDosnumeros = sum(numeros); %soma dos numeros

somadoQuadnum = sum(numeros.^2); % soma do quadrado dos numeros
t = size(numeros); % quantos numeros tem

v =(1/(t(2)-1))*(somadoQuadnum - ((somaDosnumeros)^2)/t(2));
d =sqrt((1/(t(2)-1))*(somadoQuadnum - ((somaDosnumeros)^2)/t(2)));

end