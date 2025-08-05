# 🧩 Chain of Responsibility - Ejemplo en Python

**Ejemplo**: Sistema de tickets de soporte técnico con tres niveles de atención.

🔗 **[Ver código completo en GitHub](https://github.com/manu-mx/block_responsability_manu/block_responsability_pi1.py)**

## 🛠️ Cómo funciona
1. **Cadena de manejo**:
   - Soporte Básico → Soporte Avanzado → Especialista
2. **Cada nivel atiende tickets según su complejidad**:
   - Básico: Nivel 1
   - Avanzado: Nivel 3
   - Especialista: Nivel 5
3. **Si ningún nivel puede atenderlo**, se marca como derivado

## 📋 Resultado esperado
```plaintext
Nuevo ticket (Nivel 1): No puedo iniciar sesión.
[Soporte Básico] Resuelto: 'No puedo iniciar sesión.'

Nuevo ticket (Nivel 3): Error al conectar a la base de datos.
[Soporte Avanzado] Resuelto: 'Error al conectar a la base de datos.'

Nuevo ticket (Nivel 5): Fallo crítico en el servidor.
[Especialista] Resuelto: 'Fallo crítico en el servidor.'

Nuevo ticket (Nivel 6): Bug en el núcleo del sistema.
[Especialista] Ticket demasiado complejo: 'Bug en el núcleo del sistema.' (Derivado a desarrollo)
