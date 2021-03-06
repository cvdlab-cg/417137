//es 1

var dominio = DOMAIN([[-15, 15], [-15, 15]])([20,20]);

var terrain = function(punto){
	var x = punto[0];
	var y = punto[1];
	var z =  1;
	
	if (y==15 || y==-15)
		return [x,y,0]

	if (x==15 || x==-15)
		return [x,y,0]

	return [x, y, Math.random()*z*2];
}

brown  = [90/255,50/255,20/255]; 

brown2  = [50/255,10/255,10/255]; 

var DTM = MAP(terrain)(dominio);

pianura=(COLOR(brown)(CUBOID([30,13]))) //terreno pianeggiante

DRAW(T([0,1])([-15,+15])(pianura))

DRAW(COLOR(brown)(DTM));


//es 2

vertici=DTM.geometry.vertices;

MinMax=function (vertici) {
MinZ=[0,0,1];
MaxZ=[0,0,0];
for (var i = 0; i <vertici.length; i++) {
		if (vertici[i].position.z>MaxZ[2]){
			MaxZ[0]=vertici[i].position.x
			MaxZ[1]=vertici[i].position.y
			MaxZ[2]=vertici[i].position.z
		}
		if (vertici[i].position.z<MinZ[2])
			MinZ=[vertici[i].position.x,vertici[i].position.y,vertici[i].position.z]
	};
	return [MinZ,MaxZ];
}

m=MinMax(vertici);

//lago
blue = [0,0,1]; 
lago=COLOR(blue)(CUBOID([16,20]))
DRAW(T([0,1,2])([-10,-8,m[0][2]+0.3])(lago));



//es3

//albero
function tree(height,radius,discrAng){
	  green = [0,1,0]; 
    var model = CYL_SURFACE([radius/4,height/2])([32]);
    //DRAW(model);
    model=COLOR(brown2)(model)
    var domain = DOMAIN([[0,1],[0,2*PI]])([20,discrAng]);
    var profile = BEZIER(S0)([[radius,0,0.25],[0,0,height]]);
    var mapping = ROTATIONAL_SURFACE(profile);
    var surface = COLOR(green)(MAP(mapping)(domain));
    //DRAW(surface);
    return(STRUCT([model,surface]))
}

tr=tree(1.2,0.3,32)
//disegno alberi da una certa quota in poi
for (var i = 0; i <vertici.length; i++) {
if(vertici[i].position.z>m[1][2]-0.4){
	t=T([0,1,2])([vertici[i].position.x,vertici[i].position.y,vertici[i].position.z])(tr)
	DRAW(t);}
}


//es4
red = [1,0,0]; 

//4 villaggio
function home(){
	random=Math.random()
	return COLOR(red)( CUBOID([(3+3*random)/9,(3+4*random)/9,(3+2.5*random)/9]))
}

function settlement(vertici){
for (var i = 0; i <vertici.length; i++) {
if(vertici[i].position.z<m[0][2]+0.6 && m[0][2]+0.3  <vertici[i].position.z){
	if (vertici[i].position.y>-14 && vertici[i].position.x>-14 && vertici[i].position.y<14 && vertici[i].position.x<14)
		DRAW(T([0,1,2])([vertici[i].position.x,vertici[i].position.y,vertici[i].position.z])(home()))

}
}
}

black = [0.3,0.3,0.3]; 

function settl (x,y,numCase){
for (var i = 0; i <numCase; i++) {
	for (var j = 0; j <numCase; j++) {

	DRAW(COLOR(black)(T([0,1])([i+x,j+y]) (home())))
}
}
}

settl (7,16,7);
settl(-10,20,7);
