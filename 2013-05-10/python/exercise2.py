#profilo sx

#scocca superiore tettuccio
#controls1=(MAP(BEZIER(S1)([[0.205,-0.410],  [0.269,-0.376], [0.325,-0.370],  [0.413,-0.384]]))(INTERVALS(1)(32)))

controls1=(MAP(BEZIER(S1)([[0.205,-0.410],  [0.229,-0.395], [0.254,-0.384],  [0.288,-0.372]]))(INTERVALS(1)(32)))

controls1_1=(MAP(BEZIER(S1)([[0.288,-0.372],  [0.320,-0.371], [0.348,-0.373],  [0.382,-0.378]]))(INTERVALS(1)(32)))

controls1_2=(MAP(BEZIER(S1)([[0.382,-0.378],  [0.403,-0.384], [0.425,-0.391],  [0.446,-0.399]]))(INTERVALS(1)(32)))

controls1_3=(MAP(BEZIER(S1)([[0.446,-0.399],[0.465,-0.405],[0.477,-0.409]]))(INTERVALS(1)(32)))

#scocca superiore cofano
#[0.205, -0.410],  [0.163, -0.418] , [0.125, -0.422],  [0.104, -0.430]


controls2=(MAP(BEZIER(S1)([[0.205, -0.410],  [0.163, -0.418] , [0.125, -0.422],  [0.104, -0.430]]))(INTERVALS(1)(32)))


controls3=(MAP(BEZIER(S1)([[0.104, -0.430],  [0.090,-0.440],  [0.084,-0.461],  [0.084,-0.490]]))(INTERVALS(1)(32)))

#[0.90,-0.440],  [0.84,-0.461],  [0.84,-0.490]

controls4=(MAP(BEZIER(S1)([[0.084, -0.490],  [0.112,-0.494],  [0.136,-0.495]]))(INTERVALS(1)(32)))


controls5=(MAP(BEZIER(S1)([[0.136, -0.495],  [0.140,-0.469],  [0.154,-0.445],[0.178,-0.440],[0.199,-0.445],[0.211,-0.459],[0.219,-0.477],[0.217,-0.495]]))(INTERVALS(1)(32)))


controls6=(MAP(BEZIER(S1)([[0.217,-0.495],[0.397,-0.495]]))(INTERVALS(1)(32)))


controls7=(MAP(BEZIER(S1)([[0.400,-0.495],[0.400,-0.477],[0.410,-0.457],[0.422,-0.447],[0.442,-0.443],[0.456,-0.449],[0.469,-0.459],[0.475,-0.470],[0.478,-0.495]]))(INTERVALS(1)(32)))


controls8=(MAP(BEZIER(S1)([[0.480,-0.495],[0.507,-0.492],[0.516,-0.490],[0.522,-0.481]]))(INTERVALS(1)(32)))

controls9=(MAP(BEZIER(S1)([[0.522,-0.481],[0.524,-0.460],[0.523,-0.453],[0.519,-0.453]]))(INTERVALS(1)(32)))

controls10=(MAP(BEZIER(S1)([[0.519,-0.453],[0.512,-0.436],[0.503,-0.426],[0.495,-0.418],[0.477,-0.409]]))(INTERVALS(1)(32)))

#vetro posteriore
#controls11=(MAP(BEZIER(S1)([[0.477,-0.409],[0.454,-0.395],[0.436,-0.388],[0.413,-0.384]]))(INTERVALS(1)(32)))



profiloSx=T(2)(0.496+0.03)(STRUCT([controls1,controls2,controls3,controls4,controls5,controls6,controls7,controls8,controls9,controls10,controls1_1,controls1_2,controls1_3]))

profiloDx= T(3)(0.192)(profiloSx)

proLateral=T(3)(-0.192/2)(STRUCT([profiloSx,profiloDx]))

#VIEW(proLateral)












#profilo superiore

#parafango
controls12=(MAP(BEZIER(S1)([[0.132,0,0.782],[0.142,0,0.782],[0.158,0,0.783],[0.176,0,0.783]]))(INTERVALS(1)(64)))

#faro
controls13=COLOR(RED)((MAP(BEZIER(S1)([[0.132,0,0.782],[0.109,0,0.769],[0.094,0,0.750],[0.082,0,0.732]]))(INTERVALS(1)(64))))
controls14=(MAP(BEZIER(S1)([[0.082,0,0.732],[0.081,0,0.685]]))(INTERVALS(1)(64)))

#metà posteriore
controls15=(MAP(BEZIER(S1)([[0.514,0,0.745],[0.521,0,0.728],[0.526,0,0.707],[0.527,0,0.688]]))(INTERVALS(1)(64)))

#continuo verso parafango parte posteriore
controls16=(MAP(BEZIER(S1)([[0.514,0,0.745],[0.505,0,0.765],[0.480,0,0.778],[0.446,0,0.782]]))(INTERVALS(1)(64)))

#scocca laterale
controls17=(MAP(BEZIER(S1)([[0.446,0,0.782],[0.394,0,0.780]]))(INTERVALS(1)(64)))

controls18=(MAP(BEZIER(S1)([[0.394,0,0.780],[0.349,0,0.780],[0.313,0,0.783]]))(INTERVALS(1)(64)))

controls19=(MAP(BEZIER(S1)([[0.313,0,0.783],[0.274,0,0.783],[0.226,0,0.780]]))(INTERVALS(1)(64)))

controls20=(MAP(BEZIER(S1)([[0.226,0,0.780],[0.202,0,0.783],[0.189,0,0.783],[0.176,0,0.783]]))(INTERVALS(1)(64)))

#VIEW(STRUCT([controls1,controls2,controls3,controls4,controls5,controls6,controls7,controls8,controls9,controls10,controls11]))

profiloSup=(STRUCT([controls13,controls14,controls12,controls15,controls16,controls17,controls18,controls19,controls20]))

#ok
proSup=T(2)(0.03)(STRUCT([   T(3)(0.688)(S([1,2,3])([1,1,-1])(profiloSup)),T(3)(-0.688)(profiloSup)]))

proSup2=T(2)(0.07)(proSup)

#VIEW(proSup)



#VIEW(STRUCT([proSup,proLateral,proSup2]))













#profilo anteriore

#tettuccio

controls21=(MAP(BEZIER(S1)([[0,-0.142,0.166],[0,-0.142,0.148],[0,-0.143,0.133],[0,-0.144,0.120]]))(INTERVALS(1)(64)))

#vetro laterale
controls22=(MAP(BEZIER(S1)([[0,-0.144,0.120],[0,-0.146,0.102],[0,-0.163,0.096],[0,-0.181,0.090]]))(INTERVALS(1)(64)))

controls23=(MAP(BEZIER(S1)([[0,-0.181,0.090],[0,-0.189,0.078],[0,-0.195,0.072],[0,-0.204,0.072]]))(INTERVALS(1)(64)))

controls24=(MAP(BEZIER(S1)([[0,-0.204,0.072],[0,-0.208,0.070],[0,-0.217,0.070],[0,-0.229,0.071]]))(INTERVALS(1)(64)))

controls25=(MAP(BEZIER(S1)([[0,-0.229,0.071],[0,-0.242,0.073],[0,-0.257,0.075],[0,-0.265,0.073]]))(INTERVALS(1)(64)))

controls26=(MAP(BEZIER(S1)([[0,-0.265,0.073],[0,-0.266,0.085],[0,-0.265,0.103]]))(INTERVALS(1)(64)))

controls27=(MAP(BEZIER(S1)([[0,-0.265,0.103],[0,-0.266,0.121],[0,-0.256,0.130],[0,-0.256,0.166]]))(INTERVALS(1)(64)))

profiloAnt=T(2)(0.266+0.03)(STRUCT([controls22,controls21,controls23,controls24,controls25,controls26,controls27]))


#ok

proAnt=T(1)(0.085)(STRUCT([T(3)(-0.166)(profiloAnt),T(3)(0.166)(S([1,2,3])([1,1,-1])(profiloAnt))]))

#VIEW(proAnt)


#VIEW(STRUCT([proSup,proLateral,proSup2,proAnt]))














#profilo posteriore

controls28=(MAP(BEZIER(S1)([[0,-0.141,0.43],[0,-0.141,0.409],[0,-0.143,0.393],[0,-0.144,0.383]]))(INTERVALS(1)(64)))

controls29=(MAP(BEZIER(S1)([[0,-0.144,0.383],[0,-0.146,0.37],[0,-0.157,0.364],[0,-0.168,0.359]]))(INTERVALS(1)(64)))

controls30=(MAP(BEZIER(S1)([[0,-0.144,0.383],[0,-0.146,0.37],[0,-0.157,0.364],[0,-0.168,0.359]]))(INTERVALS(1)(64)))

controls31=(MAP(BEZIER(S1)([[0,-0.168,0.359],[0,-0.181,0.354],[0,-0.19,0.341],[0,-0.201,0.338]]))(INTERVALS(1)(64)))

controls32=(MAP(BEZIER(S1)([[0,-0.201,0.338],[0,-0.217,0.338],[0,-0.232,0.339],[0,-0.248,0.342]]))(INTERVALS(1)(64)))


controls33=(MAP(BEZIER(S1)([[0,-0.248,0.342],[0,-0.258,0.344],[0,-0.262,0.349],[0,-0.264,0.362]]))(INTERVALS(1)(64)))

controls34=(MAP(BEZIER(S1)([[0,-0.264,0.362],[0,-0.265,0.381],[0,-0.251,0.387],[0,-0.250,0.4]]))(INTERVALS(1)(64)))

controls35=(MAP(BEZIER(S1)([[0,-0.250,0.4],[0,-0.25,0.43]]))(INTERVALS(1)(64)))

#ok
profiloPost=(T(2)(0.265)(STRUCT([controls28,controls29,controls30,controls31,controls32,controls33,controls34,controls35])))
proPost=T([1,2])([0.52,0.012])(STRUCT([T(3)(-0.43)(profiloPost),T(3)(0.43)(S([1,2,3])([1,1,-1])(profiloPost))]))

#VIEW(proPost)

profileTotal=T(1)(-0.3)(STRUCT([proSup,proLateral,proSup2,proAnt,proPost]))

profileTotal=S([1,2,3])([20,20,20])(profileTotal)

#VIEW(STRUCT([profileTotal,ruote]))


VIEW(profileTotal)


