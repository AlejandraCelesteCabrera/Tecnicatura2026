//Tipos de Datos en JavaScript
/*
La sisntexi en lo que es comentarios 
es muy similar a la de Java
realmente diriamos que es identica
*/
var nombre ="Celeste"
console.log(nombre);
nombre= 7;
var numero = 3000;
console.log(numero);
numero=12.3;
var objeto ={
        nombre : "Celeste",
        apellido : "Cabrera",
        telefono : "20202020"

}

console.log(objeto);

//Tipo de datos boolean
 var bandera = true;
 console.log (bandera);

//Tipos de dato funcion
function miFuncion() {}
console.log(miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase
class Persona {
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }    
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log (typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su orgigen es de tipo object
console.log(typeof y);

//Tipo de datos array y Empty String
var autos = ['Cintroen','Audi','BMW','Ford' ];
console.log(autos);
console.log(typeof autos);//Preguntamos que tipo de dato es:

var z = '';
console.log(z);//Esto se refiere a que es una cadena vacia:
console.log(typeof z);
