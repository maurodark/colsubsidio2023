var nombre = "Mauricio Pe;a"
var profesion = "Publicista"
var cargo = "Director Creativo"
var estatura = 43

document.write("Hola!!")

var datos = document.getElementById("datos")
//comentarios
datos.innerHTML = `
    <h2>Nuevos datos</h2>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda nulla ipsam similique non vel tempore quidem veniam placeat necessitatibus! Unde repudiandae velit eaque deserunt aspernatur molestias sapiente incidunt est quia!</p>
    <h5>Nombre: ${nombre}</h5>
    <h5>Profesion :${profesion}</h5>
    <h5>Cargo: ${cargo}</h5>
`   

//Sentencias condicionales
if(estatura >= 40)
    {
//insertar html
    datos.innerHTML += '<h2>Estatura es 40</h2>';
    document.write("ssssQue se dice!")
    }
else
{
    datos.innerHTML += '<h2>No tienes estatura</h2>';

}

//Ciclo for
for(var i = 2020; i<=2023; i++)
{
    datos.innerHTML += "<h3>Estamos en el año:</h3>" + i;
}