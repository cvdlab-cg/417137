for(i=1;i<11;i++){
	a=""
	for(j=1;j<11;j++){
		if (j === 10)
			a += j*i+"\t";	 
		else
			a += j*i+",\t";
		}
	console.log(a);

}

