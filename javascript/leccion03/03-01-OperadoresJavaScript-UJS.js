//Ejercicio para encontrar numero pares
let parInpar = 9;
if(parInpar % 2 == 0){
    console.log("Es un número par");
}
else{
    console.log("Es un número impar");
}

//Ejercicio: es mayor de edad
let edad = 13, adulto =18;
if(edad >= adulto){
    console.log("Usted es mayor de edad");
}
else{
    console.log("Usted es menor de edad");
}

//Ejercicio: Dentro de un rango
let dentroRango =5;//Aqui vamos a ir cambiando el valor
let valMin =0, valMax =10;
if (dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}

//Ejercicio:Si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if( dentroRango || diaDescanso){
    console.log("El padre puede assitir al juego de su hijo")
}
else{
    console.log("El padre no puede assitir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero = 9;
resultado2 = numero % 2 == 0? "Es un número PAR" : "Es un número IMPAR";
console.log(resultado2)

//Convertir String a Number
let miNumero = "18"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero);//Esta es una función
console.log(typeof edad2);
//Funcion uinNaN
if(isNaN(edad2)){ //No es un número=is not a Number(devuelve un resultado booleando)
    console.log("Esta variable no contiene solo números")
}
else{
    if(edad2 >= 18){
        console.log("Puede votar")
    }
    else{
         console.log("Muy joven para votar")

    }
}
//Operador ternario
let resultado3 = edad2 >= 10 ? "Puede votar" :"Es muy joven para votar"
console.log(resultado3);
