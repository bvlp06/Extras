function [o,p,q,r] = disf(varargin)

numerosAmostra = cell2mat(varargin);
ordAmostra = sort(numerosAmostra);
t = size(ordAmostra);
tamAmostra = t(2);
ampTotal = ordAmostra(end)-ordAmostra(1);

if(tamAmostra<=100)
    numClasses= fix(sqrt(tamAmostra));
else
    numClasses= fix(5*log10(tamAmostra));
end

ampClas = ampTotal/numClasses;

d=cell(numClasses+1,8);% tabela da distribuição de frequencia em classes
d(1,1)= {'classe'};
d(1,2)={'xmedio da classe'};
d(1,3)=  {'freq abs simples '};
d(1,4)= {'freq rel simples '};
d(1,5)= {'porc freq rel simples'};
d(1,6)= {'freq abs acum'};
d(1,7)= {'freq rel acum'};
d(1,8)= {'porc freq rel acum'};

fabsC(1:numClasses)=0; %freq abs em classes

for i=1:numClasses
    a=num2str(ordAmostra(1)+ampClas*(i-1));
    b=num2str(ordAmostra(1)+ampClas*(i));
    c = strcat(a,'|--|',b);
   d(i+1,1) = {c};
   e = (2*ordAmostra(1)+ampClas*(i-1)+ampClas*(i))/2;
   d(i+1,2) = {e};
end

for i=1:numClasses
    f=0;
    for j=1:tamAmostra
    
        a=(ordAmostra(1)+ampClas*(i-1));
        b=(ordAmostra(1)+ampClas*(i));
    
        if(ordAmostra(j)>=a)
            if(ordAmostra(j)<=b)
                f=f+1;
            end
        end       
    end
            fabsC(i)=f; 
            d(i+1,3)={fabsC(i)};
end

frkabs(1:numClasses)=0;

frkabs= fabsC./t(2);

porcfrkabs(1:numClasses)=0;

porcfrkabs=frkabs.*100;

facuC(1:numClasses)=0;

for i=1:numClasses
    if(i==1)
    facuC(i)= fabsC(i);
    else
       facuC(i)=facuC(i-1)+fabsC(i); 
    end
     d(i+1,4)={frkabs(i)};
     d(i+1,5)={porcfrkabs(i)};
     d(i+1,6)={facuC(i)};
end
frkacuC(1:numClasses)=0;

frkacuC= facuC./t(2);

porcfrkacu(1:numClasses)=0;

porcfrkacu=frkacuC.*100;

for i=1:numClasses
     d(i+1,7)={frkacuC(i)};
     d(i+1,8)={porcfrkacu(i)};
end

o=ampTotal; %retorna a amplitude total
p=numClasses; %retorna o numero de classes
q=ampClas; %retorna amplitude de classe
r=d; %retorna tabela de distribuicao de freq em classes

end