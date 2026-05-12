var nombre ='Jose ';
var apellido = ' Montes';
var nombrecompleto = nombre +' '+ apellido; //Primera concatenacion
console.log(nombrecompleto);
var nombrecompleto2 = 'Ariel'+' '+'Betacud'; //Segunda concatenacion
console.log( nombrecompleto2);
var juntos = nombre + 219; //Lee de izq a der sigiendo la cadena lee el numero como tipo string
console.log(juntos);
juntos = nombre + 78 + 17; //Aqui se puede diferenciara tarves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //concatenamos usando el operador simplificado
console.log(nombre);