function r = moda(varargin)
%counting sort
numeros = cell2mat(varargin);
nordenados = sort(numeros);
t = size(nordenados);

s(1:(nordenados(end)+1))=0;

    for i = 1 : t(2)
        s(nordenados(i)+1) = s(nordenados(i)+1)+1;
    end
    
    n=max(s);
    j=0;
    
    for i=1:(nordenados(end)+1)
        if(s(i)==n)
            j=j+1;
        end
    end
    
    p(j)=0;
    k=1;
    
    for i=1 : (nordenados(end)+1)
       if(n==s(i))
            p(k)=i-1;
            k=k+1;
       end
    end
    
    r=p;
end