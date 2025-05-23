# Laboratorio de Pruebas de Software

## Descripción

Este repositorio contiene la implementación de un tokenizador simple en Python junto con pruebas unitarias, de integración y desarrollo dirigido por pruebas (TDD).

## Estructura del proyecto

- `src/`: Código fuente del tokenizador y módulos relacionados.
- `tests/`: Pruebas unitarias e integración usando pytest.
- `user_test.py`: Script para interacción manual con el tokenizador.

## Proceso realizado

1. **Pruebas unitarias:** Se implementaron pruebas para verificar funcionalidades básicas como `encode`, `decode` y conteo de tokens únicos.
2. **Pruebas de integración:** Se probó la interacción entre módulos mediante funciones que combinan funcionalidades.
3. **TDD:** Se aplicó la metodología para agregar la función `unique_token_count`, escribiendo primero la prueba que falló y luego implementando la función.
4. **Pruebas de versión:** Se crearon tags y ramas en Git para simular lanzamientos y validar que las pruebas siguieran pasando.
5. **Pruebas de usuario:** Se desarrolló un script CLI para interacción manual y se diseñó un cuestionario de retroalimentación.

## Cómo ejecutar

- Instalar dependencias:  
  `pip install pytest`

- Ejecutar todas las pruebas:  
  `python -m pytest`

- Ejecutar script de prueba manual:  
  `python user_test.py`

## Conclusiones

- La aplicación pasó todas las pruebas implementadas, demostrando buena calidad y estabilidad.
- La metodología TDD facilitó el desarrollo ordenado y seguro de nuevas funcionalidades.
- La retroalimentación del usuario permitió identificar mejoras en la interfaz.

