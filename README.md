
**Formularios**

*Login / registro:* Forms

*Post:* ModelForm


---
**APIs**

Creadas con APIView

*User*: Serializer

*Post*: ModelSerializer

---
Endpoints
--

**Listado de users**

URL/api/1.0/users (GET)

**Crear user**

URL/api/1.0/users (POST)

**Detalle users**

URL/api/1.0/users/<id user> (GET)

**Update User**

URL/api/1.0/users/<id user> (PUT)

**Delete User**

URL/api/1.0/users/<id user> (DELETE)

**Listado de Blogs**

URL/api/1.0/blogs/

**Listado filtrado por user y orden asc/desc**

URL/api/1.0/blogs/[<username>][/0|1]

**Crear post**

URL/api/1.0/post/ (POST)

**Detalle Post**

URL/api/1.0/post/<post id> (GET)

**Actualizar Post**

URL/api/1.0/post/<post id> (PUT)

**Eliminar Post**

URL/api/1.0/post/<post id> (DELETE)

**LISTADO POSTS DE UN USUARIO CON SEARCH y ORDEN**

URL/api/1.0/posts/<user_name>[/search=<texto_de_busqueda>][/order=<[-]publish_date|[-]title>]