/**
 * como poder tipar un objecto en TS
 * para elos tenemos 2 soluciones:
 *  1.- interface: la cual me permite poder definir los atributois 
 *  del objeto del tipo de datos de data atributo
 * 
 *  2.- type: lo mismo que interface.
 * 
 * 
 */

interface Persona{
    nombre : string;
    apellido :string;
    dni : number;
    edad :number;
    direccion: string;
  }

type Persona2 = {
    nombre: string;
    apellido: string;
    dni: number;
    edad: number;
    direccion?: string;
  };

const persona: Persona = {
    nombre: "Pepe",
    apellido: "Perez",
    dni: 22424242,
    edad: 82, 
    direccion: "av. mi casa123"
  };

const persona2: Persona2 = {
    nombre: "Juan",
    apellido: "Perez",
    dni: 88888,
    edad: 29,
  };
function saludar(persona: Persona) {
    console.log(
        `Hola me llamo ${persona.nombre} ${persona.apellido} y trengo ${persona.edad} años de edad`)
  }
  saludar(persona);