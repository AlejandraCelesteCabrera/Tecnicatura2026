//Ejerciccio1: Calcular estación del año

let mes = 4;
let estacion;
if(mes ==1 || mes == 2 || mes == 12){
    estacion="Verano";
}
else if (mes == 3 || mes == 4 || mes == 5){
    estacion="Otoño";
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion="Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion="Primavera";
}
else {
    estacion ="Valor incorrecto";
}
console.log("El valor corresponde a la estacion de: "+estacion);

//Ejercicio2: Hora del día
let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Goor morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good afternoon";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good night";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);