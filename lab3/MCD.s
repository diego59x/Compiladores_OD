.data
num1: .word 10  # Primer numero
num2: .word 2  # Segundo numero

result: .word 0  # Variable para almacenar el resultado (MCD)
newline: .asciiz "\n"

.text
.globl main

main:
    # Cargar los valores de num1 y num2 en registros
    lw $a0, num1
    lw $a1, num2

    # Llamar a la funcion recursiva para calcular el MCD
    jal mcd

    # Almacenar el resultado en la variable result
    sw $v0, result

    li $v0, 1
    lw $a0, result
    syscall

    # Imprimir el resultado
    li $v0, 4
    la $a0, newline
    syscall
    
    # Salir del programa
    li $v0, 10
    syscall

mcd:
    # Guardar registros
    addi $sp, $sp, -8
    sw $ra, 4($sp)
    sw $a1, 0($sp)

    # Verificar si el segundo numero es igual a cero (caso base)
    beqz $a1, base_case

    # Calcular el residuo
    div $a0, $a1
    mfhi $t0  # El residuo se almacena en $t0
    move $a0, $a1
    move $a1, $t0

    # Llamar recursivamente con los valores actualizados
    jal mcd

    # Restaurar registros
    lw $a1, 0($sp)
    lw $ra, 4($sp)
    addi $sp, $sp, 8

    jr $ra

base_case:
    move $v0, $a0  # El MCD se encuentra en $v0
    jr $ra
