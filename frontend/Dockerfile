# Imagen base de Node.js
FROM node:18

# Carpeta de trabajo en el contenedor
WORKDIR /app

# Copia archivos de dependencias (asegura que package-lock.json también se copie si existe)
COPY frontend/package*.json ./

# Instala las dependencias del proyecto
RUN npm install

# Copia el resto del código fuente al contenedor
COPY frontend/. .

# Puerto por defecto de Vite en desarrollo
EXPOSE 5173

# Inicia la app con el servidor de desarrollo de Vite
CMD ["npm", "run", "dev"]
