function pushFirstNatural(array,n){
array.push(n);
if (n>0)
	pushFirstNatural(array,n-1);
}
