# 🛠 Chain of Responsibility (Cadena de Responsabilidad) - Patrón de Diseño

**Ejemplo en Python**: Sistema de Soporte Técnico con Manejadores en Cadena.

## 📌 Descripción
Implementación del patrón **Chain of Responsibility** donde una solicitud (ticket de soporte) pasa por una cadena de manejadores hasta que uno la procesa o la cadena termina. Cada manejador decide si puede resolver el problema o lo delega al siguiente nivel.

## 🏗 Estructura del Código
```plaintext
.
├── README.md
└── chain_of_responsibility.py
