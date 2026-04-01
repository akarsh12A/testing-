pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY = "python-sample-project"
        SONAR_PROJECT_NAME = "Python Sample Project"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/akarsh12A/testing-.git'
            }
        }

        stage('Set Up Python') {
            steps {
                sh '''
                python3 --version
                pip3 install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                if [ -f requirements.txt ]; then
                    pip3 install -r requirements.txt
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
                      -Dsonar.language=py \
                      -Dsonar.python.version=3
                    '''
                }
            }
        }
    }
}
