pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY = "akarsh-python-project"
        SONAR_PROJECT_NAME = "Akarsh Python Sonar Project"
    }

    stages {

        stage('Set Up Python') {
            steps {
                sh '''
                python3 --version
                python3 -m ensurepip --upgrade || true
                python3 -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                if [ -f requirements.txt ]; then
                    python3 -m pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube-Server') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=$SONAR_PROJECT_KEY \
                      -Dsonar.projectName="$SONAR_PROJECT_NAME" \
                      -Dsonar.sources=. \
                      -Dsonar.python.version=3
                    '''
                }
            }
        }
    }
}
