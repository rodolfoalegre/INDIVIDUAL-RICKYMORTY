pipeline {
    agent any  // Definición del agente Jenkins que puede ser cualquiera disponible en el sistema

    stages {
        // Etapa 1: Clonar el repositorio desde GitHub
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/rodolfoalegre/INDIVIDUAL-RICKYMORTY.git'  
                // Se clona el repositorio desde la rama 'master' de la URL proporcionada.
            }
        }
        
        // Etapa 2: Ejecutar comandos y validar el archivo README.md
        stage('Run Commands') {
            steps {
                script {
                    // Ejecutar comandos en el contenedor del agente o máquina
                    sh 'echo "Running basic commands..."'  
                    // Imprime en consola un mensaje que indica que los comandos básicos están corriendo.
                    
                    sh 'ls -la'
                    // Lista todos los archivos y directorios en el directorio de trabajo (workspace).
                    
                    sh 'test -f README.md && echo "README.md exists" || echo "README.md is missing"'
                    // Verifica si el archivo README.md existe en el directorio clonado:
                    // Si existe, muestra el mensaje "README.md exists".
                    // Si no existe, muestra el mensaje "README.md is missing".
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            cleanWs()  // Limpia el espacio de trabajo después de la ejecución para liberar espacio.
        }
    }
}