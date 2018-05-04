import random
import math

NUM_CLUSTERS = 4 #numero de clustes
TOTAL_DATA = 500 #total de registros
C = [100,200,300,400] #de 0 a 499 #escolher os cluters
BIG_NUMBER = math.pow(10, 10)  #max distancia

#dataset
SAMPLES = [[1 , 71] , [1 , 1056] , [1 , 1396] , [1 , 1794] , [1 , 2293] , [1 , 2643] , [1 , 2773] , [1 , 3299] , [1 , 3406] , [2 , 4171] , [2 , 4319] , [2 , 4937] , [2 , 5027] , [2 , 5759] , [2 , 6002] , [2 , 6258] , [2 , 6541] , [2 , 6687] , [2 , 6930] , [2 , 7031] , [2 , 7257] , [2 , 7323] , [2 , 7422] , [3 , 7656] , [3 , 8020] , [3 , 8103] , [3 , 8315] , [3 , 8377] , [3 , 8560] , [3 , 8585] , [3 , 8666] , [3 , 9647] , [3 , 9840] , [3 , 9990] , [3 , 10442] , [3 , 10917] , [3 , 11080] , [4 , 11271] , [4 , 11642] , [4 , 11700] , [4 , 11952] , [4 , 12136] , [4 , 12144] , [4 , 12353] , [4 , 12468] , [4 , 12606] , [4 , 12666] , [4 , 13301] , [4 , 13311] , [4 , 13530] , [4 , 13582] , [4 , 13726] , [4 , 14042] , [5 , 14150] , [5 , 14155] , [5 , 14271] , [5 , 14283] , [5 , 14300] , [5 , 14691] , [5 , 14736] , [5 , 14810] , [5 , 14817] , [5 , 14898] , [5 , 15081] , [5 , 15159] , [5 , 15862] , [5 , 15951] , [5 , 16094] , [6 , 16226] , [6 , 16317] , [6 , 16617] , [6 , 16731] , [6 , 16858] , [6 , 16920] , [6 , 17078] , [6 , 17265] , [6 , 17571] , [6 , 17832] , [6 , 18081] , [6 , 18107] , [6 , 18131] , [6 , 18400] , [6 , 18749] , [6 , 19174] , [6 , 19176] , [6 , 19780] , [6 , 19928] , [7 , 20250] , [7 , 20500] , [7 , 20735] , [7 , 20840] , [7 , 20892] , [7 , 21754] , [7 , 22075] , [7 , 22082] , [7 , 22438] , [7 , 22473] , [7 , 22580] , [7 , 22714] , [7 , 23009] , [7 , 23627] , [7 , 23716] , [7 , 23910] , [7 , 23977] , [8 , 24046] , [8 , 24400] , [8 , 24867] , [8 , 24899] , [8 , 25308] , [8 , 25525] , [8 , 25611] , [8 , 25924] , [8 , 25989] , [8 , 26494] , [8 , 26549] , [8 , 26603] , [9 , 26982] , [9 , 27742] , [9 , 27767] , [9 , 27807] , [9 , 27814] , [9 , 28143] , [9 , 28208] , [9 , 28270] , [9 , 28625] , [9 , 28643] , [9 , 28702] , [9 , 29163] , [9 , 29372] , [9 , 29522] , [9 , 30759] , [9 , 30871] , [9 , 30909] , [9 , 31702] , [9 , 32046] , [9 , 32465] , [9 , 32736] , [9 , 32777] , [9 , 33310] , [9 , 33891] , [10 , 34478] , [10 , 34778] , [10 , 34802] , [10 , 35390] , [10 , 35746] , [10 , 35935] , [10 , 36487] , [10 , 36490] , [10 , 36847] , [10 , 38053] , [10 , 38860] , [10 , 38877] , [10 , 39176] , [11 , 39362] , [11 , 39687] , [11 , 39699] , [11 , 39711] , [11 , 39898] , [11 , 40142] , [11 , 40263] , [11 , 40396] , [11 , 40492] , [11 , 40677] , [11 , 41495] , [11 , 42313] , [12 , 42635] , [12 , 42718] , [12 , 42853] , [12 , 42860] , [12 , 42866] , [12 , 42941] , [12 , 43001] , [12 , 43988] , [12 , 44222] , [12 , 44390] , [12 , 44662] , [12 , 44666] , [12 , 44833] , [12 , 44947] , [12 , 45268] , [13 , 45340] , [13 , 45574] , [13 , 45644] , [13 , 46942] , [13 , 46964] , [13 , 47355] , [13 , 48496] , [13 , 48547] , [13 , 48551] , [13 , 48926] , [14 , 49386] , [14 , 49469] , [14 , 49634] , [14 , 49842] , [14 , 50949] , [14 , 51482] , [14 , 52417] , [14 , 52753] , [14 , 52810] , [14 , 53117] , [14 , 53286] , [14 , 53461] , [15 , 53531] , [15 , 53567] , [15 , 53568] , [15 , 53810] , [15 , 53849] , [15 , 54295] , [15 , 54323] , [15 , 54619] , [15 , 54718] , [15 , 54939] , [15 , 55961] , [15 , 56038] , [15 , 56299] , [15 , 56572] , [15 , 57058] , [15 , 57120] , [15 , 57282] , [15 , 57286] , [15 , 57964] , [15 , 57992] , [15 , 58040] , [15 , 58386] , [16 , 58407] , [16 , 59218] , [16 , 59405] , [16 , 59633] , [16 , 59712] , [16 , 59725] , [16 , 59936] , [16 , 60100] , [16 , 60214] , [16 , 60531] , [16 , 60985] , [16 , 61100] , [16 , 61568] , [16 , 61815] , [17 , 62541] , [17 , 62754] , [17 , 63055] , [17 , 63244] , [17 , 64728] , [17 , 64736] , [17 , 65381] , [17 , 65405] , [17 , 65456] , [17 , 65506] , [17 , 65827] , [17 , 66092] , [17 , 66199] , [17 , 66826] , [17 , 66849] , [17 , 67243] , [17 , 67381] , [17 , 68233] , [17 , 68261] , [18 , 69306] , [18 , 69448] , [18 , 69736] , [18 , 70208] , [18 , 70455] , [18 , 70537] , [18 , 70882] , [18 , 70930] , [18 , 71024] , [18 , 71237] , [18 , 71597] , [18 , 71635] , [18 , 71668] , [18 , 71714] , [19 , 72060] , [19 , 72099] , [19 , 72334] , [19 , 72711] , [19 , 72898] , [19 , 73000] , [19 , 73020] , [19 , 73425] , [19 , 73537] , [19 , 73771] , [19 , 74188] , [19 , 74491] , [19 , 74560] , [19 , 75025] , [19 , 75151] , [20 , 75302] , [20 , 75374] , [20 , 75470] , [20 , 75676] , [20 , 75852] , [20 , 76273] , [20 , 77451] , [20 , 77580] , [20 , 77949] , [20 , 78313] , [20 , 78496] , [20 , 78604] , [20 , 78677] , [21 , 78731] , [21 , 79109] , [21 , 79123] , [21 , 79384] , [21 , 80624] , [21 , 80662] , [21 , 80723] , [21 , 81469] , [21 , 81478] , [21 , 82062] , [21 , 82331] , [21 , 82697] , [21 , 82987] , [21 , 83791] , [22 , 83830] , [22 , 84038] , [22 , 84505] , [22 , 84767] , [22 , 85035] , [22 , 85195] , [22 , 85289] , [22 , 85752] , [22 , 85815] , [22 , 86308] , [22 , 86443] , [22 , 86497] , [22 , 86662] , [22 , 86679] , [23 , 87150] , [23 , 87388] , [23 , 87507] , [23 , 88249] , [23 , 88250] , [23 , 88265] , [23 , 88493] , [23 , 88503] , [23 , 89228] , [23 , 89480] , [23 , 89909] , [23 , 89967] , [23 , 90169] , [23 , 90613] , [23 , 90621] , [23 , 90644] , [23 , 90895] , [23 , 91178] , [23 , 91619] , [23 , 91765] , [23 , 92011] , [24 , 92262] , [24 , 92302] , [24 , 92353] , [24 , 92479] , [24 , 92548] , [24 , 92853] , [24 , 93492] , [24 , 93792] , [24 , 93848] , [24 , 93996] , [24 , 94019] , [24 , 94051] , [24 , 94865] , [24 , 94936] , [24 , 95047] , [24 , 95407] , [24 , 95434] , [25 , 95480] , [25 , 96554] , [25 , 97342] , [25 , 97568] , [25 , 97595] , [25 , 98370] , [25 , 98511] , [25 , 98517] , [25 , 99137] , [25 , 99220] , [25 , 99397] , [25 , 99406] , [25 , 99609] , [26 , 99717] , [26 , 99905] , [26 , 99988] , [26 , 100070] , [26 , 100070] , [26 , 100244] , [26 , 100398] , [26 , 100649] , [26 , 100753] , [26 , 101064] , [26 , 101076] , [27 , 101133] , [27 , 101513] , [27 , 101916] , [27 , 101936] , [27 , 102344] , [27 , 102346] , [27 , 102510] , [27 , 102793] , [27 , 103074] , [27 , 103127] , [27 , 103135] , [27 , 103590] , [27 , 103796] , [27 , 103810] , [28 , 103819] , [28 , 103831] , [28 , 104212] , [28 , 104218] , [28 , 104318] , [28 , 104928] , [28 , 105324] , [28 , 105486] , [28 , 105561] , [28 , 105898] , [28 , 106051] , [28 , 106525] , [28 , 106565] , [28 , 106646] , [28 , 106705] , [28 , 107279] , [28 , 107708] , [28 , 107778] , [28 , 107860] , [28 , 108182] , [28 , 109150] , [29 , 109243] , [29 , 109963] , [29 , 110079] , [29 , 110179] , [29 , 110458] , [29 , 110933] , [29 , 111183] , [29 , 111454] , [29 , 111485] , [29 , 112378] , [29 , 112523] , [30 , 113698] , [30 , 114056] , [30 , 114100] , [30 , 114847] , [30 , 115056] , [30 , 115155] , [30 , 115304] , [30 , 115957] , [30 , 116160] , [31 , 116254] , [31 , 116368] , [31 , 116466] , [31 , 116835] , [31 , 117012] , [31 , 117036] , [31 , 117443] , [31 , 117601] , [31 , 117981] , [31 , 118667] , [31 , 119378] , [31 , 119850] , [32 , 120215] , [32 , 120252] , [32 , 120545] , [32 , 120743] , [32 , 120818] , [32 , 121121] , [32 , 121296] , [32 , 121616] , [32 , 122194] , [32 , 122196] , [32 , 123138] , [32 , 123364] , [32 , 124349] , [32 , 124697] , [32 , 125323] , [33 , 125498] , [33 , 125713] , [33 , 125903] , [33 , 125936] , [33 , 126058] , [33 , 126145] , [33 , 126324] , [33 , 126785] , [33 , 126877] , [33 , 127307] , [33 , 127971] , [33 , 128157] , [33 , 128371] , [33 , 128717] , [33 , 129187] , [33 , 130198] , [33 , 131031] , [33 , 131321] , [34 , 132611] , [34 , 132683] , [34 , 132894] , [34 , 133372] , [34 , 133437] , [34 , 133504] , [34 , 133633] , [34 , 133644] , [34 , 134151] , [34 , 134378] , [34 , 134932]]

#lista q guarda o dataSet já classificado
data = []
centroids = []

#classe dos pontos onde guarda as coordenadas e o seu respectivo cluster
class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    
    def get_cluster(self):
        return self.clusterNumber
#classe para o centroide q guarda suas coordenadas
class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y

#inserir novo Elemento
def insertNewEle(SAMPLES):
    u=[]
    x=input('Digite a coordenada X    ')
    u.append(int(x))
    y=input('Digite a coordenada Y    ')
    u.append(int(y))
    SAMPLES.append(u)
    SAMPLES.sort(key=lambda x:x[0])
    return 

#inicializar o algoritmo, identifica os centroids iniciais
def initialize_centroids():
    # Set the centoid coordinates to match the data points furthest from each other.
    # centoide (1.0, 1.0) and (5.0, 7.0)
    centroids.append(Centroid(SAMPLES[C[0]][0], SAMPLES[C[0]][1]))
    centroids.append(Centroid(SAMPLES[C[1]][0], SAMPLES[C[1]][1]))
    centroids.append(Centroid(SAMPLES[C[2]][0], SAMPLES[C[2]][1]))
    centroids.append(Centroid(SAMPLES[C[3]][0], SAMPLES[C[3]][1]))
    
    print("Centroids initialized at:")
    print("(", centroids[0].get_x(), ", ", centroids[0].get_y(), ")")
    print("(", centroids[1].get_x(), ", ", centroids[1].get_y(), ")")
    print("(", centroids[2].get_x(), ", ", centroids[2].get_y(), ")")
    print("(", centroids[3].get_x(), ", ", centroids[3].get_y(), ")")
    print()
    return

def initialize_datapoints():
    # As coordenadas x e y dos registros são pegas da lista SAMPLES
    # Eles são classificados de acordo com os centroids iniciais
    for i in range(TOTAL_DATA):
        newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1])
        
        if(i == C[0]):
            newPoint.set_cluster(0)
        elif(i == C[1]):
            newPoint.set_cluster(1)
        elif(i == C[2]):
            newPoint.set_cluster(2)
        elif(i == C[3]):
            newPoint.set_cluster(3)
        else:
            newPoint.set_cluster(None)
            
        data.append(newPoint) #lista da classe DataPoint
    
    return

def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    # calcula a Distancia Euclidiana.
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))

def recalculate_centroids():
    #reescolhe os centroids
    totalX = 0
    totalY = 0
    totalInCluster = 0
    
    for j in range(NUM_CLUSTERS): #no nosso caso j vai até 4
        for k in range(len(data)): #no nosso k até o 500 (tamanho de registro)
            if(data[k].get_cluster() == j): #se o data[k] pertencer ao cluster J
                totalX += data[k].get_x()   #soma a coordenada X
                totalY += data[k].get_y()  #soma a coordenada Y
                totalInCluster += 1   #conta quantos elementos tem no cluster J
        
        if(totalInCluster > 0):
            centroids[j].set_x(totalX / totalInCluster)  #coordenada X do centroide J
            centroids[j].set_y(totalY / totalInCluster)  #coordenada Y do centroide J
    return

def update_clusters(): #atualiza o cluster do elemento
    isStillMoving = 0 #para verificar se chegou na convergencia
    
    for i in range(TOTAL_DATA):
        bestMinimum = BIG_NUMBER  #menor distancia
        currentCluster = 0 #possivel Cluster
        
        for j in range(NUM_CLUSTERS): # j vai de 0 a 3
            #calcula a distancia entre o data[i] e o centroide[j]
            distance = get_distance(data[i].get_x(), data[i].get_y(), centroids[j].get_x(), centroids[j].get_y())
            if(distance < bestMinimum): #se a distancia calculada do centroid[j+1] for menor que a do centroid[j]
                bestMinimum = distance #recebe a distancia
                currentCluster = j #atualiza o numero do cluster
        #No fim atualiza de fato no registro
        data[i].set_cluster(currentCluster) # atualiza o numero do cluster q o data[i] pertence

        #se n tiver cluster ou se for diferente do possivel cluster
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster): 
            data[i].set_cluster(currentCluster) #atualiza o cluster
            isStillMoving = 1   #não chegou na convergencia
    
    return isStillMoving

def perform_kmeans():
    isStillMoving = 1 #não chegoi na convergencia
   
    #inicializa TUDO
    
    initialize_centroids()
    
    initialize_datapoints()
    
    while(isStillMoving): #enquanto for 1
        recalculate_centroids() #recalcula os centroids
        isStillMoving = update_clusters() #reescolhe os cluters do registro
    
    return

def print_results():
    for i in range(NUM_CLUSTERS):
        print('Cluster :', i+1)
        for j in range(TOTAL_DATA):
            if(data[j].get_cluster() == i):
                print("(", data[j].get_x(), ", ", data[j].get_y(), ")")
        print()
    
    return
    
r=1
while r>0:
    
    r=input('Se deseja inserir um novo elemento digite 2, se não digite 1  ')
    while int(r)>1:
        insertNewEle(SAMPLES)
        TOTAL_DATA = TOTAL_DATA+1
        print(TOTAL_DATA)
        r=input('Se deseja inserir mais um elemento digite 2, se não digite 1  ')

    data = []
    centroids = []
    perform_kmeans()
    print_results()
    r = input('Se deseja sair digite 0, se não digite 1   ')
    r=int(r)
