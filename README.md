# Plataforma de Autenticación con Flask

## Descripción
Bienvenido a este Authentication, una aplicación web potenciada por Flask que ofrece una funcionalidad de autenticación y una experiencia de inicio de sesión.

## Tecnologías Utilizadas
- Flask: Framework web ágil y potente de Python
```bash
pip install Flask
```
- SQLAlchemy: ORM para interacción con bases de datos
```bash
pip install SQLAlchemy
```
- Werkzeug: Herramientas web eficientes para Python
```bash
pip install Werkzeug
```
- MySQL: Sistema de gestión de bases de datos relacional
```bash
pip install pymysql
```

## Caracteristicas
- Registro de usuarios fácil y seguro
- Inicio de sesión con autenticación hash
- Página de inicio personalizada con mensajes de bienvenida
- Integración sin problemas con bases de datos MySQL

## Configuración Rápida
## Configuración Rápida
1. **Configuración del Entorno Virtual (Opcional, pero Recomendado)**
   - Crea un entorno virtual (se recomienda, pero es opcional):
     ```bash
     python -m venv venv
     ```
   - Activa el entorno virtual:
     - En Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - En Linux/Mac:
       ```bash
       source venv/bin/activate
       ```
2. ** Configura la base de datos en config.py **
```
SQLALCHEMY_DATABASE_URI='mysql+pymysql://tu_usuario:tu_contraseña@localhost:3306/tu_basededatos'
```
