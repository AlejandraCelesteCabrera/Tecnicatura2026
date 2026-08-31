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

//Hoy no se utiliza var, se tutiliza let y const
let nomnre2 ="Pedro";
consel.Log(nombre);

const apellido2 ="Lopez";
//Apellido2 = "peres"; una constante no puede ser modificada
console.Log(apellido2)

let x, y;// se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; //se pueden hacer asignacion de varias variables dentro de la misma línea
let z= x + y; //Se asigna el valor de la operación
console.Log(z)

let _1num = 31;//No utilizar números para iniciar el nombre de una variable
let rompiendo ="rompe";//No utilizar palabras reservadas para variables

console.Log (_1num);
console.Log (rompiendo);
