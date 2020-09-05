importar  numpy  como  np
importar  matplotlib . pyplot  como  plt
importar  pandas  como  pd
de  fracciones  importar  fracción

# Función a evaluar
def  f ( x ):
    return  np . float128 ( x ** 3 - 2 * x ** 2 + ( 4 / 3 ) * x - ( 8 / 27 ))

## DECLARACION DE VARIABLES
tolerancia  = [ 10 ** - 8 , 10 ** - 16 , 10 ** - 32 ]     ## Tolerancias a evualuar
n0  =  10000                           ## Limite de iteraciones
x  =  np . arange ( - 2 , 2 , 0,1 )
#x = np. rango (-1, 0,7, 0,1) ## Intervalo
#x = np. rango (0.8, 2, 0.1)
ans  = []                             ## Resultados
ite  = []                             ## Lista de iteraciones
err  = []                             ## Error de los resultados

## DECLARACION DE FUNCIONES
#Metodo de biseccion utilizado para camparar la eficacia en el numero de operaciones
def  metodobiseccion ( f , x0 , x1 , tol ):
    cont  =  0
    mientras que  x1 - x0 > = tol :
        cont  =  cont  +  1
        x2 = np . float128 (( x0 + x1 ) / 2 )
        si  f ( x2 ) == 0 :
            return ( x2 , cont )
        otra cosa :
            si  f ( x0 ) * f ( x2 ) > 0 :
                x0 = x2
            otra cosa :
                x1 = x2
    return ( x2 , cont )

#Metodo de Steffensen que implementa Aitken para acelerar la convergencia
def  Steffensen ( f , p0 , tol ):
   
    resultado  = [ 0 , 0 ]
    para  i  en el  rango ( 1 , n0 ):
        p1  =  np . float128 ( p0  +  f ( p0 ))
        p2  =  np . float128 ( p1  +  f ( p1 ))
        ## Evitar division por cero
        si ( p2  - ( 2 * p1 ) +  p0  ! =  0 ) & ( pow (( p2  -  p1 ), 2 ) ! =  0 ):
            p  =  np . float128 ( p2  - ( pow (( p2  -  p1 ), 2 ) / ( p2  - ( 2 * p1 ) +  p0 )))

        #si el punto inicial satisface la tolerancia da un resultado y lo retorna
        si  abs ( p - p0 ) <  tol :
            resultado [ 0 ] =  p
            resultado [ 1 ] =  i
            volver  resultado
        p0  =  p
    volver  resultado

## GRAFICA DE LA FUNCION

y  = []

para  k  en  x :
    y . añadir ( f ( k ))
    
plt . trama ( x , y )
plt . xlabel ( "x" )
plt . ylabel ( "F (x)" )
plt . título ( "x ^ 3-2x ^ 2 + (4/3) * x- (8/27)" )
plt . cuadrícula ()
plt . mostrar ()


## El siguiente ciclo compara los resultados y el error aproximado por cada una de las 3 tolerancias
xx  = []
iteraciones  = []
bisecIte  = []
para  j  en  tolerancia :
    
    cont  =  0
    ans . claro ()
    ite . claro ()
    err . claro ()
    xx . claro ()
    
    
    #Se emplea el metodo de Steffensen para evaluar cada punto del intervalo dado
    para  k  en  x :
        
        si ( Steffensen ( f , k , j ) [ 1 ] ! =  0 ):
            ans . añadir ( Steffensen ( f , k , j ) [ 0 ])
            ite . añadir ( Steffensen ( f , k , j ) [ 1 ])
            xx . añadir ( k )
            si ( cont > 3 ):
                temp  =  abs (( ans [ cont - 2 ] - ans [ cont - 1 ]) / ans [ cont - 2 ]) * 100
                si ( temperatura > 20 ):
                    err . añadir ( 1 )
                otra cosa :
                    err . añadir ( temp )
            si ( cont <= 3 ):
                err . añadir ( 0 )
            cont  =  cont  +  1
    
    plt . plot ( xx , ans , label  =  "Resultados" )
    plt . plot ( xx , err , label  =  "Error" )
    plt . plot ( x , y , label  =  "Funcion" )
    plt . xlim ( 0 , 2 )
    plt . ylim ( - 0,3 , 1 )
    plt . xlabel ( "x" )
    plt . ylabel ( "F (x)" )
    plt . leyenda ()
    plt . título ( "Metodo de Steffensen" +  str ( j ))
    plt . cuadrícula ()
    plt . mostrar ()
    
    #Se extrae la posición en el arreglo de errores para mostrarlo por consola
    p = 100
    cont  =  0
    porque  yo  en  err :
        si ( p > abs ( i )):
            p  =  cont
        cont  =  cont  +  1
    
    #Resultados metodo de Steffensen
    print ( "Tolerancia:" , j )
    print ( "El resultado es:" , ans [ p ])
    print ( "La función de actualización en el resultado es:" , f ( ans [ p ]))
    print ( "El numero maximo de iteraciones es:" , min ( ite ))
    
    h  =  metodobiseccion ( f , min ( x ), max ( x ), j )
    
    #Resultados metodo de bisección
    print ( "Resultado con el metodo de biseccion:" +  str ( h [ 0 ]))
    print ( "Numero de iteraciones:" +  str ( h [ 1 ]))
    
    # Cálculo del error entre ambos metodos
    t  = ( abs ( ans [ p ] - h [ 0 ]) / ans [ p ]) *  100
    print ( "El error entre ambos metodos es:" , '{0: .2g}' . formato ( t ))
    
    iteraciones . añadir ( min ( ite ))
    bisecIte . añadir ( h [ 1 ])
     
    
#Grafica donde se relaciona las iteraciones en la stres tolerancias para cada uno de los métodos empleados
data  = { 'Iteraciones Steffensen' : iteraciones ,
        'Iteraciones Biseccion' : bisecIte ,
        'Tolerancias' : [ "10 ^ -8" , "10 ^ -16" , "10 ^ -32" ]}
  
df  =  pd . DataFrame ( datos )
higo , ax  =  plt . subtramas ()
ax  =  gl . plot ( kind  =  'bar' , x  =  'Tolerancias' , title =  'Comportamiento respecto a la tolerancia x ^ 3-2x ^ 2 + 4 / 3x-8/27' , ax  =  ax )

para  p  en  ax . parches :
    hacha . anotar ( str ( p . get_height ()), ( p . get_x () *  1.005 , p . get_height () *  1.005 ))
