# Url Text Mining Boot

Robot para el minado del palabras

Autor: Nicolás Ortiz Valencia
Fecha: 22 Diciembre 2021

## APIS

### [.../conteo_palabras]

Servicio web que tiene como respuesta una lista ordenada de palabras más recurrentes en una página web.

URL: ` https://kakua94.pythonanywhere.com/conteo_palabras?url=<str:url>`

**Parámetros:**
- url: Dominio

Ejemplo:
`https://kakua94.pythonanywhere.com/conteo_palabras?url=https://google.com`

Respuesta:
```json
{
	"conteo": [
		["Google",2],
		["GoogleSearch",1],
		["Images",1],
		["Maps",1],
		["Play",1],
		["YouTube",1],
		["News",1],
		["Gmail",1],
		["Drive",1],
		["More",1],
		["Web",1],
		["History",1],
		["Settings",1],
		["Sign",1],
		["inAdvanced",1],
		["searchAdvertisingProgramsBusiness",1],
		["SolutionsAbout",1],
		["2021",1],
		["Privacy",1],
		["Terms",1]
	]
}
```

### [.../pretty/conteo_palabras]

Servicio web que tiene como respuesta contenido HTML que muestra las palabras más recurrentes dentro de una página web.

Servicio web que tiene como respuesta una lista ordenada de palabras más recurrentes en una página web.

URL: ` https://kakua94.pythonanywhere.com/conteo_palabras?url=<str:url>&&n=<int:n>`

**Parámetros:**
- url: Dominio
- n: número de elementos a mostrar

Ejemplo:
`https://kakua94.pythonanywhere.com/pretty/conteo_palabras?url=http://google.com&&n=3`

Respuesta:


<b>Google:</b> 2
<b>GoogleSearch:</b> 1
<b>Images:</b>1
