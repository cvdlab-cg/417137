function capitalizedText(string){
s="";
array=string.split(" ");
for (word in array){
	s+=array[word].charAt(0).toUpperCase()+array[word].slice(1,word.lenght)+ ' ';
}
return s;
}
