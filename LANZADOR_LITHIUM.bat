@echo off
title Lanzador Maestro - Lithium Electronica
cls
echo ==========================================
echo    PANEL DE LANZAMIENTO - LITHIUM
echo ==========================================
echo 1. Abrir NUEVA Landing Page 2026
echo 2. Abrir Calculadora de Costos
echo 3. Abrir Presupuesto Jorge (72V)
echo 4. Abrir Panel de Control (MD)
echo 5. Salir
echo ==========================================
set /p opt="Elija una opcion (1-5): "

if %opt%==1 start chrome "c:\Users\Marcos\Documents\LithiumBateriasPro\01_Ventas_y_Marketing\Landing_Fase_Industrial.html"
if %opt%==2 start chrome "c:\Users\Marcos\Documents\LithiumBateriasPro\02_Administracion_y_Finanzas\Calculadora_Costos_Insumos.html"
if %opt%==3 start chrome "c:\Users\Marcos\Documents\LithiumBateriasPro\01_Ventas_y_Marketing\Presupuesto_Jorge_72V.html"
if %opt%==4 start notepad "c:\Users\Marcos\Documents\LithiumBateriasPro\PANEL_CONTROL_LITHIUM.md"
if %opt%==5 exit

echo Lanzamiento exitoso.
pause
