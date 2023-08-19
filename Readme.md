antlr4 -Dlanguage=Python3 ./Hello.g4 -visitor -o ./yapl/grammar

antlr4-parse ./Hello.g4 program ./example.txt -gui
control z enter

- [ ]  Main
  - [  ] Debe tener una clase Main
  - [  ] La clase main solo puede heredar de IO
  - [  ] La clase Main debe de tener un metodo main sin parametros
  - [  ] La ejecucion inicia evaluando (new Main).main() - NO EN ESTA PARTE

- [  ] BASICS Types
  - [  ] Int, String, Bool
  - [  ] Se puede crear tipos de datos apartir de clases
  - [  ] Las clases de tipos basicos no pueden ser padres de otras clases

- [ ] Scope
  - [  ] Los atributos deben de ser definidos antes de su uso
  - [  ] Un metodo puede ser llamado de forma recursiva - ! COMO VALIDARLO
  - [  ] Ambito global y local, las variables let son locales
  - [  ] Todos los atributos y metodos de las clases son publicos
  - [  ] Scope local tiene prioridad sobre global
  - [  ] Ningun identificador puede ser definido mas de una vez
  - [  ] Si B hereda de A y B sobreescribe un método de A, este método debe de poseer la misma firma con la que fue declarado en A
  - [  ] No se puede herencia multiple y herencia recursiva

- [  ] Default
  - [  ] Int -> 0
  - [  ] String -> "" (cadena vacia)
  - [  ] Bool -> false

- [  ] Casteo
  - [  ] Casteo implicito de Bool a Int (False es 0 y True es 1)
  - [  ] Casteo implicito de Int a Bool (0 es False y 1 es True)
  - [  ] NO se puede casteo explicito

- [ ]  Asignacion
  - [  ] `<id>` <- `<expr>`
  - [  ] El tipo de expr debe ser del mismo tipo de id o puede ser heredado
  - [  ] El valor de `<expr>` se convierte a `<id>`
  - [  ] El tipo de dato de la asignacion es el tipo de `<exp>`
  - [  ] Si `<id>` es un atributo de alguna clase este debe de haberse definido antes
  - [  ] Se pueden tener identificadores recurisivos [class1].[class2].[class3]...

- [  ] Metodos y returns
  - [  ] Los argumentos que son de tipo basicio se pasan por valor
  - [  ] Los argumetnos que son de tipos derivados se pasan po referencia - NOT NEED FOR THIS PART
  - [  ] Los argumentos del metodo son variables locales
  - [  ] Los argumentos se evaluan de izquierda a derecha
  - [  ] El tipo de retorno del metodo debe concidir con tipo de retorno
  - [  ] Si se llama a un metodo en `<id>` <- `<exp>` el return se asiganra al `<id>`

- [  ] Estructuras de control
  - [  ] El tipo estatico de un if o while debe de ser bool
  - [  ] El tipo de dato del condicional if es el tipo de dato del bloque que sea un supertipo de ambas ramas del condicional
  - [  ] El tipo de dato de while es un Objeto

- [  ] Expresiones
  - [  ] Los aritmeticos se aplican a variables tipo int y el resultado es int
  - [  ] Los comparativos se aplica a datos que sean de la misma clase o que sean objetos que hereden de la misma clase. El resultado es bool
  - [  ] La operacion ~ aplicado a tipo int devuelve un tipo int
  - [  ] La operacion not en un dato bool devuelve un tipo bool

- [  ] Clases especiales
  - [  ] Clase IO que define funciones de entrada y salida de int y string
  - [  ] La tabla de simbolos debe de tener definidas las clases IO, Int, String y Bool con sus metodos por defecto.